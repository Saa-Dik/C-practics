// Write a program that checks if a number is odd or even. If the number is even, print "Even"; otherwise, print "Odd."

#include <bits/stdc++.h>
using namespace std;

int main(){
	int num; 
	cout << "Enter the nums: ";
	cin >> num;

	if(num % 2 == 0) 
	    cout << "Even\n";
	else 
	    cout << "Odd\n";
}