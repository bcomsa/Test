#include <stdio.h>
#include <conio.h>
#include <string.h>

int dec(char chuoi[5000],int j)//tuong tu encrypt
{
	int i,t=0;
	printf("Nhap Vao Thong Diep (nhap lien tuc den khi nao het thong diep moi an Enter)\n");
	fflush(stdin);
	gets(chuoi);
	printf("Nhap Vao Key Giai Ma\n");
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
	int key;
	dec(day,key);
	getch();
}
