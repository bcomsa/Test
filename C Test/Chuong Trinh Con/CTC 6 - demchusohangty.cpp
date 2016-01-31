#include <stdio.h>
#include <conio.h>

int docbachuso(long so,int n)
{
    int tram,chuc,donvi;
    char *mang[20]={"khong","mot","hai","ba","bon","nam","sau","bay","tam","chin"};
    tram=so%100;
    donvi=tram%10;
    chuc=tram/10;
    tram=so/100;
    if(tram!=0)
    {
               if(chuc==0&&donvi==0)
               printf("%s tram ",mang[tram]);
               else 
                    if(chuc==0&&donvi!=0)
                    printf("%s tram linh %s ",mang[tram],mang[donvi]);
                    else
                        if(chuc!=0&&donvi==0)
                         if(chuc==1)
                          printf("%s tram muoi ",mang[tram]);
                         else
                          printf("%s tram %s muoi ",mang[tram],mang[chuc]);
                        else
                            if(chuc!=0&&donvi!=0)
                             if(chuc==1)
                              printf("%s tram muoi %s ",mang[tram],mang[donvi]);
                             else
                              printf("%s tram %s muoi %s ",mang[tram],mang[chuc],mang[donvi]);
    }
    else
    if(n==1)
    {
            if(chuc!=0&&donvi!=0)
             if(chuc==1)
              printf("muoi %s ",mang[donvi]);
             else
              printf("%s muoi %s ",mang[chuc],mang[donvi]);
            else
                if(chuc!=0&&donvi==0)
                 if(chuc==1)
                  printf("muoi ");
                 else
                  printf("%s muoi ",mang[chuc]);
                else
                    if(donvi!=0)
                    printf("%s ",mang[donvi]);
    }
    else 
    if(n==2)
    {
            if(chuc!=0&&donvi!=0)
             if(chuc==1)
              printf("khong tram muoi %s ",mang[donvi]);
             else
              printf("khong tram %s muoi %s ",mang[chuc],mang[donvi]);
            else
                if(chuc!=0&&donvi==0)
                 if(chuc==1)
                  printf("khong tram muoi ");
                 else
                  printf("khong tram %s muoi ",mang[chuc]);
                else
                    if(donvi!=0)
                     printf("khong tram linh %s ",mang[donvi]);
    }                           
}
int main()
{
    unsigned long so;
    int ty,trieu,ngan,donvi;
    printf("moi nhap chu so (so nguyen duong cho phep nhap toi hang ty)\n");
    scanf("%d",&so);
    ty=so%1000000000;
    trieu=ty%1000000;
    donvi=trieu%1000;
    ngan=trieu/1000;
    trieu=ty/1000000;
    ty=so/1000000000;
    if(so<1000000000&&so>=1000000)
    {
                     docbachuso(trieu,1);if(trieu!=0) printf("trieu ");
                     docbachuso(ngan,2);if(ngan!=0) printf("ngan ");
                     docbachuso(donvi,2);
    }
    else
        if(so<1000000&&so>=1000)
        {
                     docbachuso(ngan,1);if(ngan!=0) printf("ngan ");
                     docbachuso(donvi,2); 
        }
        else
            if(so<1000)
             if(so==0)
              printf("khong ");
             else
              docbachuso(donvi,1);
            else
            {
                     docbachuso(ty,1);if(ty!=0) printf("ty ");
                     docbachuso(trieu,2);if(trieu!=0) printf("trieu ");
                     docbachuso(ngan,2);if(ngan!=0) printf("ngan ");
                     docbachuso(donvi,2);
            }
    getch();
}
