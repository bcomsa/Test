#include <stdio.h>
#include <conio.h>
int main()
{   int matran[100],i,n;
    printf("moi ban nhap vao so nguyen duong\n");
    scanf("%d",&n);
    for (i=0;i<n*n;++i)
    {   
        printf("\nnhap phan tu thu %d : ",i);
        scanf("%d",&matran[i]);
    }
    for(i=0;i<n*n;++i)
    {                 if (i==n*n-1)
                      printf(" %d voi n=%d",matran[i],n);
                      else
                      if (i%n==0)
                      printf("\n%d",matran[i]);
                      else
                      printf(" %d",matran[i]);
    }
    getch();
}
