import json
import os
from lean_translator import translate_problem

os.environ["GEMINI_API_KEY"] = "AIzaSyDJI9mEZobZTOp3OaYhQAohw1J3nQaadNU"

prob_text = "三角形ABCにおいて、AB=3, BC=4, CA=5のとき、三角形の面積を求めよ。"
print("Testing translation...")
res = translate_problem(prob_text)
print(f"RESULT:\n{res}")
