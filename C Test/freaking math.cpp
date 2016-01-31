#include <iostream>
#include <time.h>
#include <conio.h>

using namespace std;

int game(int level){
	int times,time1,time2,dem=0,gt1,gt2,kq,ran,kt;
	char nhap;
	srand(time(0));
	do
	{
		ran=rand()%2;
		gt1=1+rand()%20; gt2=1+rand()%20;
		if(ran==1){
			kq = gt1 + gt2;
			cout << gt1 << "+" << gt2 << "=" << kq << endl;
			time1 = time(0);
			fflush(stdin);
			nhap = getch();
			time2 = time(0);
			if(nhap == '1') kt=1;
			else break;
		}else{
			kq = gt1 + gt2 + rand()%7 - rand()%5;
			if(kq == gt1 +gt2) kq = kq - 1;
			cout << gt1 << "+" << gt2 << "=" << kq << endl;
			time1 = time(0);
			fflush(stdin);
			nhap=getch();
			time2 = time(0);
			if(nhap == '2') kt=1;
			else break;
		}
		times = difftime(time2,time1);
		if(times < level)
		dem++;
	}
	while(kt && times < level);
	cout << "Your Score = " << dem << endl;
	return dem;
}
int main(){
	MENU:
	int menu,menuChoi;
	cout << "====FREAKING MATH====" << endl;
	cout << "1.Play Game" << endl;
	cout << "2.Instruction" << endl;
	cout << "3.Exit" << endl;
	fflush(stdin);
	menu = getch();
	switch (menu){
		case '1':{
			MENUCHOI:
			system("cls");
			cout << "====FREAKING MATH====" << endl;
			cout << "====    LEVEL    ====" << endl;
			cout << "1.Easy (5s)" << endl;
			cout << "2.Normal (3s)" << endl;
			cout << "3.Hard (1s)" << endl;
			cout << "4.Practice (No Time Limit)" << endl;
			cout << "5.Back To Main Menu" << endl;
			fflush(stdin);
			menuChoi = getch();
			switch (menuChoi){
				case '1':{
					system("cls");
					cout << "====FREAKING MATH====" << endl;
					cout << "****  EASY MODE  ****" << endl;
					game(6);
					break;
				}		
				case '2':{
					system("cls");
					cout << "====FREAKING MATH====" << endl;
					cout << "**** NORMAL MODE ****" << endl;
					game(4);
					break;
				}
				case '3':{
					system("cls");
					cout << "====FREAKING MATH====" << endl;
					cout << "****  HARD MODE  ****" << endl;
					game(2);
					break;
				}
				case '4':{
					system("cls");
					cout << "====FREAKING MATH====" << endl;
					cout << "****PRACTICE MODE****" << endl;
					game(999999999);
					break;
				}
				case '5':{
					system("cls");
					goto MENU;
				}
				default:{
					system("cls");
					goto MENUCHOI;
					break;
				}
			}
			break;
     	}
 		case '2':{
 			system("cls");
 			cout << "====FREAKING MATH====" << endl;
	 		cout << "Press 1 If It's True, 2 If It's False" << endl;
	 		cout << "Press Any Key To Back ..." << endl;
		 	getch();
	 		system("cls");
		    goto MENU;
			break;
 		}
 		case '3':{
 			system("cls");
	 		exit(0);
			break;
	 	}
 	 	default:{
 	 		system("cls");
 	 		goto MENU;
 	 		break;
 	 	} 
    }
    cout << "Do You Want To Play Again ? (y,n)" << endl;
    fflush(stdin);
	if (getch() == 'y') {
		system("cls");
		goto MENU;
	}
	return 0;
}