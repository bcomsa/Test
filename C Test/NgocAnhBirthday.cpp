#include<stdio.h>
#include<conio.h>
#include<string.h>
void happybirthday()
{
    printf("*     *     *     ******  ******   *     *\n");
    printf("*     *    * *    *     * *     *   *   *\n");
    printf("*******   *****   ******  ******      *\n");
    printf("*     *  *     *  *       *           *\n");
    printf("*     * *       * *       *           *\n\n");
    printf("******   **   ******  ******* *     * ******      *     *     *\n"); 
    printf("*     *  **   *     *    *    *     * *     *    * *     *   *\n");
    printf("******   **   ******     *    ******* *     *   *****      *\n");
    printf("*     *  **   *  **      *    *     * *     *  *     *     *\n");
    printf("******   **   *    **    *    *     * ******  *       *    *\n");
}
void loianhnhannhu()
{
    printf("\nAnh nhan nhu trong thiep roi :),hihi,cai nay cho them phan dac biet nha :)) vui ca ngay nha :P\
    \nhihi hom bua anh noi, anh moi hoc duoc 1 phan moi do,em nho ko, hihi, hom ma anh tang em cai lap\
    \ntrinh trai tim do :P,hom nay anh ap dung vao roi do:))hihi, ep buoc em phai ghi:EM YEU ANH moi duoc\
    \nhihi :P,dung gian anh nha co be :),sau khi thay cai nay roi em thich mon qua nao hon,con minion hay\
    \nla cai nay :),nho noi anh biet nha :),hihi,minion la hom thu nam do, anh di qua ben quan binh thanh :)\
    \nhihi,cach ktx cua em 5km do:P,hihi, qua do het hang,nen a ghe qua em luon hihi, luc ve anh ghe vo tiem\
    \nkia mua luon,ben kia no hen thu sau :), ma xa qua nen thoi :)) hihi, con minion dep ko em,a biet\
    \nem se thich lam cho xem^^,hihi,anh tinh mua tu nam ngoai roi,ma ko co dip:),hom 14/2,cung tinh tang em\
    \nhihi,ma thoi,de dip dac biet nhat,sinh nhat a,tang luon^^..hihi..,em biet khong lan dau tien anh\
    \ntang qua cho con gai do:),hihi,con gai thoi nha :P phu nu thi con co me anh nua :),hihi,em la nguoi \
    \ndau tien va duy nhat luon:).yeu Ngoc Anh cua anh nhat^^\n");
}
int main()
{   
    int i=0;
    char a[20]={"EM YEU ANH"},b[20];
    printf("Ngoc Anh oi yeu anh ko :))..yeu thi nhap EM YEU ANH nha, cho em xem cai nay vui lam :P\n");
    gets(b);
    while(strcmp(a,b)!=0)
    {
                        printf("hihi,em nhap sai roi kia :)) yeu anh ko :)),cho tra loi lai do :P, yeu thi nhap EM YEU ANH nha :P\n");
                        gets(b);
    } 
    printf("hihi phan thuong cho em ne\n");
    do
    {
                   printf("THONG DIEP CUA ANH  (nhap vao so 1 roi an enter)\nLOI NHAN NHU CUA ANH(nhap vao so 2 roi an enter)\nTHOAT CHUONG TRINH  (nhap vao so 3 roi an enter)\n");
                   scanf("%d",&i);
                   switch(i)
                   {
                            case 1:
                            happybirthday();
                            break;
                            case 2:
                            loianhnhannhu();
                            break;
                            default:
                            break;
                   }
    }while(i!=3);
}
