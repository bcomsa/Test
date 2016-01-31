#include <stdio.h>


int DeQuyMax(int *a, int n, int &max){
	if ( n ==1) {return max=(max > a[1])?max:a[1];}
 	if (max < a[n]) max = a[n];
 	DeQuyMax(a, n-1, max);	
}
 
int main(){
	int a[10] = {0,8,2,3,4,5,6,7},max = 0;
	DeQuyMax(a,7,max);
	printf("\nmax = %d",max);	
}