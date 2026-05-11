#include <iostream>
#include <vector>
using namespace std;

int main() {
    long TOTALS;
    string S;
    vector<string> CNST(3);
    CNST[0] = "o";
    CNST[1] = "x";
    CNST[2] = "?";
    vector<long> SUMS(3);
    cin >> S;
    for (int i = 0; i < 10; i++) {
        if (S.at(i) == CNST[0].at(0)) {
            SUMS[0]++;
        } else if (S.at(i) == CNST[1].at(0)) {
            SUMS[1]++;
        } else if (S.at(i) == CNST[2].at(0)) {
            SUMS[2]++;
        }
    }
    for (int i = 1; i <= SUMS[0]; i++) {
        TOTALS += SUMS[i];
    }
}