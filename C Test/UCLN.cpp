#include <stdio.h>

int main(){
	int a,b,temp1,temp2,uc,bc,tich;
	printf("nhap 2 so a, b . Tim uoc chung lon nhat\n");
	scanf("%d%d",&a,&b);
	tich = a*b;
	temp1 = a; temp2 = b;
	while(a != b){
        if(a>b)
        a-=b;
        else
        b-=a;
	}
	uc=a=b;
	printf("UCLN cua a va b = %d\n",a);
	bc = tich/a; 
	printf("BCNN cua a va b = %d\n",bc);
	if (uc==1) printf("%d va %d la 2 so nguyen to cung nhau\n",temp1,temp2); 
}