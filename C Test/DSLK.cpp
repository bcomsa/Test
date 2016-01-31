#include <stdio.h>
#include <conio.h>
#include <malloc.h>
#include <string.h>

struct mark{
	float toan,ly,hoa; 
};
typedef struct{
	char hoten[30];
	struct mark diem;	
}sinhvien;

char* getName(char *hoten){
	int k=0,j,i=strlen(hoten);
	char kq[30];
	while(hoten[i]=' '){
		i--;
	}
	for(int i = j;i < strlen(hoten)+1;i++){
		kq[k++] = hoten[i];
	}
	return kq;  
}
int main(){
	sinhvien *sv,*svTen,*svDTB;
	int i,j,k,l=0,sosv;
	printf("\nnhap so sinh vien : ");
	scanf("%d",&sosv);
	sv = (sinhvien*)malloc(sosv*sizeof(sinhvien));
	for(i = 0;i < sosv;++i){
		printf("Nhap Du Lieu Sinh Vien Thu %d\n",i+1);
		printf("Ho Ten : ");
		fflush(stdin); gets(sv[i].hoten);
		printf("Diem Toan : "); scanf("%f",&sv[i].diem.toan);
		printf("Diem Ly   : "); scanf("%f",&sv[i].diem.ly);
		printf("Diem Hoa  : "); scanf("%f",&sv[i].diem.hoa);
	}
	for(i = 0;i < sosv;++i){
		printf("Sinh Vien Thu %d\n",i+1);
		printf("Ho Ten : %s\n",sv[i].hoten);
		printf("Diem Toan : %.2f\n",sv[i].diem.toan);
		printf("Diem Ly   : %.2f\n",sv[i].diem.ly);
		printf("Diem Hoa  : %.2f\n",sv[i].diem.hoa);
	}
	svTen = svDTB = sv;
	for(i = 0;i < sosv - 1;++i){
		for (j = i;j < sosv;++j)
		if(strcmp(getName(svTen[i].hoten),getName(svTen[j]hoten)) < 0){
			char temp[20];
		}
	}	
}