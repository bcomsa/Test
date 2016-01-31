#include <stdio.h>
 int main(){
 	int mang[20],n,i,j,tg,find;
 	printf("nhap n phan tu : ");
 	scanf("%d",&n);
 	for(i = 0;i < n;++i){
	 	printf("mang[%d] = ",i);
	 	scanf("%d",&mang[i]);
	}
	printf("\nnhap phan tu muon tim kiem : ");
 	scanf("%d",&find);
 	printf("\ntruoc khi sap xep : ");
 	for(i = 0;i < n;++i){
	 	printf("  %d ",mang[i]);
	}
	for(i = 0;i < n - 1;++i)
		for(j = i;j > 0; --j)
		if(mang[i]<mang[j]){
			tg=mang[i];
			mang[i] = mang[j];
			mang[j] = tg;
		}
	printf("\nsau khi sap xep : ");
 	for(i = 0;i < n;++i){
	 	printf("  %d ",mang[i]);
	}
 	for(i = 0;i < n;++i){
		if(mang[i] == find){
			printf("co phan tu %d \n",find);
			break;
		}
		}
	printf("khong co phan tu %d \n",find);
	}
 }