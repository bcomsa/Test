#include <iostream.h>
#include <stdlib.h>
#include <new.h>

 void MyHandler();

 unsigned long I = 0; 9;
 void main()
 {
 int *A;
 _new_handler = MyHandler;
 for( ; ; ++I)
 A = new int;

 }

 void MyHandler()
 {
 cout<<"Lan cap phat thu "<<I<<endl;
 cout<<"Khong con du bo nho!"<<endl;
 exit(1);
 }
