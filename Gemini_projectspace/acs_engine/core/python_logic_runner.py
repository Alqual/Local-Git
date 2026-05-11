import subprocess
import os
import sys

class PythonLogicRunner:
    def __init__(self, workspace_root):
        self.workspace_root = workspace_root
        self.target_file = os.path.join(workspace_root, "acs_engine/sandbox/logic_verification.py")
        self.python_exe = os.path.join(workspace_root, "acs_engine/llm_env/miniconda/envs/acs_env/bin/python")

    def verify_code(self, python_code):
        """Executes Python code and checks for logical success."""
        # Write code to target file
        with open(self.target_file, "w") as f:
            f.write(python_code)
        
        try:
            # Execute the script
            result = subprocess.run(
                [self.python_exe, self.target_file],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            output = result.stdout + result.stderr
            
            # Success condition: return code 0 and a specific success string from the script
            # We'll ask the model to print "VERIFICATION_SUCCESSFUL" if Z3/SymPy proves it.
            if result.returncode == 0 and "VERIFICATION_SUCCESSFUL" in output:
                return {"status": "success", "message": "Logic verified successfully via Python/Z3/SymPy."}
            else:
                return {
                    "status": "error",
                    "all_output": output if output else f"Process exited with code {result.returncode}"
                }
        except subprocess.TimeoutExpired:
            return {"status": "error", "all_output": "Execution timed out (30s)."}
        except Exception as e:
            return {"status": "exception", "error": str(e)}

if __name__ == "__main__":
    # Test
    runner = PythonLogicRunner(".")
    test_code = """
import sympy as sp
x = sp.symbols('x')
expr = (x + 1)**2 - (x**2 + 2*x + 1)
if sp.simplify(expr) == 0:
    print("VERIFICATION_SUCCESSFUL")
"""
    print(runner.verify_code(test_code))
