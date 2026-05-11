import requests
import json
import re
import os

class ACSGovernor:
    def __init__(self, model_name="mathstral"):
        self.model_name = model_name
        self.url = "http://localhost:11434/api/generate"

    def ask_llm(self, prompt):
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": True
        }
        live_log = os.path.join(os.path.dirname(__file__), "../data/live_thinking.txt")
        
        # Clear live log for new prompt
        with open(live_log, "w") as f:
            f.write(f"--- Thinking Start ({self.model_name}) ---\n")

        full_response = ""
        response = requests.post(self.url, json=payload, stream=True)
        for line in response.iter_lines():
            if line:
                chunk = json.loads(line)
                token = chunk.get("response", "")
                full_response += token
                # Write to live log immediately
                with open(live_log, "a") as f:
                    f.write(token)
                    f.flush()
                if chunk.get("done"):
                    break
        
        with open(live_log, "a") as f:
            f.write("\n--- Thinking End ---\n\n")
            
        return full_response

    def extract_answers(self, text):
        """Extracts numerical list from LLM response like {1, 2, 3} or [1, 2, 3]."""
        # Look for patterns like {1, 2, 3} or [1, 2, 3]
        match = re.search(r"[\{\[]([\d\s,]+)[\}\]]", text)
        if match:
            nums = re.findall(r"\d+", match.group(1))
            return [int(n) for n in nums]
        return []

    def run_loop(self, initial_prompt, verifier, max_iterations=10):
        ground_truth = verifier.get_ground_truth_tit2022()
        current_prompt = initial_prompt
        history = []

        log_file = os.path.join(os.path.dirname(__file__), "../data/reasoning_log.md")
        with open(log_file, "w") as f:
            f.write(f"# Reasoning Loop Log\n\n- Model: {self.model_name}\n\n")

        for i in range(max_iterations):
            print(f"\n--- Iteration {i+1} ---")
            response = self.ask_llm(current_prompt)
            print(f"RAW RESPONSE: {response}")
            answers = self.extract_answers(response)
            eval_result = verifier.evaluate_answer(answers, ground_truth)

            # Log to file
            with open(log_file, "a") as f:
                f.write(f"## Iteration {i+1}\n\n")
                f.write(f"### Answer: {answers}\n")
                f.write(f"### Evaluation: {eval_result}\n\n")
                f.write(f"### Full Response:\n{response}\n\n")
                f.write("---\n\n")

            print(f"LLM Answer set: {answers}")
            print(f"Evaluation: {eval_result}")

            if eval_result["is_correct"]:
                print("Success! The model found the correct and complete set.")
                return response, True

            # Generate feedback
            feedback = f"\n\n[System Feedback]: Your answer {answers} is incomplete or incorrect.\n"
            if eval_result['missing']:
                feedback += f"- Missing values found by computer search: {eval_result['missing']}\n"
            if eval_result['excess']:
                feedback += f"- Incorrect values that shouldn't be there: {eval_result['excess']}\n"
            
            feedback += "Please re-examine your proof. Look for logical leaks, especially regarding parity or prime factors of coefficients in polynomial identities. Do not hallucinate math. Provide a rigorous proof."
            
            current_prompt += f"\n\nYour previous response was:\n{response}\n{feedback}"
            history.append(response)

        return history[-1], False
