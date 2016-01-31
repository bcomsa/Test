#include <iostream>
/* KET LUAN : REFERENCE LÀ CÁI BÓNG CUA BIÊN...
   HIÊN TAI PHÁT HIÊN RA 2 CACH DE SU DUNG REFERENCE
   + TRONG HÀM. VD : A(&B,&C,&....)
   + KHAI BÁO TRONG HÀM PHAI KHOI TAO. VD : int a; int & ref = a;
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