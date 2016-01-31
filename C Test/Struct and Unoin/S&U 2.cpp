#include <stdio.h>
#include <string.h>

struct bana
{
       float toan,ly,hoa;
};
struct banc
{
       float van,su,dia;
};
struct ngay
{
       unsigned int ngay,thang,nam;
};
union khoi
{
     struct bana a;
     struct banc c;
};   
typedef struct sinhvien
{
       char hoten[50],que[50];
       struct ngay ngaysinh;
       char khoi;
       float tongdiem;
       union khoi khoithi; 
}thisinh;
void nhap(thisinh *a,int n)
{
    char chuoi[50],ctemp;
    float ftemp;
    int itemp,i;
    for(i=0;i<n;++i)
    {
            printf("nhap du lieu thi sinh thu %d\n",i+1);
	    fgets(chuoi,50,stdin);//fflush(stdin);
            printf("ho va ten\n"); fgets(chuoi,50,stdin); chuoi[strlen(chuoi)-1]='\0'; strcpy((a+i)->hoten,chuoi);
            printf("que quan\n");  fgets(chuoi,50,stdin); chuoi[strlen(chuoi)-1]='\0'; strcpy((a+i)->que,chuoi);
            printf("ngay sinh\n"); 
            scanf("%d",&itemp); a[i].ngaysinh.ngay=itemp; 
            scanf("%d",&itemp); a[i].ngaysinh.thang=itemp;
            scanf("%d",&itemp); a[i].ngaysinh.nam=itemp;
            printf("khoi (a hoac c)\n");
            fgets(chuoi,50,stdin);//fflush(stdin);
            nhapkhoi:
            scanf("%c",&ctemp);
            (a+i)->khoi=ctemp;
            if((a+i)->khoi=='a')
            {
                                printf("nhap diem toan ly hoa\n");
                                scanf("%f",&ftemp); a[i].khoithi.a.toan=ftemp;
                                scanf("%f",&ftemp); a[i].khoithi.a.ly=ftemp;
                                scanf("%f",&ftemp); a[i].khoithi.a.hoa=ftemp;
                                (a+i)->tongdiem=(*(a+i)).khoithi.a.toan+(*(a+i)).khoithi.a.ly+(*(a+i)).khoithi.a.hoa;
            }
            else
                if((a+i)->khoi=='c')
                {
                                printf("nhap diem van su dia\n");
                                scanf("%f",&ftemp); a[i].khoithi.c.van=ftemp;
                                scanf("%f",&ftemp); a[i].khoithi.c.su=ftemp;
                                scanf("%f",&ftemp); a[i].khoithi.c.dia=ftemp;
                                (a+i)->tongdiem=(*(a+i)).khoithi.c.van+(*(a+i)).khoithi.c.su+(*(a+i)).khoithi.c.dia;
                }
                else
                {
                 printf("nhap lai khoi (a hoac c)\n");   
                 goto nhapkhoi;
                }        
    }
}
void sapxep(thisinh *a,thisinh *khoia,thisinh *khoic,int n,int *k,int *l)
{
 thisinh temp;
 int i,j,m,p;
 m=0;
 p=0;
 for(i=0;i<n;i++)
 {
         if((a+i)->khoi=='a')
         {
                             khoia[m]=a[i];
                             m++;
         }
         else
         {
                             khoic[p]=a[i];
                             p++;
         }         
 }
 for(i=0;i<(m)-1;++i)
         for(j=m;j>i;j--)
         if(khoia[i].tongdiem<khoia[j].tongdiem)
         {
           temp=khoia[i];
           khoia[i]=khoia[j];
           khoia[j]=temp;                                     
         }
 for(i=0;i<p-1;++i)
         for(j=p;j>i;j--)
         if(khoic[i].tongdiem<khoic[j].tongdiem)
         {
           temp=khoic[i];
           khoic[i]=khoic[j];
           khoic[j]=temp;                                     
         }    
 *k=m;
 *l=p;
}
void xuat(thisinh *a,int n,int choose)
{
    int i;
    if(choose==1)
  {
    printf("     DANH SACH THI SINH KHOI A         \n");
    printf("STT HO TEN         QUE        NGAY SINH   TOAN   LY   HOA   TONG\n");
    for(i=0;i<n;++i)
    printf("\n%d   %6s   %6s  %2d/%2d/%2d  %.2f  %.2f %.2f %.2f\n",i+1,a[i].hoten,a[i].que,a[i].ngaysinh.ngay,a[i].ngaysinh.thang,a[i].ngaysinh.nam,a[i].khoithi.a.toan,a[i].khoithi.a.ly,a[i].khoithi.a.hoa,a[i].tongdiem);
  }
    else
  {
    printf("     DANH SACH THI SINH KHOI C         \n");
    printf("STT HO TEN         QUE        NGAY SINH   TOAN   LY   HOA   TONG\n");
    for(i=0;i<n;++i)
    printf("\n%d   %6s   %6s  %2d/%2d/%2d  %.2f    %.2f %.2f %.2f\n",i+1,a[i].hoten,a[i].que,a[i].ngaysinh.ngay,a[i].ngaysinh.thang,a[i].ngaysinh.nam,a[i].khoithi.a.toan,a[i].khoithi.a.ly,a[i].khoithi.a.hoa,a[i].tongdiem);
  }
}
int main()
{
    thisinh a[50],khoia[50],khoic[50];
    int n,m,p,*k,*l;
    printf("nhap so thi sinh\n");
    scanf("%d",&n);
    nhap(a,n);
    k=&m;
    l=&p;
    sapxep(a,khoia,khoic,n,k,l);
    xuat(khoia,m,1);
    xuat(khoic,p,0);
}
