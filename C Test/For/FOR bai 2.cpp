#include<stdio.h>

int main(void)
{
	int i,n,gt=1;
	float tong=0;
	printf("Bai 2,nhap n\n",n);
	scanf("%d",&n);
	for(i=1;i<=n;++i)
	{
		gt*=i;
		tong+=(float)1/gt;	
	}
	printf("kq=%f",tong);
}