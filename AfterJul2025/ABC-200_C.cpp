#include <iostream>
#include <vector>
using namespace std;

int main() {
    long N,M;
    long L,DL;
    M = 200;
    cin >> N;
    vector<long> A(N), B(M);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        B[A[i] % M]++;
        /*cout << A[i] % M<< endl;*/
    }
    for (int i = 0; i < M; i++) {
            if (B[i]>=2){
            DL= (B[i] * (B[i]-1))/2;
            L+=DL;
            }
    }
        std::cout << L << std::endl;
    }