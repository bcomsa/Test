#include <stdio.h>
#include <math.h>
#include <conio.h>
#include <stdlib.h>
int giaithua(int);
int main()
{
    int x,n=0;
    float a,sinx,eps;
    printf("nhap x va do chinh xac eps ");
    scanf("%d %f",&x,&eps);
    while(abs(a)<=eps)
    {
                 a=(pow(-1,n)*pow(x,2*n+1)/giaithua(2*n+1));
                 sinx+=a;
                 n++;                
    }
    printf("%f",sinx);
    getch();
}
int giaithua(int a=1)
{
    int i,gt=1;
    for(i=1;i<=a;++i)
    gt*=i;
    return gt;
}


