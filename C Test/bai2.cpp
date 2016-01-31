#include <stdio.h>
#include <conio.h>

int main(){
	int mang[100][100];
	int num,hang,cot,max,dem,flag;
	FILE *fp,*fp2;
	fp = fopen("square.in","r");
	fp2 = fopen("square.out","w");
	fscanf(fp,"%d",&num);
	for(int k = 0;k < num;++k){
		dem = 0, 
		fscanf(fp,"%d",&hang);
		fscanf(fp,"%d",&cot);
		fscanf(fp,"%d",&max);
		for(int i = 0;i < hang;++i)
			for(int j = 0;j < cot;++j)
				fscanf(fp,"%d",&mang[i][j]);
		for(int i = 0;i < hang - max + 1;++i){
			for(int j = 0;j < cot - max + 1;++j){	
				flag = 1;
				if(mang[i][j]){
					for(int k = i;k < i + max;++k){
						for(int l = j;l < j + max;++l){
							if (!mang[k][l]) flag = 0;
						}
					if(!flag) break;
					}
				if (flag) dem++;
				}
			}
		}
		fprintf(fp2,"%d\n",dem);		
	}
	fclose(fp);
	fclose(fp2);
}
