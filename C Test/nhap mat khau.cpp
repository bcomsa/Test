	

    #include <iostream>
     
    #include <conio.h>
     
    using namespace std;
     
    void getpassword(char s[], int size)//Nha^.p ma^.t kha^?u da.ng da^'u *
     
    {
     
    char ch=0;
     
    memset(s,0,size);
     
    fflush(stdin);
     
    while (ch!=13)//ch kh�c Enter
     
    {
     
    fflush(stdin);
     
    ch=getch();
     
    if (ch<=0)
     
    getch();//Loa.i bo? k� c�c tu+. �ie^`u khie^?n
     
    else if (ch>31 && ch<127)//C�c k� tu+. ASCII in ��o+.c
     
    {
     
    if (int(strlen(s))<size-1) //Ne^'u chuo^~i ch�a �a^`y
     
    {
     
    cout<<'*';
     
    s[strlen(s)]=ch;
     
    }
     
    }
     
    else if (ch==8)//X�a mo^.t k� tu+.
     
    if (s[0])//Ne^'u chuo^~i kh�c ro^~ng
     
    {
     
    s[strlen(s)-1]=0;//Xo� k� tu+. cuo^'i c�ng cu?a chuo^~i
     
    cout<<ch<<' '<<ch;//Xo� mo^.t k� tu+. tr�o+'c �� tr�n m�n hi`nh
     
    }
     
    }
     
    cout<<endl;
     
    fflush(stdin);
     
    }
     
    int main()
     
    {
     
    char s[50];
     
    cout<<"Nhap mat khau: ";
     
    getpassword(s,7);
     
    cout<<"Mat khau ban nhap la: "<<s;
    
    cout<<endl<<strlen(s);
    
    getch();
    return 0;
    }

/*void getpassword(char s[], int size)//chuong trinh mat khau dau * 
     
{
     
    char ch=0;
     
    memset(s,0,size);
     
    fflush(stdin);
     
    while (ch!=13)//ch kh�c Enter
     
    {
     
    fflush(stdin);
     
    ch=getch();
     
    if (ch<=0)
     
    getch();// loai bo cac ki tu dieu khien
     
    else if (ch>31 && ch<127)//in cac ki tu ascii
     
    {
     
    if (int(strlen(s))<size-1) //neu chuoi chua day
     
    {
     
    printf("*");;
     
    s[strlen(s)]=ch;
     
    }
     
    }
     
    else if (ch==8)//backspace.
     
    if (s[0])//neu chuoi khac rong
     
    {
     
    s[strlen(s)-1]=0;//xoa ki tu cuoi cung
     
	printf("%c ",ch); // |   xoa ki tu truoc do tren man hinh 
	printf("%c",ch); //  |
	     
    }
     
    }
     
    printf("\n");
     
    fflush(stdin);
     
}*/