#!/usr/bin/env python3
import os
import subprocess
import json
from datetime import datetime

def run_command(command, cwd=None):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, cwd=cwd)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command}")
        print(e.stderr)
        return None

def get_current_phase(registry_path):
    try:
        with open(registry_path, 'r') as f:
            data = json.load(f)
            return data.get('current_phase', 'Unknown Phase')
    except Exception:
        return 'Unknown Phase'

def get_latest_report(notebooks_dir):
    latest_file = None
    latest_time = 0
    for root, dirs, files in os.walk(notebooks_dir):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                mtime = os.path.getmtime(path)
                if mtime > latest_time:
                    latest_time = mtime
                    latest_file = file
    return latest_file

def main():
    # Paths (relative to script location or project root)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming the script is in Gemini_projectspace/fixed/meta_management/
    project_root = os.path.abspath(os.path.join(script_dir, "../../"))
    registry_path = os.path.join(script_dir, "registry.json")
    notebooks_dir = os.path.join(project_root, "workspace/notebooks")

    print(f"--- Research Sync Started at {datetime.now().isoformat()} ---")
    
    # 1. Get Context
    phase = get_current_phase(registry_path)
    latest_report = get_latest_report(notebooks_dir)
    
    # 2. Check for changes
    status = run_command("git status --short", cwd=project_root)
    if not status:
        print("No changes to sync.")
        return

    print("Changes detected:")
    print(status)

    # 3. Stage changes
    print("Staging changes...")
    run_command("git add -A", cwd=project_root)

    # 4. Commit
    commit_msg = f"[{phase}] Research update"
    if latest_report:
        commit_msg += f": {latest_report}"
    else:
        commit_msg += f" (Manual sync at {datetime.now().strftime('%Y-%m-%d %H:%M')})"
    
    print(f"Committing with message: {commit_msg}")
    run_command(f'git commit -m "{commit_msg}"', cwd=project_root)

    # 5. Push
    current_branch = run_command("git branch --show-current", cwd=project_root)
    print(f"Pushing to origin {current_branch}...")
    # Note: This might still fail if authentication is required, 
    # but the user can run the script manually and handle the prompt.
    run_command(f"git push origin {current_branch}", cwd=project_root)

    print("--- Research Sync Completed ---")

if __name__ == "__main__":
    main()
