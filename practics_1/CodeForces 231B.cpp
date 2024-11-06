// Write a program that prints all numbers from 1 to 50, but for multiples of 5, print "Five" instead of the number.

#include <bits/stdc++.h>
using namespace std;
int main(){
    int num;
    cout << "Enter Your Nums: ";
    cin >> num;
    
    if (num %5 ==0)
        cout<<num<< " is a multiple of 5\n";
    else
        cout << num << " is not multiple of 5\n";
}