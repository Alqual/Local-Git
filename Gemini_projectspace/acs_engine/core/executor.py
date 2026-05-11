import subprocess
import os

class ACSExecutor:
    def __init__(self, workspace_root):
        self.workspace_root = workspace_root
        self.conda_path = os.path.join(workspace_root, "acs_engine/llm_env/miniconda/bin/conda")
        self.env_name = "acs_env"

    def run_python_code(self, code):
        """Runs the provided Python code within the acs_env environment."""
        # Temporary script file
        script_path = os.path.join(self.workspace_root, "acs_engine/scripts/temp_exec.py")
        with open(script_path, "w") as f:
            f.write(code)
        
        try:
            result = subprocess.run(
                [self.conda_path, "run", "-n", self.env_name, "python", script_path],
                capture_output=True,
                text=True,
                check=True
            )
            return {"status": "success", "stdout": result.stdout, "stderr": result.stderr}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "stdout": e.stdout, "stderr": e.stderr}

if __name__ == "__main__":
    # Self-test
    executor = ACSExecutor("/home/tack-mit/デスクトップ/Gemini_projectspace")
    test_code = "import torch; print(f'Torch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
    print(executor.run_python_code(test_code))
