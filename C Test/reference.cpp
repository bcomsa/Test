#include <iostream>
/* KET LUAN : REFERENCE L� C�I B�NG CUA BI�N...
   HI�N TAI PH�T HI�N RA 2 CACH DE SU DUNG REFERENCE
   + TRONG H�M. VD : A(&B,&C,&....)
   + KHAI B�O TRONG H�M PHAI KHOI TAO. VD : int a; int & ref = a;
*/
using namespace std;
int main(){
	int a=2;
	int &ref = a;
	ref = 3 ; a = 2;
	cout << "ref = " << ref << endl << "a = " << a << endl;
	a = 10;
	cout << "ref = " << ref << endl << "a = " << a << endl;
	ref = 100;
	cout << "ref = " << ref << endl << "a = " << a << endl;
	return 0;
}