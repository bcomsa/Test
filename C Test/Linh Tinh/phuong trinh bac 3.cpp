#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <stdlib.h>

void nhapdathuc(float *a);
float tinhdathuc(float *a,float x);
float tinhx(float n,float *mang,float a,float b);   
float dochinhxac(float x,float a ,float b);
int main()
{
    float mang[3],a,b,c;
    printf("chuong trinh tinh pt bac 3 a3x^3+a2x^2+a1x+a0=0\n");
    printf("nhap khoang phan ly (a,b)\na = "); scanf("%f",&a);
    printf("b = "); scanf("%f",&b);
    printf("nhap do chinh xac\ndenta = "); scanf("%f",&c);
    printf("nhap he so\n");
    nhapdathuc(mang);
    printf("nghiem pt la : %f",tinhx(dochinhxac(c,a,b),mang,a,b));
    getch();
}
void nhapdathuc(float *a)
{
    for(int i=0;i<4;++i)
    {
     printf("nhap a%d\n",i); scanf("%f",a+i);
    }
}
float tinhdathuc(float *a,float x)
{
     float tong=0;
     for(int i=1;i<4;++i)
     {
      tong+=(*(a+i))*pow(x,i);
     }
     tong+=*a;
     return tong;
}
float tinhx(float n,float *mang,float a,float b)
{
    int i=0;
    float kq,tb; 
    while(i<n)
    {
     tb=(a+b)/2;
     if(tinhdathuc(mang,a)==0)
     {
      return a;
      break;
     }
     else if(tinhdathuc(mang,b)==0)
          {
           return b;
           break;
          }
          else if((tinhdathuc(mang,a)*tinhdathuc(mang,tb))<0)
               { 
                b=tb;
                i++;
               }
               else if((tinhdathuc(mang,b)*tinhdathuc(mang,tb))<0)
               { 
                a=tb;
                i++;
               }  
    }
    return tb;
}
float dochinhxac(float x,float a,float b)
{
      float n,temp;
      temp=(b-a)/x;
      n=log(temp)/log (2);
      return n; 
}
