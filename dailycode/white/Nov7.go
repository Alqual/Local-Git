//入力した文字列Tとn組の文字列S1,S2,...,Snが与えられます。各Siについて、SiがTに含まれるかを出力してください。
//例えば、T="ababab"、S1="ab"、S2="c"、S3="ab"の場合、S1とS3はTに含まれますが、S2は含まれません。
//Tの部分列は連続している必要はありません。例えば、T="caccbcb"、S="ab"の場合、SiはTに含まれます。
//出力は,含まれるSiの組の個数を出力してください。
//例えば、T="ababab"、S1="ab"、S2="c"、S3="ab"の場合、S1とS3はTに含まれますが、S2は含まれませんので、出力は2となります。
//T
//n
//Si

package main

func settest(T string, n int, S []string) int {
	ans, j := 0, 0
	for i := 0; i < n; i++ {
		for j < len(S[i]) {
			if T[j] == S[i][0] {
				j++
			}
			ans += max(0, j-len(S[i])+1)
		}
	}
	return ans
}
