#include<stdio.h>
#include<conio.h>

int main()
{
	int i,phanngan,phantram,phanchuc,phandonvi;
	printf("xin moi nhap chu so nho hon 1000\n"); // thuc ra la 10000
	scanf("%d",&i);
	phanngan=i%1000;
	phantram=phanngan%100;
	phandonvi=phantram%10;
	phanchuc=phantram/10;
	phantram=phanngan/100;
	phanngan=i/1000;
	switch(phanngan)
	{
		case 0:
		break;
		case 1:
		printf("Mot nghin ");
		break;
		case 2:
		printf("Hai nghin ");
		break;
		case 3:
		printf("Ba nghin ");
		break;
		case 4:
		printf("Bon nghin ");
		break;
		case 5:
		printf("Nam nghin ");
		break;
		case 6:
		printf("Sau nghin ");
		break;
		case 7:
		printf("Bay nghin ");
		break;
		case 8:
		printf("Tam nghin ");
		break;
		case 9:
		printf("Chin nghin ");
		break;
		default:
		break;
	}
	switch(phantram)
	{
		case 0:
		if(phanngan==0)
		break;
		else
		if(phanngan==0&&phandonvi==0)
		break;
		else
		printf("khong tram ");
		break;
		case 1:
		printf("mot tram ");
		break;
		case 2:
		printf("hai tram ");
		break;
		case 3:
		printf("ba tram ");
		break;
		case 4:
		printf("bon tram ");
		break;
		case 5:
		printf("nam tram ");
		break;
		case 6:
		printf("sau tram ");
		break;
		case 7:
		printf("bay tram ");
		break;
		case 8:
		printf("tam tram ");
		break;
		case 9:
		printf("chin tram ");
		break;
		default:
		break;
	}
	switch(phanchuc)
	{
		case 0:
		if(phantram==0&&phanngan==0)
		break;
		else
		if(phandonvi==0)
		break;
		else
		printf("linh ");
		break;
		case 1:
		printf("muoi ");
		break;
		case 2:
		printf("hai muoi ");
		break;
		case 3:
		printf("ba muoi ");
		break;
		case 4:
		printf("bon muoi ");
		break;
		case 5:
		printf("nam muoi ");
		break;
		case 6:
		printf("sau muoi ");
		break;
		case 7:
		printf("bay muoi ");
		break;
		case 8:
		printf("tam muoi ");
		break;
		case 9:
		printf("chin muoi ");
		break;
		default:
		break;
	}
	switch(phandonvi)
	{
		case 0:
		break;
		case 1:
		printf("mot");
		break;
		case 2:
		printf("hai");
		break;
		case 3:
		printf("ba");
		break;
		case 4:
		printf("bon");
		break;
		case 5:
		printf("nam");
		break;
		case 6:
		printf("sau");
		break;
		case 7:
		printf("bay");
		break;
		case 8:
		printf("tam");
		break;
		case 9:
		printf("chin");
		break;
		default:
		break;
	}
	printf("\n");
	getch();
}
