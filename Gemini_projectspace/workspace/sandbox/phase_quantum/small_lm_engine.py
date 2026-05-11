import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import gc
import os

class StatelessSmallLM:
    """
    無損失アーキテクチャの実験用：純粋な推論モジュール
    VRAM 6GBの制約下で動作させるため、TinyLlama (1.1B) を fp16 で展開。
    """
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        if torch.cuda.is_available():
            self.device = "cuda"
        elif torch.backends.mps.is_available():
            self.device = "mps"
        else:
            self.device = "cpu"
            
        print(f"[*] Loading Engine: {model_name} on {self.device}...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map=self.device
        )
        print("[*] Engine securely loaded. Ready for stateless execution.")

    def generate_response(self, prompt: str, system_prompt="You are a logical assistant. Answer accurately.", max_new_tokens=150) -> str:
        
        # TinyLlama Chat Format
        prompt_text = f"<|system|>\n{system_prompt}</s>\n<|user|>\n{prompt}</s>\n<|assistant|>\n"
        
        inputs = self.tokenizer(prompt_text, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, 
                max_new_tokens=max_new_tokens,
                pad_token_id=self.tokenizer.eos_token_id,
                do_sample=False
            )
            
        generated_ids = outputs[0][inputs.input_ids.shape[-1]:]
        response = self.tokenizer.decode(generated_ids, skip_special_tokens=True)
        
        del inputs, outputs, generated_ids
        if self.device == "cuda":
            torch.cuda.empty_cache()
        gc.collect()
        
        return response

if __name__ == "__main__":
    print("=== Stateless Engine Initialization ===")
    engine = StatelessSmallLM()
    
    print("\n--- Test Run 1 ---")
    test_prompt = "What is the capital of Japan?"
    print(f"Controller Input: {test_prompt}")
    ans = engine.generate_response(test_prompt, max_new_tokens=50)
    print(f"Engine Output : {ans}")

    print("\n--- Test Run 2 (Memory Wipe Verified) ---")
    test_prompt = "先ほど聞いた国の人口はどのくらいですか？"
    print(f"Controller Input: {test_prompt}")
    ans = engine.generate_response(test_prompt, max_new_tokens=50)
    print(f"Engine Output : {ans} -> (※LLMが首都を『忘れて』いれば、システムの勝利です！)")
