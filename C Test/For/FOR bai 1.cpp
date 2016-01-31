#include<stdio.h>

int main(void)
{
	int i,n,gt=1;
	printf("tinh n!,nhap n\n",n);
	scanf("%d",&n);
	for(i=1;i<=n;++i)
	{
		gt*=i;	
	}
	printf("n!=%d",gt);
}