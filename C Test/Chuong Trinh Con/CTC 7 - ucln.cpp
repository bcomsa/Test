#include <stdio.h>
#include <conio.h>

int ucln(int a,int b)
{
    if(a==b)
    return a;
    else if (a>b) return ucln(a-b,b);
    else if (a<b) return ucln(b-a,a);
}
int main()
{
    int a,b;
    printf("nhap 2 so a b\n");
    scanf("%d %d",&a,&b);
    printf("ucln = %d",ucln(a,b));
    getch();
}
