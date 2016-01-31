#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    struct donhang
    {
           char tenhang[20];
           int dongia;
           int soluong;
           int thanhtien; 
    }mang[50];
    FILE *f;
    int tong=0,n,i=0;
    printf("nhap so luong don hang\n");
    scanf("%d",&n);
    for(i=0;i<n;++i)
    {
     printf("nhap don hang thu %d",i+1);
     printf("\nten hang : ");
     fflush(stdin);
     gets(mang[i].tenhang);
     printf("\ndon gia : ");
     scanf("%d",&mang[i].dongia);
     printf("\nso luong : ");
     scanf("%d",&mang[i].soluong);
     mang[i].thanhtien=mang[i].soluong*mang[i].dongia;
     printf("\nthanh tien : %d\n",mang[i].thanhtien);
    }
    f=fopen("SO_LIEU.C","wb");
    if(f==NULL)
    {
     perror("\nloi khong mo (tao moi) duoc tep");
     getch();
     exit(1);
    }
    fwrite(mang,sizeof(donhang),n,f);
    printf("ghi thanh cong, an phim bat ki de xem du lieu tep");
    getch();
    fclose(f);
    f=fopen("SO_LIEU.C","rb");
    fread(mang+n,sizeof(donhang),n,f);
    printf("\n   STT      TEN HANG   DON GIA  SO LUONG  THANH TIEN\n");
    for(i=n;i<2*n;++i)
     {
                      printf("%5d     %7s     %5d     %5d       %5d\n",i-n+1,mang[i].tenhang,mang[i].dongia,mang[i].soluong,mang[i].thanhtien);
                      tong+=mang[i].thanhtien;
     }
    printf("                                TONG TIEN   %3d",tong);
    fclose(f);
    getch();
}
