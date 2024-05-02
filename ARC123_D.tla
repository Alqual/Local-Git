Get A = {A1,..,AN} in integer

def B = {B1,..,BN} in integer
def C = {C1,..,CN} in integer
B,C meets the following conditions:
1. Ai = Bi + Ci
2. Bi <= B[i+1] , 1,2,..,N-1
3. Ci >= C[i+1], 1,2,..,N-1

Find the minimum value of sum(abs(B) + abs(C))

Greedy algorithm:

condition of B and C:
Bi >= Bi-1
Ci <= Ci-1
Ai = Bi + Ci
decide the minimum value of abs(Bi) + abs(Ci) for each i

'''
