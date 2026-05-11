import sys
import os

# Add parent directory to path to import acs_engine modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from acs_engine.core.verifier import ACSVerifier
from acs_engine.core.governor import ACSGovernor

def test_tit_problem():
    print("Initializing ACS Reasoning Loop Test...")
    verifier = ACSVerifier()
    governor = ACSGovernor(model_name="mathstral")

    initial_prompt = """Let a, b, c be three positive integers such that their greatest common divisor is 1.
Find all positive integers that can be the greatest common divisor of a + b + c, a^2 + b^2 + c^2, a^3 + b^3 + c^3.
Please provide the final set of answers CLEARLY in curly braces like this: {1, 2, 3, 6}.
Then explain your reasoning step-by-step."""

    final_response, success = governor.run_loop(initial_prompt, verifier, max_iterations=10)

    if success:
        print("\n[RESULT] Convergence achieved.")
    else:
        print("\n[RESULT] Max iterations reached without full convergence.")

if __name__ == "__main__":
    test_tit_problem()
