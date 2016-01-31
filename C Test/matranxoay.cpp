#include<stdio.h>
#include<conio.h>
int mang[100][100];
int nhapmang(int a)
{
    int i,dem=0,docmin=0,docmax=a-1,ngangmin=0,ngangmax=a-1;
    while(dem<=a*a)
    {
                   for(i=ngangmin;i<=ngangmax;++i)
                   mang[docmin][i]=++dem;
                   docmin++;
                   for(i=docmin;i<=docmax;++i)
                   mang[i][ngangmax]=++dem;
                   ngangmax--;
                   for(i=ngangmax;i>=ngangmin;--i)
                   mang[docmax][i]=++dem;
                   docmax--;
                   for(i=docmax;i>=docmin;--i)
                   mang[i][ngangmin]=++dem;
                   ngangmin++;
    }
}
int main()
{   int i,j,a;
    printf("nhap a : ");
    scanf("%d",&a);
    nhapmang(a);
    for(i=0;i<a;++i)
    {
                    for(j=0;j<a;++j)
                    printf("%2d ",mang[i][j]);
                    printf("\n");
    }
    getch();
}
