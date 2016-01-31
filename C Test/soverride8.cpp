#include<stdio.h>
#include<conio.h>
#include<math.h>
int main(){
	int a,ab,cd;
	float od,oa,ob,bd;
	scanf("%d%d%d",&a,&ab,&cd);
	od=cd/2;
	oa=sqrt(a*a-od*od);
	ob=ab-oa;
	bd=sqrt(ob*ob+od*od);
	printf("%f",bd);
}