import math

def gcd(a, b):
    return math.gcd(a, b)

def solve():
    found_gcds = set()
    limit = 40  # 探索範囲
    
    for a in range(1, limit):
        for b in range(1, limit):
            for c in range(1, limit):
                if math.gcd(a, math.gcd(b, c)) == 1:
                    s1 = a + b + c
                    s2 = a**2 + b**2 + c**2
                    s3 = a**3 + b**3 + c**3
                    
                    g = math.gcd(s1, math.gcd(s2, s3))
                    found_gcds.add(g)
                    
    print(f"Unique GCD values found: {sorted(list(found_gcds))}")

if __name__ == "__main__":
    solve()
