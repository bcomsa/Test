#include <stdio.h>
#include <string.h>

#define MAX 100

int Next(int A[MAX],int n,int k){ //k la so phan tu tap con, n la so phan tu tap cha
	int i = k;
	while(i > 0 && A[i] == (n - k + i)){
		i--;
	}
	if (i == 0){
		return 0;
	}
	else{
		A[i]++;
		for(int j = i + 1;j < k + 1;++j){
			A[j] = A[j-1] + 1;
		}	
		return 1;
	}
}

int Result(int A[MAX],int k){
	static int count = 0;
	printf("\nxau thu %d : ",++count);
	for(int i = 1;i < k + 1;++i){
		printf("%d",A[i]);
	}
}
int Generate(int A[MAX],int n,int k){
	do{
		Result(A,k);
	}while(Next(A,n,k));	
}

int main(){
	int A[MAX];
	int n = 9,k = 3;
	for(int i = 1;i < k + 1;++i){
		A[i] = i;
	}
	Generate(A,n,k);		
}