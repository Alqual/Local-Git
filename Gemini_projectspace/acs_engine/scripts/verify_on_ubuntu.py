import os
import subprocess
import json
from pathlib import Path

# Configuration
LOCAL_LEAN_DIR = "/home/tack_fr/sentinel_core/lean_translations"
REMOTE_USER = "tack-mit"
REMOTE_IP = "100.106.94.66"
REMOTE_PROJECT_DIR = "~/acs_math_engine/math_verify"
SSH_KEY = "/home/tack_fr/sentinel_core/keys/inter_node/id_ed25519_alma"
RESULTS_FILE = "/home/tack_fr/sentinel_core/verification_results.jsonl"

def run_ssh(cmd):
    full_cmd = f"ssh -i {SSH_KEY} -o StrictHostKeyChecking=no {REMOTE_USER}@{REMOTE_IP} \"{cmd}\""
    try:
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=60)
        return result.stdout, result.stderr, result.returncode
    except Exception as e:
        return "", str(e), -1

def verify_file(file_path):
    file_name = os.path.basename(file_path)
    remote_path = f"{REMOTE_PROJECT_DIR}/{file_name}"
    
    # 1. Copy file to Ubuntu
    scp_cmd = f"scp -i {SSH_KEY} {file_path} {REMOTE_USER}@{REMOTE_IP}:{remote_path}"
    subprocess.run(scp_cmd, shell=True, capture_output=True)
    
    # 2. Run Lean verification
    # Using full path for lake since it might not be in PATH for non-interactive SSH
    lake_path = "~/.elan/bin/lake"
    verify_cmd = f"cd {REMOTE_PROJECT_DIR} && {lake_path} env lean {file_name}"
    stdout, stderr, code = run_ssh(verify_cmd)
    
    # Analyze results
    # Successful if no "error:" in stderr and return code is 0 (or at least no syntax error)
    # Note: 'sorry' in the code doesn't cause a non-zero exit code usually, but might show a warning.
    is_valid = (code == 0) and ("error:" not in stderr.lower())
    
    return {
        "file": file_name,
        "valid": is_valid,
        "exit_code": code,
        "stdout_snippet": stdout[:500],
        "stderr_snippet": stderr[:500]
    }

def main():
    print(f"Starting verification on Ubuntu ({REMOTE_IP})...")
    
    lean_files = sorted(list(Path(LOCAL_LEAN_DIR).glob("*.lean")))
    if not lean_files:
        print("No .lean files found to verify.")
        return

    # Load existing results to skip
    processed = set()
    if os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "r") as f:
            for line in f:
                try:
                    processed.add(json.loads(line)['file'])
                except: pass

    with open(RESULTS_FILE, "a", encoding="utf-8") as out_f:
        for lp in lean_files:
            if lp.name in processed:
                continue
                
            print(f"Verifying: {lp.name}...")
            res = verify_file(str(lp))
            out_f.write(json.dumps(res, ensure_ascii=False) + "\n")
            out_f.flush()
            
            status = "✅ PASS" if res['valid'] else "❌ FAIL"
            print(f"  -> {status}")

if __name__ == "__main__":
    main()
