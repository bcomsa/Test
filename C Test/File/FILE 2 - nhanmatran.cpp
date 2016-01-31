#include <stdio.h>
#include <conio.h>

int kq[100][100];
int nhapmatran(int a[100][100],int m,int n)
{   
    for(int i=0;i<m;++i)
    {
            for(int j=0;j<n;++j)
            {       printf("\na[%d][%d]= ",i+1,j+1);
                    scanf("%d",&a[i][j]);
            }
    }   
}
int nhanmatran(int a[100][100],int b[100][100],int m,int n,int x,int y)
{
    for(int i=0;i<m;++i)
    {
            for(int j=0;j<y;++j)
            {
                    kq[i][j]=0;
                    for(int k=0;k<n;++k)
                    kq[i][j]+=a[i][k]*b[k][j];
            }
    }
}
int main()
{
    int a[100][100],b[100][100];
    int m,n,x,y;
    FILE *f;
    do
    {          
               printf("nhap hang cot ma tran 1\n");
               scanf("%d %d",&m,&n);
               printf("nhap hang cot ma tran 2\n");
               scanf("%d %d",&x,&y);
               if(n!=x)
               printf("2 ma tran nay khong nhan duoc,moi nhap lai\n");
    }
    while(n!=x);
    {
     printf("nhap du lieu ma tran 1\n");
     nhapmatran(a,m,n);
     printf("nhap du lieu ma tran 2\n");
     nhapmatran(b,x,y);
    }
    nhanmatran(a,b,m,n,x,y);
    f=fopen("TICH_MT.C","w");
    fprintf(f,"n=%d p=%d m=%d\n",m,n,y);
    fprintf(f,"Ma Tran 1");
    for(int i=0;i<m;++i)
    {
                    fprintf(f,"\n");    
                    for(int j=0;j<n;++j)
                    fprintf(f,"%3d ",a[i][j]);       
    }
    fprintf(f,"\nMa Tran 2");
    for(int i=0;i<x;++i)
    {
                    fprintf(f,"\n");
                    for(int j=0;j<y;++j)
                    fprintf(f,"%3d ",b[i][j]);       
    }
    fclose(f);
    printf("\nGhi Thanh Cong");
    f=fopen("TICH_MT.C","a");
    fprintf(f,"\nTich ma tran ");
    for(int i=0;i<m;++i)
    {
                    fprintf(f,"\n");
                    for(int j=0;j<y;++j)
                    fprintf(f,"%3d ",kq[i][j]);       
    }
    fclose(f);
    getch();
}
