#include <stdio.h>
#include <string.h>
#define MAX 100

int NextBS(int BS[MAX],int n){
	int i = n;
	while (i > 0 && BS[i]){
		BS[i--] = 0;
	}
	if(i == 0){
		return 0;	
	}
	else{
		BS[i] = 1;
		return 1;
	}
}

int Result(int BS[MAX],int n){
	static int count = 0;
	printf("\nxau thu %d : ",++count);
	for(int i = 1;i < n+1;++i){
		printf("%d",BS[i]);
	}
}
int Generate(int BS[MAX],int n){
	do{
		Result(BS,n);
	}while(NextBS(BS,n));	
}

int main(){
	int BS[MAX];
	int n = 3;
	memset(BS,0,(n+1)*sizeof(int));
	Generate(BS,n);		
}