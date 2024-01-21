#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> carry_and_fix(vector<int> digit) {
    int N = digit.size();
    for(int i = 0; i < N - 1; ++i) {
        // 繰り上がり処理 (K は繰り上がりの回数)
        if(digit[i] >= 10) {
            int K = digit[i] / 10;
            digit[i] -= K * 10;
            digit[i + 1] += K;
        }
        // 繰り下がり処理 (K は繰り下がりの回数)
        if(digit[i] < 0) {
            int K = (-digit[i] - 1) / 10 + 1;
            digit[i] += K * 10;
            digit[i + 1] -= K;
        }
    }
    // 一番上の桁が 10 以上なら、桁数を増やすことを繰り返す
    while(digit.back() >= 10) {
        int K = digit.back() / 10;
        digit.back() -= K * 10;
        digit.push_back(K);
    }
    // 1 桁の「0」以外なら、一番上の桁の 0 (リーディング・ゼロ) を消す
    while(digit.size() >= 2 && digit.back() == 0) {
        digit.pop_back();
    }
    return digit;
}


vector<int> addition(vector<int> digit_a, vector<int> digit_b) {
    int N = max(digit_a.size(), digit_b.size()); // a と b の大きい方
    vector<int> digit_ans(N); // 長さ N の配列 digit_ans を作る
    for(int i = 0; i < N; ++i) {
        digit_ans[i] = (i < digit_a.size() ? digit_a[i] : 0) + (i < digit_b.size() ? digit_b[i] : 0);
        // digit_ans[i] を digit_a[i] + digit_b[i] にする (範囲外の場合は 0)
    }
    return carry_and_fix(digit_ans); // 2-4 節「繰り上がり計算」の関数です
}

int main() {
    int N1,N2;
    cout<<"Please write sizes of Both\n"<< "N1 = \n";
    cin >> N1;
    cout<<"N2 = \n";
    cin >> N2;
    vector<int> digit_a(N1);
    vector<int> digit_b(N2);
    cout<<"Please write vector \n" << "Vector_a = \n";
    for (size_t j=0; j<N1;j++){
        cin>> digit_a[j];
    }

    cout<<"Please write vector \n" << "Vector_b = \n";
    for (size_t j=0; j<N2;j++){
        cin>> digit_b[j];
    }
    cout<<"Vector_a = ";
    for_each(
        digit_a.begin(), digit_a.end(), [](auto x)
        { std::cout << x << ", "; });
     cout<<"\n"<<"Vector_b = ";
    for_each(
        digit_b.begin(), digit_b.end(), [](auto y)
       { std::cout << y<< ", "; });

    cout<<"\n"<<"Vector_a + Vector_b = ";


    vector<int> addition_ =  addition(digit_a,digit_b) ;
    for (size_t k=0; k<addition_.size();++k) {
        if (k<=addition_.size()-2) {
            cout << addition_[k]<<",";
        } else {
        cout << addition_[k];
        }
        }
}
