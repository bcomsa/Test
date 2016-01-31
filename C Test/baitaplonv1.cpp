#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>

typedef struct khachHang{
	long soTk;
	char pin[6];
	char tenTk[30];
	double soDu;
	int trangThai;
};

long int readnum(FILE* );

void getpassword(char* , int );

int createAcc();
	
int main(){
	createAcc();
	return 0;
}
int readnum(char* dir){ //ham xuat ra so tiep theo tu CSDL , dir la ten CSDL (nameATM.txt,soTk.txt)
	FILE *fp;
	fp = fopen(dir,"r+");
	if (fp == NULL){ // neu nhu chua khoi tao thi khoi tao. gan gia tri dau tien bang 1
		int result = 1;
		fp = fopen(dir,"w");
		fprintf(fp,"\n%d",result);
		fclose(fp);
		return result;
	}
	else{
		int i=0,result;
		char temp,number[20];
		fseek(fp,0,2);
		while((temp=fgetc(fp))!='\n'){ //kiem tra vi tri cua so cuoi cung
			fseek(fp,-2,1); 
		}
		while(!feof(fp)){
			number[i++]=fgetc(fp); //quet so vao mang number	
		}
		result = atoi(number) + 1;
		fprintf(fp,"\n%d",result); // in gia tri ke tiep vao CSDL
		fclose(fp);
		return result;
	}
}
     
void getpin(char s[], int size)//chuong trinh mat khau dau * 
     
{
     
    char ch=0;
     
    memset(s,0,size);
     
    fflush(stdin);
     
    while (ch!=13)//ch khác Enter
     
    {
     
    fflush(stdin);
     
    ch=getch();
     
    if (ch<=0)
     
    getch();// loai bo cac ki tu dieu khien
     
    else if (ch>47 && ch<58)//in cac ki tu so
     
    {
     
    if (int(strlen(s))<size-1) //neu chuoi chua day
     
    {
     
    printf("*");;
     
    s[strlen(s)]=ch;
     
    }
     
    }
     
    else if (ch==8)//backspace.
     
    if (s[0])//neu chuoi khac rong
     
    {
     
    s[strlen(s)-1]=0;//xoa ki tu cuoi cung
     
	printf("%c ",ch); // |   xoa ki tu truoc do tren man hinh 
	printf("%c",ch); //  |
	     
    }
     
    }
     
    printf("\n");
     
    fflush(stdin);
     
}

int	createAcc(){
	FILE *fp;
	char dir[30],temp[20],check;
	khachHang khach;
		itoa(readnum("CSDL.txt"),temp,10);	// noi string thanh dang acc[%d].dat.
		strcpy(dir,"acc");      			//
		strcat(dir,temp);					//
		strcat(dir,".dat");					//
	printf("tao tai khoan ATM \n");
	printf("nhap Ho Ten\n"); fflush(stdin); gets(khach.tenTk);
	printf("nhap ma PIN\n"); 
	Nhap1:
	getpin(khach.pin,7);
	if(khach.pin[5] == 0){
		printf("khong du 6 chu so. Nhap lai ma PIN\n");	
		goto Nhap1;
	}  
	printf("ma PIN cua ban la %s.Dong y ?(y)\n",khach.pin);
	fflush(stdin); check = getch();
	if(check == 'y') goto Nhap2;
	else{
		printf("nhap ma PIN");
		goto Nhap1;	
	}
	Nhap2:
	printf("haha");
	fp=fopen(dir,"w");		
	fprintf(fp,"hahahaha");		
	fclose(fp);	
}
