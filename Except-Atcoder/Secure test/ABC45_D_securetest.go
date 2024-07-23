package main

// https://atcoder.jp/contests/abc045/tasks/arc061_b
// Coding review Comments
// 1. pacakge name should not be main. main is global. it should be dedicated by the repository name.
// 2. func main()はコードの行頭に書くべきです。main関数の後に参照する他の関数を書くと、読みやすいです。
// 3. A,B,Cなどの変数名は、コードの意味を理解しやすくするために、適切な名前に変更することをお勧めします。

// 3-1. 変数名の付け方は、Goのベストプラクティションに従ってください。https://golang.org/doc/effective_go.html#names
// 3-1-1.Mixedcapsで命名すること
// 3-1-2.他パッケージから参照できる変数は最初の文字を大文字（MaxLength）、参照できない変数は小文字から始める（maxLength）
// 3-1-3.頭字語は大文字または小文字を統一 例: URLかurlなど。
// 3-1-4.エラー型の変数名にはErrorを接尾語として付ける。例: MarshalerError
// 3-1-5. ローカル変数はスコープが限定されているため、短い名前が好まれる。例: req、i

// 3-2. インターフェースの命名もGOのベストプラクティスに従ってください。https://golang.org/doc/effective_go.html#interface-names
// 3-2-1. 1つのメソッドのみを持つインタフェースには、-er接尾語を付けることがある。例: Reader、Stringer。
// 3-2-2. 数のメソッドを持つインタフェースはその目的を反映した名前を選ぶ。例: net.Conn。

// 3-3. レシーバーの命名もGoのベストプラクティスに従ってください。https://golang.org/doc/effective_go.html#mixed-caps
// 3-3-1. レシーバー名は型を反映した短い名前を使用する。例: r（Requestの場合）、re（Regexpの場合）
// 3-3-2. 一貫性を持たせるために、同一型に対して同じレシーバー名を用いる

import (
	"bufio"
	"fmt"
	"os"

	"code.google.com/p/go.exp/utf8string"
)

func main() { //main関数が長すぎるので、関数を分割することをお勧めします。

	// 入力処理をmainで書くのは本当に適切???関数化させすぎるのもよくない???
	//何となく拡張性が無いように感じるのは気のせい??
	//現在制約条件: 25MB, X~10**6, 3×3格子, 2秒
	//拡張条件: 25GB, X~10**20, 1000*1000格子, 60秒

	// 入力用の行を修正
	//var C map[key]bool = map[key]bool{} //Cだと何の変数かわからない
	var Lattice_blackmass_in map[loc]bool = map[loc]bool{} //黒マスを含む3×3格子の座標
	//var chk2 int //これも不要
	Count_lattice_blackmass := make([]int, 10) //黒マスを各0-9個含む3×3格子の数
	//ans := make([]int, 10) //cout_blkの方が良い??
	//Count_33lattice_filled_blk すごく冗長な名称になってしまう。配列をもう一用意するなどした方が良い??
	//33latticeの変数ぐるーぷ(class)などを作って管理した方が分かりやすい?? structure化？？
	//var visited map[key]bool = map[key]bool{}
	/////////////

	// 入力の行を修正
	WorkScanner.Buffer(Buffermem, 300000) //test　これは何??
	Input_board_str := Newline()          //幾つかのマス目からなるBoardの構造と入力回数を[Row数,Col数,Task数]で獲得
	// addition
	for tasknum := 0; tasknum < Input_board_str[2]; tasknum++ { //Task数だけ繰り返し入力処理を行う
		Input_blackmass_loc := Newline() //Board上の黒マス位置を[Row,Col]で獲得
		//Newlineではわかりにくくないか??
		for row := Input_blackmass_loc[0] - 1; row <= Input_blackmass_loc[0]+1; row++ { //1000*1000格子だと配列が準備できない??10**6行配列はメモリ消費が激しくて重すぎる
			for col := Input_blackmass_loc[1] - 1; col <= Input_blackmass_loc[1]+1; col++ {
				Lattice_blackmass_in[loc{row, col}] = true //ここで3×3格子マス上すべてをtrueとすると、下のvisitedの処理が不要になるし、誤解が少ない。
			}
		}
	}
	/////////////

	for locs := range Lattice_blackmass_in { //黒マスを含む3×3格子の中心座標について処理

		//このアルゴリズムは初見の人にわかりやすいか???わかりやすくする必要がある??
		//技術力の高い集団ならば、このアルゴリズムは問題ないかもしれませんが、初心者には理解しにくいかもしれない。
		//セキュリティ面、脆弱性とかも考慮に含めると、高速化処理が良いとも限らない。

		//暗示的な取り出し方なので、何かわかるよな仕組みが欲しい。

		//for i := keys.x - 1; i <= keys.x+1; i++ {
		//	for j := keys.y - 1; j <= keys.y+1; j++ {
		//		if !visited[key{i, j}] { //重複があることが前提なのでvisitedを使っているが、重複の無いように作り変えれば、visitedは不要になる。
		//			visited[key{i, j}] = true //key{i,j}他、入力値が正しく入力されたことが確認されていない。
		//		} else {
		//			continue
		//		}
		//依存関係が若干わかりにくい??

		var Count_blackmass_eachlattice int //格子内黒マス計量用ダミー変数
		//var chk int //不要な変数
		for row := locs.x - 1; row <= locs.x+1; row++ {
			for col := locs.y - 1; col <= locs.y+1; col++ {
				if Lattice_blackmass_in[loc{row, col}] {
					Count_blackmass_eachlattice++
				}
				//if row >= 1 && row <= Input_Lattice_str[0] && col >= 1 && col <= Input_Lattice_str[1] {
				//		chk++ //これは不要では??
				//	}
			}
		}
		if locs.x-1 >= 1 && locs.x+1 <= Input_board_str[0] && locs.y-1 >= 1 && locs.y+1 <= Input_board_str[1] { //これで良いのでは??
			Count_lattice_blackmass[Count_blackmass_eachlattice]++
			//		chk2++ //これも不要では??
		}
		//chk = 0
		Count_blackmass_eachlattice = 0
		//}
		//}
	}
	//Count_lattice_blackmass[0] += (Input_Lattice_str[0]-2)*(Input_Lattice_str[1]-2) - chk2 //これも不要
	for countnum := 0; countnum < 10; countnum++ { //塗りつぶされたマスの数が0~9個あるような、3×3格子の数を昇順出力
		fmt.Println(Count_lattice_blackmass[countnum])
	}
}
// test coding at Jul24
var WorkScanner = bufio.NewScanner(os.Stdin)
var Buffermem = make([]byte, 10000)

func Newline() []int {
	WorkScanner.Scan() // validationが必要, white listingは除外 (標準入力で,このプログラムを実行できた場合なので)
	//sc.Scan()は改行はされるが、それを引っ張る必要がある
	//if byte(sc) == //

	/////XSS 対策 (今回はterminal上入力なので該当せず。/./で追加する)////
	//if strings.Contains(sc.Text(), "<") || strings.Contains(sc.Text(), ">") {
	//	return nil
	//}

	//SQL injection対策(今回はterminal上入力なので該当せず。)
	//ctx := context.Background()
	//customerId := r.URL.Query().Get("id")
	//query := "SELECT number, expireDate, cvv FROM creditcards WHERE customerId = ?"
	//stmt, _ := db.QueryContext(ctx, query, customerId)
	//	return nila

	// validation check flow /////
	asci := utf8string.NewString(WorkScanner.Text()) //ascii only is allowed, vali1
	if asci.IsASCII() == false {
		return nil
	}

	if len(WorkScanner.Text()) == 0 || len(WorkScanner.Text()) > 100 { //boundery check added,vali2
		return nil
	}
	val := WorkScanner.Text() //ret -> val

	/////////////////////////////

	var ret []int //reti -> ret
	for _, s := range val {
		if s < 48 || s > 57 { //numeric type check, vali3
			return nil
		}
		valint := int(s) //res -> valint
		ret = append(ret, valint)
	}
	return ret
}

type loc struct {
	x, y int //parameter名を工夫すべき
}
