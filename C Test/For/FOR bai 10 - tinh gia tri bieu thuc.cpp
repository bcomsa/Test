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
double tinhgiatri(int *a,int x,int n)
{
    int mu=0;
    double kq=0;
    for(int i=0;i<n;++i)
    {
            kq+=a[i]*pow(x,mu);
            mu++;
    } 
    return kq;
}
int main()
{
    int n,x,mang[100];
    printf("nhap x\n");
    scanf("%d",&x);
    printf("nhap so mu toi da va gia tri x\n");
    scanf("%d",&n);
    printf("nhap cac he so");
    nhapheso(mang,n);
    for(int i=n-1;i>=0;--i)
    {
            if(mang[i]!=0)
            {   
                       if(mang[i]>0&&i==0)
                       printf("+%d",mang[i]);
                       else   
                       if(mang[i]>0&&i==n-1)
                       {
                                          if(mang[i]==1)
                                          printf("x^%d",i);
                                          else  
                                          printf("%dx^%d",mang[i],i);
                       }
                       else
                       if(mang[i]>0&&i==1)
                       {                  
                                          if(mang[i]==1)
                                          printf("+x");
                                          else
                                          printf("+%dx",mang[i]);
                       }
                       else
                       if(mang[i]<0&&i==1)
                       {                  
                                          if(mang[i]==1)
                                          printf("-x");
                                          else
                                          printf("%dx",mang[i]);
                       }
                       else
                       
                       if(mang[i]>0)
                       {
                                    if(mang[i]==1)
                                    printf("+x^%d",i);
                       else
                                    printf("+%dx^%d",mang[i],i);
                       }
                       else
                       if(mang[i]<0)
                       {
                                    if(mang[i]==1)
                                    printf("x^%d",i);
                       else
                                    printf("%dx^%d",mang[i],i);
                       }
            }
    }
    printf("\ngia tri bieu thuc = %.2f",tinhgiatri(mang,x,n));
    getch();
}
