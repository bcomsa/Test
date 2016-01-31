#include<stdio.h>

int main()
{
	int ithang,inam,ngay[13];
	printf("moi ban nhap thang va nam\n");
	scanf("%d %d",&ithang,&inam);
	printf("thang %d nam %d phai khong =]]\n",ithang,inam);
	ngay[1]=ngay[3]=ngay[5]=ngay[7]=ngay[8]=ngay[10]=ngay[12]=31;
	ngay[4]=ngay[6]=ngay[9]=ngay[11]=30;
	if(0==inam%4)
		29==ngay[2];
	else
		ngay[2]=28;
	printf("thang %d nam %d co %d ngay\n",ithang,inam,ngay[ithang]);
}