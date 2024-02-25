#include <vector>
#include <string>
#include <iostream>
using namespace std;

string bigint_to_string(vector<int> digit) {
    int N = digit.size(); // N = (配列 digit の長さ)
    string str = "";
    for(int i = N - 1; i >= 0; --i) {
        str += digit[i] + '0';
    }
    return str;
}


int main() {
    cout<<"Please write number\n";
    int N;
    cin >> N;
    vector<int> digit(N);
    for (size_t i=0; i < N ; i++) {
    cin >> digit[i];
    }
    string str =  bigint_to_string(digit) ;
    for (size_t i=0; i<str.size();++i) {
        cout << str[i]<< endl;
        }
        }
