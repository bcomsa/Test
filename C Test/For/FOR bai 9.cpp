#include <stdio.h>
#include <conio.h>

int main()
{
    int a[100],b[100],c[100],n,m,x;
    printf("nhap so phan tu mang 1\n");
    scanf("%d",&n);
    for(int i=0;i<n;++i)
    {
            printf("a[%d]= \n",i+1);
            scanf("%d",&a[i]);
    }
    printf("nhap so phan tu mang 2\n");
    scanf("%d",&m);
    for(int i=0;i<m;++i)
    {
            printf("b[%d]= \n",i+1);
            scanf("%d",&b[i]);
    }
    int i=0,j=0,k=0;
    while(i<n&&j<m)
    {
                     if (a[i]<=b[j]) 
                     {
                                  c[k]=a[i];  
                                  k++;
                                  i++;
                     }
                     else
                     {
                                  c[k]=b[j];     
                                  k++;
                                  j++;
                     }
    }
    if(i!=n)
    {
            while(i<n)
            {
                      c[k]=a[i];
                      k++;
                      i++;
            }
    }
    if(j!=m)
    {
            while(j<m)
            {         
                      c[k]=b[j];
                      k++;
                      j++;
            }
    }
    for(i=0;i<m+n;i++)
    printf("%d ",c[i]);
    getch();
}
