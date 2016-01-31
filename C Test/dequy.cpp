#include <stdio.h>
#include <conio.h>

int somu(int a,int b)
{
    if (b==0)
    return 1;
    else
    return a*somu(a,b-1);
}
int giaithua(int a)
{
    if (a==0)
    return 1;
    else
    return a*giaithua(a-1);
}
int tonglapphuong(int n)
{
    if(n==1)
    return 1;
    else
    return (somu(n,3)+tonglapphuong(n-1));
}
int main()
{   
    int x,y,a,n,i;
    printf("Chuong Trinh Tinh So Mu(nhap 1),Giai Thua(nhap 2),Tong Lap Phuong(nhap 3)\n");
    scanf("%d",&i);
    switch(i)
    {
             case 1: printf("Chuong Trinh Tinh So Mu x^y\n");
                     printf("nhap x va y\n");
                     scanf("%d %d",&x,&y);
                     printf("%d^%d = %d",x,y,somu(x,y));
                     break;
             case 2: printf("Chuong Trinh Tinh Giai Thua (2a)!\n");
                     printf("nhap a\n");
                     scanf("%d",&a);
                     printf("(%d)! = %d",2*a,giaithua(2*a));
                     break;
             case 3: printf("Chuong Trinh Tinh Tong Lap Phuong 1^3+2^3+...n^3\n");
                     printf("nhap n\n");
                     scanf("%d",&n);
                     printf("Tong Lap Phuong = %d",tonglapphuong(n));
                     break;
             default:
                     break;
    }
    getch();
}
