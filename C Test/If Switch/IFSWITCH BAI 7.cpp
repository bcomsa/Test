#include<stdio.h>
#include<conio.h>

int main()
{
	int i,ithang,inam,ingay,ngay[13],isongay=0;
	printf("moi ban nhap ngay, thang va nam\n");
	scanf("%d %d %d",&ingay,&ithang,&inam);
	printf("ngay %d thang %d nam %d phai khong =]]\n",ingay,ithang,inam);
	ngay[1]=ngay[3]=ngay[5]=ngay[7]=ngay[8]=ngay[10]=ngay[12]=31;
	ngay[4]=ngay[6]=ngay[9]=ngay[11]=30;
	if(0==inam%4)
		ngay[2]=29;
	else
		ngay[2]=28;
	for(i=1;i<ithang;++i)
	{
		isongay+=ngay[i];
	}
	isongay+=ingay;
	printf("ngay %d/%d/%d la ngay thu %d\n",ingay,ithang,inam,isongay);
	getch();
}
