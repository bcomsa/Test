#include <stdio.h>
#include <conio.h>
#include <string.h>

typedef struct donhang
{
       char tenhang[20];
       int dongia;
       int soluong;
       int thanhtien;
};
void nhap(donhang *a,int n)
{
    char ten[20];
    for(int i=0;i<n;++i)
    {
            printf("don hang thu %d\n",i+1);
            printf("nhap ten hang\n");
            fflush(stdin);
            gets((*(a+i)).tenhang);
            printf("nhap don gia\n");
            scanf("%d",&a[i].dongia);
            printf("nhap so luong\n");
            scanf("%d",&(a+i)->soluong);
            (*(a+i)).thanhtien=((*(a+i)).soluong)*((*(a+i)).dongia);
            printf("thanh tien = %d\n",(*(a+i)).thanhtien);
    }
}
void xuat(donhang *a,int n)
{
    int tong=0;
    printf("\n   STT      TEN HANG   DON GIA  SO LUONG  THANH TIEN\n");
    for(int i=0;i<n;i++)
    {
                      printf("%5d     %7s     %5d     %5d       %5d\n",i+1,a[i].tenhang,a[i].dongia,a[i].soluong,a[i].thanhtien);
                      tong+=a[i].thanhtien;
    }
    printf("                                TONG TIEN     %3d",tong);
    getch();
}
void sapxep(donhang *a ,int n)
{
    donhang temp;
    for(int i=0;i<n-1;++i)
    {       
            for(int j=n;j>i;--j)
            {
                    if(strcmp((a+i)->tenhang,(a+j)->tenhang)>0)
                    {
                     temp=*a;
                     *(a+i)=*(a+j);
                     *(a+j)=temp;
                    }
            }
    }
}
int main()
{
    donhang a[20];
    int n;
    printf("nhap so luong don hang\n");
    scanf("%d",&n);
    nhap(a,n);
    sapxep(a,n);
    xuat(a,n);
}
