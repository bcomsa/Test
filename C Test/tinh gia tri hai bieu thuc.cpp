#include <stdio.h>
#include <conio.h>
#include <math.h>

int nhapheso(int *a,int n)
{
    for(int i=0;i<n;++i)
    {
            printf("\na%d = ",i);
            scanf("%d",&a[i]);
    }
}
float tinhgiatri(int *a,int x,int n)
{
    int mu=0;
    float kq=0;
    for(int i=0;i<n;++i)
    {
            kq+=a[i]*pow(x,mu);
            mu++;
    } 
    return kq;
}
int congheso(int *a,int *b,int n,int m)
{
    int heso[100];
    for(int i=0;i<((n>m)?m:n);++i)
    {
            
            heso[i]=a[i]+b[i];
            printf("\nt%d = %d",i,heso[i]);
    }
    for(int i=(n>m)?m:n;i<((n>m)?n:m);i++)
    {
            (n>m)?heso[i]=a[i]:heso[i]=b[i];
            printf("\nt%d = %d",i,heso[i]);
    }    
}
int main()
{
    int n,m,x,mang[100],mang1[100];
    printf("nhap x\n");
    scanf("%d",&x);
    printf("nhap so mu toi da cua P\n");
    scanf("%d",&n);
    printf("nhap cac he so");
    nhapheso(mang,n); 
    printf("nhap so mu toi da cua Q\n");
    scanf("%d",&m);
    printf("nhap cac he so");
    nhapheso(mang1,m);
    printf("gia tri bieu thuc P = %.2f\n",tinhgiatri(mang,x,n));
    printf("gia tri bieu thuc Q = %.2f\n",tinhgiatri(mang1,x,m));
    printf("gia tri bieu thuc T = %.2f\n",tinhgiatri(mang,x,n)+tinhgiatri(mang1,x,m));
    congheso(mang,mang1,n,m);
    for(int i=0;i<n;++i)
    printf("\np%d = %d",i,mang[i]);
    for(int i=0;i<m;++i)
    printf("\nq%d = %d",i,mang1[i]);
    printf("\nx = %d",x);
    getch();
}
