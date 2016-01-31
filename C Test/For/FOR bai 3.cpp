#include<stdio.h>

int main()
{
	int x[20],y[20],i,j,n;
	printf("moi ban nhap so diem tren mat phang(nho hon 20)\n");
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
		printf("moi ban nhap diem thu i\n");
		printf("x[%d]= ",i);
		scanf("%d",x+i);
		printf("y[%d]= ",i);
		scanf("%d",y+i);
		if(x[i]<0&&y[i]<0)
		{
			
		}
	}
	printf("\nso diem thuoc mp thu 3");
	for(i=0;i<n;++i)
	{	if((x[i]<0) && (y[i]<0))
			printf("\nx[%d]= (%d,%d)",i,x[i],y[i]);
	}
}