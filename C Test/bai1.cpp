#include <stdio.h>
#include <conio.h>

int main(){
	FILE *fp,*fp2;
	int num,num1,num2;
	fp = fopen("number1.inp","r");
	fp2 = fopen("number1.out","w");
	fscanf(fp,"%d",&num);
	for(int i = 0;i < num;++i){
		int max = -30000;
		fscanf(fp,"%d",&num1);
		for(int j = 0;j < num1;++j){
			fscanf(fp,"%d",&num2);
			if(num2 > max) max = num2;
		}
		fprintf(fp2,"%d\n",max);
	}
	fclose(fp);
	fclose(fp2);
}