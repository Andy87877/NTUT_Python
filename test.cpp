#include <bits/stdc++.h>
using namespace std;

int A[4] = {1,2,3,4};

void change(){
    A[0] = 87;
}

int main(){
    for (int i = 0; i < 4; i++){
        cout << A[i] << " ";
    }
    cout << "\n";

    for (int i = 0; i < 4; i++){
        cout << A[i] << " ";
    }
    cout << "\n";
}