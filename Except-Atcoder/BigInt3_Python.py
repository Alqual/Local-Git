import numpy as np 

def carry_and_fix(digit):
	N = len(digit)
	digit2 = np.zeros(N,dtype=int)
	digit2 = digit
	K = int(0)

	for i in np.arange(N):
		# 繰り上がり処理 (K は繰り上がりの回数)
		if digit[i] >= 10:
			K = digit[i] / 10
			digit2[i] -= K * 10
			digit2[i+1] += K
		# 繰り下がり処理 (K は繰り下がりの回数)
		if digit[i] < 0:
			K = (-digit[i]-1)/10 + 1
			digit2[i] += K * 10
			digit2[i+1] -= K
		
	
	# 一番上の桁が 10 以上なら、桁数を増やすことを繰り返す
	while digit2[len(digit2)-1] >= 10:
		K = digit2[len(digit2)-1] / 10
		digit2[len(digit2)-1] -= K * 10
		digit2 = np.append(digit2, K)
	
	# 1 桁の「0」以外なら、一番上の桁の 0 (リーディング・ゼロ) を消す
	while (len(digit2) >= 2) and (digit2[len(digit2)-1] == 0):
		digit2 = digit2[:len(digit2)-2]
	
	return digit2


def addition(digit_a, digit_b):
	N = np.max([len(digit_a), len(digit_b)]) # a と b の大きい方
	digit_ans = np.zeros(N,dtype=int)      # 長さ N の配列 digit_ans を作る
	for i in np.arange(N):
		if i < len(digit_a):
			digit_ans[i] = digit_a[i]
		else:
			digit_ans[i] = 0
		if i < len(digit_b):
			digit_ans[i] += digit_b[i]
		
		# digit_ans[i] を digit_a[i] + digit_b[i] にする (範囲外の場合は 0)

	return carry_and_fix(digit_ans)




print("Please write number \n")
N1= int(input("N1 = ") )
N2 = int(input("N2 = " ) )
digit_a = np.zeros(N1,dtype = int)
digit_b = np.zeros(N2,dtype = int)
digit_a = list(map(int,input("digit_a = ").split() ) )
digit_b = list(map(int,input("digit_b = ").split()) )
print("digit_a + digit_b = ", addition(digit_a, digit_b))
