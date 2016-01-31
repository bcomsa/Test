

#include <stdio.h>
#include <conio.h>
int main()
{   int matran[100][100],max=0,i,j,n,dem=0;
    printf("moi ban nhap vao so nguyen duong\n");
    scanf("%d",&n);
    for (i=0;i<n;++i)
        for(j=0;j<n;++j)
        {   
            printf("\nnhap phan tu thu %d-%d : ",i,j);
            scanf("%d",&matran[i][j]);
        }
    for(i=0;i<n;++i)
    {
                      printf("\n");                
                      for(j=0;j<n;++j)                 
                      printf("%d ",matran[i][j]);
    }
    
    max=matran[n][n];
     for (i=0;i<n;++i)
        for(j=0;j<n;++j)
        {   if((i+j)>n-1)
            {
                         max=matran[i][j];
                         dem+=1;
            
            }
        }
    printf("\nco %d max = %d",dem,max);
    getch();
}
