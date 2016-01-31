#include<stdio.h>
#include<conio.h>
int i;
int* doicoso(int,int);
int main()
{
    int so,j,*mang;
    printf("moi ban nhap so can chuyen so = ");
    scanf("%d",&so);
    printf("\nco so 2\n");
    mang=doicoso(so,2);
    for(j=i-1;j>=0;--j)
    printf("%d",*(mang+j));
    printf("\nco so 8\n");
    mang=doicoso(so,8);
    for(j=i-1;j>=0;--j)
    printf("%d",*(mang+j));
    printf("\ncoso 16\n");
    mang=doicoso(so,16);
    for(j=i-1;j>=0;--j)
    {
                       switch(mang[j])
                       {
                       case 10:
                            printf("A");
                            break;
                       case 11:
                            printf("B");
                            break;
                       case 12:
                            printf("C");
                            break;
                       case 13:
                            printf("D");
                            break;
                       case 14:
                            printf("E");
                            break;
                       case 15:
                            printf("F");
                            break;
                       default:
                            printf("%d",*(mang+j));
                            break;
                       }
    }   
    getch();
}
int* doicoso(int a,int b)
{
    int mang[100];
    i=0;
    while(a>0)
    {          
               mang[i]=a%b;
               i++;
               a=a/b;
    }
    return mang;
}
