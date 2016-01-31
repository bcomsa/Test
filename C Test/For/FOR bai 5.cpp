#include<stdio.h>
#include<conio.h>

int main()
{
	int day[20],i,n,dd=0,da=0;
    float tba=0,tbd=0,tb=0;
	printf("ban muon nhap bao nhieu so (nho hon 20)\n");
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
		printf("\nSo %d = ",i);
		scanf("%d",&day[i]);
	 	if(day[i]>=0)
	 	{
	 		tbd+=day[i];
	 		dd++;
	 	}
	 	else
	 	{
	 		tba+=day[i];
	 		da++;
	 	}
	 	tb+=day[i];	
	}
	printf("\nco %d so am, co %d so duong, trung binh cong so am la %f, trung binh cong so duong la %f, trung binh cong day so la %f\n",da,dd,(float)tba/da,(float)tbd/dd,(float)tb/n);
    getch();	
}
