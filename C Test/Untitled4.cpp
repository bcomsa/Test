#include<stdio.h>
int main(void)
{
	int i;
	int ascii[255];
	char day[255];
	for (i=0;i<255;i++)
	{
		ascii[i]=i*i*(i+1);
	printf("%d %d\n",i,ascii[i]);
	}
	
}