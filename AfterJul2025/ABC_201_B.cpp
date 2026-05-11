#include <iostream>
#include <vector>
using namespace std;

int main() {
    long N,T;
    string S;
    vector<string> A(2);
    vector<long> B(2);
    cin >> N;
    for (int i=0; i<N; i++) {
        cin >> S >>T ;
        if (i == 0) {
            A[0] = S;
            B[0] = T;
        } else if (i == 1) {
            if (T > B[0]) {
                A[1] = A[0];
                B[1] = B[0];
                A[0] = S;
                B[0] = T;
            } else {
            A[1] = S;
            B[1] = T;
        }
    } else {
            if (T > B[0]) {
                A[1] = A[0];
                B[1] = B[0];
                A[0] = S;
                B[0] = T;
            } else if (T > B[1]) {
                A[1] = S;
                B[1] = T;
            } 
            }
        }
std::cout << A[1] << std::endl;
    }