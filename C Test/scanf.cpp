#include <stdio.h>
#include <conio.h>
 
 
int main()
{
    char xau[100];
    //cau 1
    //scanf("%[^\n]",xau);
 
    //cau 2
    //scanf("%[^\0]",xau);
 
    //cau 3
    scanf("%[^0-9]",xau);
 
    //cau 4
    //scanf("%[a-z8*^ ]",xau);
    //scanf("%[^^]",xau);
 
    //cau 5
    //scanf("%[]",xau);
    printf("%s",xau);
    getch();
}