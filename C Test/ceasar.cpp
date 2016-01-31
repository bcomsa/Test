#include <stdio.h>
#include <conio.h>
#include <string.h>

int enc(char chuoi[5000],int j)// j la key
{
	int i,t=0;
	printf("nhap chuoi ban muon encrypt\n");
	fflush(stdin);
    gets(chuoi);
	printf("nhap key ban muon encrypt\n");
	scanf("%d",&j);
	while(1)// kiem tra vi tri ket thuc chuoi
	{
		if(chuoi[t]=='\0')
		break;
		t++;
	}
	for(i=0;i<t;i++)
	{	
		if (64<chuoi[i]&&chuoi[i]<91)// dieu kien de z quay ve a b c blablabla
		{
			if	(chuoi[i]+j<=90)
			chuoi[i]=chuoi[i]+j;
			else
			chuoi[i]=64+(chuoi[i]+j)%90;
		}
		else if(96<chuoi[i]&&chuoi[i]<123)//dieu kien de Z quay ve A B C blablabla
			{	
				if(chuoi[i]+j<=122)
				chuoi[i]=chuoi[i]+j;
				else
				chuoi[i]=96+(chuoi[i]+j)%122;
			}
	}
	printf("%s\n",chuoi);
}
int dec(char chuoi[5000],int j)//tuong tu encrypt
{
	int i,t=0;
	printf("nhap chuoi ban muon decrypt\n");
	fflush(stdin);
    gets(chuoi);
	printf("nhap key ban muon decrypt\n");
	scanf("%d",&j);
	while(1)
	{
		if(chuoi[t]=='\0')
		break;
		t++;
	}
	for(i=0;i<t;i++)
	{	
		if (64<chuoi[i]&&chuoi[i]<91)// dieu kien de z quay ve a b c blablabla
		{
			if	(chuoi[i]-j>=65)
			chuoi[i]=chuoi[i]-j;
			else
			chuoi[i]=90-64%(chuoi[i]-j);
		}
		else if(96<chuoi[i]&&chuoi[i]<123)//dieu kien de Z quay ve A B C blablabla
			{	
				if(chuoi[i]-j>=97)
				chuoi[i]=chuoi[i]-j;
				else
				chuoi[i]=122-96%(chuoi[i]-j);
			}
	}
	printf("%s\n",chuoi);
}
int main(void)
{
	char day[5000];
	int choose,key;
	printf("ban muon encrypt hay decrypt(enc=1,dec=2)\n");
	scanf("%d",&choose); 
	switch (choose)
	{
		case 1:
		enc(day,key);
		break;
		case 2:
		dec(day,key);
		break;
		default:
		break;
	}
	getch();
}
