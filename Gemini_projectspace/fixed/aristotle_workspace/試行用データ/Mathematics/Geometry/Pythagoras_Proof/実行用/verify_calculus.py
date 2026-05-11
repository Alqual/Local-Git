
import sympy
from sympy import symbols, Function, diff, Eq, solve

def verify_calculus_step():
    x, a = symbols('x a', real=True)
    y = Function('y')(x)
    
    # Hypothesis: (y^2)' = 2x
    # We want to check if y^2 = x^2 + a^2 satisfies this.
    
    # 1. Define candidate solution
    candidate_y_sq = x**2 + a**2
    
    # 2. Differentiate candidate with respect to x
    derivative_lhs = diff(candidate_y_sq, x)
    
    # 3. Check if it equals 2x
    print(f"Candidate y^2: {candidate_y_sq}")
    print(f"Derivative of y^2: {derivative_lhs}")
    
    if derivative_lhs == 2*x:
        print("VERIFICATION SUCCESS: The derivative of x^2 + a^2 is indeed 2x.")
        print("This confirms the hypothesis (y^2)' = 2x is consistent with Pythagoras.")
    else:
        print("VERIFICATION FAILED.")

    # 4. Reverse direction: Solve differential equation
    # (y^2)' = 2x  =>  2*y*y' = 2x  => y*y' = x
    # This is separable? 
    # Let u = y^2. Then u' = 2x.
    
    u = Function('u')(x)
    diff_eq = Eq(diff(u, x), 2*x)
    
    sol = sympy.dsolve(diff_eq, u)
    print(f"General solution for (y^2)' = 2x: {sol}")
    
    # Apply initial condition y(0) = a => u(0) = a^2
    # sol is likely u(x) = x^2 + C1
    
    # We can't easily parse 'sol' automatically in a robust way without more code, 
    # but the print output will show us.
    
if __name__ == "__main__":
    verify_calculus_step()
