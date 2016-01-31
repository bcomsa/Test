	

    #include <iostream>
     
    #include <conio.h>
     
    using namespace std;
     
    void getpassword(char s[], int size)//Nha^.p ma^.t kha^?u da.ng da^'u *
     
    {
     
    char ch=0;
     
    memset(s,0,size);
     
    fflush(stdin);
     
    while (ch!=13)//ch khác Enter
     
    {
     
    fflush(stdin);
     
    ch=getch();
     
    if (ch<=0)
     
    getch();//Loa.i bo? kí các tu+. ðie^`u khie^?n
     
    else if (ch>31 && ch<127)//Các kí tu+. ASCII in ðýo+.c
     
    {
     
    if (int(strlen(s))<size-1) //Ne^'u chuo^~i chýa ða^`y
     
    {
     
    cout<<'*';
     
    s[strlen(s)]=ch;
     
    }
     
    }
     
    else if (ch==8)//Xóa mo^.t kí tu+.
     
    if (s[0])//Ne^'u chuo^~i khác ro^~ng
     
    {
     
    s[strlen(s)-1]=0;//Xoá kí tu+. cuo^'i cùng cu?a chuo^~i
     
    cout<<ch<<' '<<ch;//Xoá mo^.t kí tu+. trýo+'c ðó trên màn hi`nh
     
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
     
    while (ch!=13)//ch khác Enter
     
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