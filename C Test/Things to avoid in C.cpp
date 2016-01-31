#include <stdio.h>

int main()
{
    char  b1[] = "ABCD";
    char  b2[] = "LMNO";
    char  b3[] = "ZYXW";
    
    puts(b1);
    puts(b2);
    puts(b3);
    putchar('\n');
    
    puts("Enter some characters:");
    gets(b2);

    putchar('\n');
    puts(b1);
    puts(b2);
    puts(b3);
    
    return(0);
}
