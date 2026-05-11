import os
import sys
import time
import json
import re

# Add acs_engine to path
sys.path.append(os.path.join(os.getcwd(), "acs_engine"))
from core.python_logic_runner import PythonLogicRunner

def call_llm(prompt):
    """Calls Ollama (mathstral) to generate a response."""
    try:
        # Use a temporary file for the prompt to avoid shell escaping issues
        prompt_file = "acs_engine/data/current_prompt.txt"
        with open(prompt_file, "w") as f:
            f.write(prompt)
        
        cmd = f"ollama run mathstral < {prompt_file}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error calling LLM: {str(e)}"

def run_loop():
    workspace_root = os.getcwd()
    runner = PythonLogicRunner(workspace_root)
    
    log_file = "acs_engine/data/logic_reasoning_log.md"
    progress_file = "acs_engine/data/logic_progress_report.md"
    
    with open(log_file, "w") as f:
        f.write("# Python/Z3 Formal Verification Log: Osaka Univ 2025\n\n")

    problem = "Polynomial f(x) = x^3 + 3px^2 + 3mx. Prove that f''(-p) = 0 for any real numbers p and m."

    strategy = "Initial attempt using SymPy to differentiate and Z3 to prove the identity."
    feedback = "None"
    
    for i in range(1, 11):
        print(f"--- Logic Iteration {i} ---")
        
        prompt = f"""
You are an autonomous mathematical verification agent.
Goal: {problem}

Instructions:
1. Write a Python script that uses SymPy to calculate the second derivative.
2. Use Z3 (z3-solver) to formally prove the result is 0 for all p, m.
3. Print "VERIFICATION_SUCCESSFUL" only if the proof holds.
4. Provide the full code in a single ```python ... ``` block.

Current Strategy: {strategy}
Last Feedback: {feedback}
"""
        response = call_llm(prompt)
        
        # Extract python code
        code_match = re.search(r"```python\n(.*?)\n```", response, re.DOTALL)
        if not code_match:
            feedback = "Error: No python code block found in your response. Please provide code in ```python ... ```."
            continue
            
        code = code_match.group(1)
        
        # Log the attempt
        with open(log_file, "a") as f:
            f.write(f"## Iteration {i}\n\n### Response:\n{response}\n\n")
            
        # Verify
        result = runner.verify_code(code)
        
        if result["status"] == "success":
            print(f"SUCCESS: {result['message']}")
            with open(log_file, "a") as f:
                f.write(f"### Result: SUCCESS\n{result['message']}\n\n")
            break
        else:
            print(f"FAILED: Feedback provided to model.")
            feedback = result["all_output"]
            with open(log_file, "a") as f:
                f.write(f"### Result: ERROR\n```\n{feedback}\n```\n\n")
            
        # Update progress
        with open(progress_file, "w") as f:
            f.write(f"# Logic Progress: Iteration {i}\nStatus: {result['status']}\nLast Error: {feedback[:200]}...")

    print("--- Loop Finished ---")

if __name__ == "__main__":
    run_loop()
