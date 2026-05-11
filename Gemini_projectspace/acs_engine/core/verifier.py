import math
import sympy as sp

class ACSVerifier:
    def __init__(self):
        pass

    def get_ground_truth_tit2022(self, limit=20):
        """Generates the ground truth for the TIT 2022 problem."""
        found_gcds = set()
        for a in range(1, limit):
            for b in range(1, limit):
                for c in range(1, limit):
                    if math.gcd(a, math.gcd(b, c)) == 1:
                        s1 = a + b + c
                        s2 = a**2 + b**2 + c**2
                        s3 = a**3 + b**3 + c**3
                        g = math.gcd(s1, math.gcd(s2, s3))
                        found_gcds.add(g)
        return sorted(list(found_gcds))

    def evaluate_answer(self, llm_answer_list, ground_truth):
        """Compares LLM answers with ground truth."""
        llm_set = set(llm_answer_list)
        gt_set = set(ground_truth)
        
        missing = gt_set - llm_set
        excess = llm_set - gt_set
        
        return {
            "is_correct": len(missing) == 0 and len(excess) == 0,
            "missing": sorted(list(missing)),
            "excess": sorted(list(excess))
        }
    def evaluate_osaka_2025(self, p_val, locus_func_str):
        """
        Verifies if the locus y = g(x) satisfies f(alpha) - f(beta) = 4.
        p_val: a sample value for p to test.
        locus_func_str: the locus equation in string form, e.g., "x**3 - 3*x"
        """
        try:
            x, p, m = sp.symbols('x p m')
            f = x**3 + 3*p*x**2 + 3*m*x
            df = sp.diff(f, x)
            # Find roots of 3x^2 + 6px + 3m = 0
            roots = sp.solve(df, x)
            alpha, beta = roots[0], roots[1]
            # f(alpha) - f(beta) = 4
            diff_val = f.subs(x, alpha) - f.subs(x, beta)
            # Since alpha is max and beta is min, diff_val should be positive.
            # We want to solve diff_val = 4 for m.
            m_expr = sp.solve(diff_val - 4, m)[0] # Expected: p**2 - 1
            
            # Inflection point
            ddf = sp.diff(f, x, 2)
            inflection_x = sp.solve(ddf, x)[0] # Expected: -p
            inflection_y = f.subs({x: inflection_x, m: m_expr}) # Expected: -p**3 + 3*p
            
            # Check if (inflection_x, inflection_y) lies on y = g(x)
            test_x = sp.symbols('test_x')
            g_func = sp.sympify(locus_func_str)
            check = g_func.subs(sp.symbols('x'), inflection_x) - inflection_y
            
            return {
                "is_correct": sp.simplify(check) == 0,
                "expected_m_relation": str(sp.simplify(m_expr)),
                "expected_inflection_y": str(sp.simplify(inflection_y)),
                "inflection_x": str(inflection_x)
            }
        except Exception as e:
            return {"is_correct": False, "error": str(e)}

if __name__ == "__main__":
    v = ACSVerifier()
    gt = v.get_ground_truth_tit2022(20)
    print(f"Ground Truth: {gt}")
    test_ans = [1, 3]
    print(f"Evaluation of [1, 3]: {v.evaluate_answer(test_ans, gt)}")
