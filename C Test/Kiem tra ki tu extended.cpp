#include <stdio.h>
#include <conio.h>

int main()
{
    int c;
    int extended =0;
    c=getch();
    if(!c)
          extended = getch();
    if(extended)
    printf("la extended\n");
    else
    printf("ko la extended\n";
    getch();
}
