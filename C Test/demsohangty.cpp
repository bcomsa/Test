#include"stdio.h"
#include"string.h"
#include"conio.h"
char *xau[10]={"không","m?t","hai","ba","b?n","nam","sáu","b?y","tám","chín"};
void docso(int *s,int n,int kt)
{
	if (s[n]!=0) printf(" %s  tram ",xau[s[n]]);
		else if (kt==0) printf(" không  tram ");
	if (s[n+1]==0) 
	{
		if (s[n+2]!=0)
		{
			if (s[n+1]==0 && kt==1) printf("%s",xau[s[n+2]]);
				else printf(" l?  %s ",xau[s[n+2]]);
		}
	}
	else if (s[n+1]==1) 
	{
		if (s[n+2]==0) printf(" mu?i ");
			else printf(" mu?i  %s ",xau[s[n+2]]);
	}
	else if (s[n+2]==0) printf (" %s  muoi ",xau[s[n+1]]);
		else if (s[n+2]==1) printf (" %s  muoi  m?t ",xau[s[n+1]]);
			else printf(" %s  muoi  %s ",xau[s[n+1]],xau[s[n+2]]);
	return;
}

int main()
{
	long x;
	int i=0,s[12],tam[12],landau=1;
	nhaplai:
	printf("nh?p s? t? nhiên bé hon 1000 t?:");
	scanf("%ld",&x);
	if (x>999999999||x<0) 
		{
		printf("sai - nhap lai\n");
		goto nhaplai;
		}
	do 
	{
	tam[i++]=x%10;
	x/=10;
	}
	while (x>0);
	while (i<12)
		tam[i++]=0;
	for (i=0;i<12;i++)
		s[i]=tam[11-i];
	i=0;
	if (s[i]!=0||s[i+1]!=0||s[i+2]!=0)
	{
		docso(s,i,landau);
		printf(" t? ");
		landau=0;
	}
	i+=3;
	if (s[i]!=0||s[i+1]!=0||s[i+2]!=0)
	{
		docso(s,i,landau);
		printf(" tri?u ");
		landau=0;
	}
	i+=3;
	if (s[i]!=0||s[i+1]!=0||s[i+2]!=0)
	{
		docso(s,i,landau);
		printf(" nghìn ");
		landau=0;
	}
	i+=3;
	docso(s,i,landau);
	printf("\n");
	getch();
	return 0;
}
