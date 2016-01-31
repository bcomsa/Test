#include<stdio.h>
#include<conio.h>

int main()
{
    int nam=2000;
    float haik,gdp,v;
    printf("nhap gdp nam 2000 va toc do tang truong binh quan \n");
    scanf("%f %f",&haik,&v);
    printf("nam gdp\n");
    printf("%d  %f \n",nam,haik);
    gdp=haik;
    while(gdp<=2*haik)
    {                
                     gdp+=gdp*v;
                     nam++;
                     printf("%d  %f\n",nam,gdp);
    }
    getch();
    
}
