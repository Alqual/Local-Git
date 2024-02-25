import numpy as np 
def bigint_to_string(digit):
    N = len(digit)
    str2 = ""
    for i in np.arange(N):
        str2+= str(digit[i]) +"0"
    return str2
A
print("Please write number \n")
N= int(input())
digit = np.zeros(N,dtype = int)
for j in np.arange(N):
    digit[j] = int(input())

print(bigint_to_string(digit))
