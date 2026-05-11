import time
import os
import re

LOG_FILE = "/home/tack-mit/デスクトップ/Gemini_projectspace/acs_engine/data/lean_reasoning_log.md"
REPORT_FILE = "/home/tack-mit/デスクトップ/Gemini_projectspace/acs_engine/data/progress_report.md"

def get_latest_iteration():
    if not os.path.exists(LOG_FILE):
        return "Log file not found."
    
    with open(LOG_FILE, "r") as f:
        content = f.read()
    
    # Find all iterations
    iterations = re.findall(r"## Iteration (\d+)", content)
    if not iterations:
        return "No iterations recorded yet."
    
    latest_num = max(map(int, iterations))
    
    # Extract the block for the latest iteration
    blocks = content.split("## Iteration")
    latest_block = ""
    for block in reversed(blocks):
        if block.strip().startswith(str(latest_num)):
            latest_block = block
            break
            
    # Extract status and error
    status_match = re.search(r"### Result: (\w+)", latest_block)
    status = status_match.group(1) if status_match else "unknown"
    
    error_match = re.search(r"### Compiler Errors:\n```\n(.*?)\n```", latest_block, re.DOTALL)
    error = error_match.group(1).strip() if error_match else "No errors recorded."
    
    # Simple logic analysis
    logic = "Still trying to fix syntax or basic differentiation."
    if "deriv_" in latest_block:
        logic = "Model is attempting to use specific calculus lemmas (e.g., deriv_pow)."
    if "by" in latest_block:
        logic += " Using Lean 4 'by' syntax correctly."
    if "∇" in latest_block:
        logic = "CAUTION: Model is hallucinating non-Lean symbols (∇)."

    return {
        "num": latest_num,
        "status": status,
        "error": error,
        "logic": logic,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def main():
    print("Starting progress reporter...")
    while True:
        data = get_latest_iteration()
        
        with open(REPORT_FILE, "w") as f:
            f.write(f"# ACS Autonomous Progress Report\n\n")
            if isinstance(data, str):
                f.write(f"Status: {data}\n")
            else:
                f.write(f"## Current Status: Iteration {data['num']}\n")
                f.write(f"- **Time**: {data['timestamp']}\n")
                f.write(f"- **Last Result**: {data['status']}\n")
                f.write(f"- **Current Strategy**: {data['logic']}\n\n")
                f.write(f"### Latest Compiler Feedback\n```\n{data['error']}\n```\n\n")
                f.write(f"---\n*Next update in 5 minutes...*\n")
        
        time.sleep(300)

if __name__ == "__main__":
    main()
