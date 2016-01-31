#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
typedef struct SINHVIEN{
	int stt; char hoten[30]; int tuoi; float diemtb;
};
typedef struct NODE{
	SINHVIEN dulieu;
	struct NODE *next;
}*NODEPTR;

void init(NODEPTR *plist){
	*plist=NULL;
}
NODEPTR makenode(void){
	NODEPTR p;
	p=(NODEPTR)malloc(sizeof(struct NODE));
	return(p);
}
int isempty(NODEPTR list){
	return(list==NULL);
}
NODEPTR addfirst(NODEPTR *plist,SINHVIEN x){
	NODEPTR p;
	p=makenode();
	p->dulieu=x;
	if(isempty(*plist)){
		p->next=NULL;
	}else 
	p->next=*plist;
	*plist=p;
	return(p);
}
NODEPTR addbottom(NODEPTR *plist,SINHVIEN x){
	NODEPTR p,q;
	p=makenode();
	p->dulieu=x;
	if(isempty(*plist)){
		*plist=p;
	}else{
		q=*plist;
		while(q->next!=NULL)
			q=q->next;
		q->next=p;
	}
	p->next=NULL;
	return(p);
}
NODEPTR addafter(NODEPTR *plist,int pos,SINHVIEN x){
	NODEPTR p,q;
	p=makenode();
	p->dulieu=x;
	if(isempty(*plist)){
		addfirst(plist,x);
	}else{
		int dem=1;
		q=*plist;
		while(q->next!=NULL&&dem<pos){
			q=q->next;
			dem++;
		}
		p->next=q->next;
		q->next=p;
	}
	return(p);
}

void travelnode(NODEPTR list){
	while (list!=NULL){
		printf("%d,%s,%d,%f\n",list->dulieu.stt,list->dulieu.hoten,list->dulieu.tuoi,list->dulieu.diemtb);
		list=list->next;
	}
}
int main(){
	NODEPTR list;
	SINHVIEN x;
	scanf("%d",&x.stt);scanf("%d",&x.tuoi);scanf("%s",&x.hoten);scanf("%f",&x.diemtb);
	init(&list);
	addafter(&list,1,x);
	scanf("%d",&x.stt);scanf("%d",&x.tuoi);scanf("%s",&x.hoten);scanf("%f",&x.diemtb);
	addbottom(&list,x);
	scanf("%d",&x.stt);scanf("%d",&x.tuoi);scanf("%s",&x.hoten);scanf("%f",&x.diemtb);
	addbottom(&list,x);
	scanf("%d",&x.stt);scanf("%d",&x.tuoi);scanf("%s",&x.hoten);scanf("%f",&x.diemtb);
	addafter(&list,2,x);
	travelnode(list);
}