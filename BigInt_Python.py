import numpy as np
def bigint_to_string(S):
    N = len(S)
    digit = np.zeros(N, dtype = int)
    for i in np.arange(N):
        digit[i] = S[N-i-1].replace("0","")
    return digit

S= input("Please write number\n")
digit = bigint_to_string(S)
N = len(S)
for j in np.arange(N):
    print(digit[j])