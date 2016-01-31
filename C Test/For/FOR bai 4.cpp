#include<stdio.h>

int main()
{
	int day[20],i,n,max,min,vtmax=0,vtmin=0;
	printf("ban muon nhap bao nhieu so (nho hon 20)");
	scanf("%d",&n);
	for(i=0;i<n;++i)
	{
		printf("\nSo %d = ",i);
		scanf("%d",&day[i]);
	}
	max=day[0];
	min=day[0];
	for(i=0;i<n;++i)
	{
		if(max<day[i])
		{
			max=day[i];
			vtmax=i;
		}
		if(min>day[i])
		{
			min=day[i];
			vtmin=i;
		}
	}
	printf("\nmax = %d o vi tri thu %d, min = %d o vi tri thu %d\n",max,vtmax,min,vtmin);
	
}