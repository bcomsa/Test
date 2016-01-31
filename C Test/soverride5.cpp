#include<stdio.h>
#include<string.h>

int main(void){
	int i=0,j=0,k=0;
	char chuoidai[500],chuoi[4][500];
	fflush(stdin);
	scanf("%[^\0]",chuoidai);
	while(i<=strlen(chuoidai)){
		if(i==strlen(chuoidai))
		chuoi[j][k]='\0';
		else
		if(chuoidai[i]=='\n'){
			chuoi[j][k]='\0';
			j++;k=0;i++;
		}
		else{
		chuoi[j][k]=chuoidai[i];
		k++;i++;
		}
	}
	for(i=0;i<5;++i){
		j=0;
		while(j<strlen(chuoi[i])){
		 if(chuoi[i][j]=='@')
  		   printf("%d-%d, ",i+1,j);
         j++;
        }
	}
	printf("\b\b");
}