#include <stdio.h>
#include <malloc.h>

int main(){
	int *mang,n,x;
	printf("\nnhap so phan tu : \n");
	scanf("%d",&n);
	mang = (int*)malloc(n*sizeof(int));
	for (int i = 0;i < n;++i){
		printf("\nphan tu thu %d = ",i);
		scanf("%d",mang+i);
	}
	int temp,i,j;
	for (i = 0;i < n-1;++i)
		for(j = i+1;j < n;++j){
			if(mang[i] > mang[j])
			{
				temp = mang[i];
				mang[i] = mang[j];
				mang[j] = temp;	
			}
		}
	printf("\nmang da duoc sap xep\n");
	for (i = 0;i < n;++i){
		printf("%d ",*(mang+i));
	}
	printf("\nnhap x : \n");
	scanf("%d",&x);
	i = 0;
	n++;
	mang = (int*)realloc(mang,n*sizeof(int));
	while(x >= mang[i] && i < n){
		i++;
	}
	if(i < n){
		for(j = n;j > i;--j){
			mang[j] = mang[j-1];	
		}
		mang[i] = x;	
	}
	else{
		mang[n] = x;
	}	
 	printf("\nmang da duoc sap xep\n");
	for (i = 0;i < n;++i){
		printf("%d ",*(mang+i));
	}
}