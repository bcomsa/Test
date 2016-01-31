#include <stdio.h>
#include <conio.h>
#include <time.h>
int main(){
	int max = 0,a = 100,temp;
	for(int j = 0;j < 100;j++){
	for(int i = j;i < a;++i){
		temp = i; 
		while (temp != 1){
			if(temp % 2 == 0) temp /= 2;
			else temp = 3*temp + 1;
			if (temp > max) max = temp;
		}
	  	printf("%d",max);
	}
	a += 100;
	}
 	time_t lt;
	lt = time(NULL);
	printf("%d\n",clock());
}