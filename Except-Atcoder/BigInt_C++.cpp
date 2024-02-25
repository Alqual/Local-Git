#include <vector>
#include <string>
#include <iostream>
using namespace std;
vector<int> string_to_bigint(string S) {
    int N = S.size(); // N = (文字列 S の長さ)
    vector<int> digit(N);
    for(int i = 0; i < N; ++i) {
        digit[i] = S[N - i - 1] - '0'; // 10^i の位の数
    }
    return digit;
}

int main() {
    cout<<"Please write number\n";
    string str;
    cin >> str;
    vector<int> int_vect =  string_to_bigint(str) ;
    for (size_t i=0; i<int_vect.size();++i) {
        cout << int_vect[i]<< endl;
        }
        }

