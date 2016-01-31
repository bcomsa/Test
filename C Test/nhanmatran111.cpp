#include <stdio.h>
#include <stdlib.h>

int main(){
	int matran1[100][100],matran2[100][100],kq[100][100],m,n,p;
	printf("nhap so hang va cot ma tran 1 : ");
	scanf("%d%d",&m,&n);
	printf("nhap so cot ma tran 2 : ");
	scanf("%d",&p);
	printf("Nhap ma tran 1\n");
	for(int i = 0;i < m;++i)
	{
		for(int j = 0;j < n;++j)
		{
			printf("A1[%d][%d] = ",i,j);	
			scanf("%d",&matran1[i][j]);
		}
	}
	printf("Nhap ma tran 2\n");
	for(int i = 0;i < n;++i)
	{
		for(int j = 0;j < p;++j)
		{
			printf("A1[%d][%d] = ",i,j);	
			scanf("%d",&matran2[i][j]);
		}
	}
	for(int i = 0;i < m;++i)
	{
		for(int j = 0;j < p;++j)
		{
			kq[i][j]=0;
			for(int k = 0;k < n;k++)
			{
				kq[i][j]+=matran1[i][k]*matran2[k][j];
			}
		}
	}
	
    for(int i=0;i<m;++i)
    {
            for(int j=0;j<p;++j)
            {
                    printf("%d ",kq[i][j]);
            }
            printf("\n");
    }
}
