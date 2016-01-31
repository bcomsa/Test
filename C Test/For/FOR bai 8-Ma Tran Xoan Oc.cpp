#include <conio.h>
#include <stdio.h>

int main()
{
	int a[100][100];
    int i,value=1,hangTren=0,hangDuoi,cotTrai=0,cotPhai,row,col;
    printf("nhap dong cot\n");
	scanf("%d %d",&row,&col);
	hangDuoi=row-1;
	cotPhai=col-1;
	while(value<=row*col)
		{
		  for(i=cotTrai;(i<=cotPhai);i++)
			 a[hangTren][i]=value++;

		  hangTren++;

		  for(i=hangTren;(i<=hangDuoi);i++)
			 a[i][cotPhai]=value++;
		  cotPhai--;

		  for(i=cotPhai;(i>=cotTrai);i--)
			 a[hangDuoi][i]=value++;
		  hangDuoi--;

		  for(i=hangDuoi;(i>=hangTren);i--)
			 a[i][cotTrai]=value++;
		  cotTrai++;
		}
	for(int i=0;i<row;i++)
		{
		  for(int j=0;j<col;j++)
			 printf("%3.d ",a[i][j]);
		  printf("\n");
		}
	getch();
}
