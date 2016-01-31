; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap a: $"
    a db 0
    Mess2 db 0ah, 0dh, "Nhap b: $"
    b db 0
    temp1 dw 0
    temp2 dw 0
    count db 0
ends

stack segment
    dw   128  dup(0)
ends

code segment
start:
; set segment registers:
    mov ax, data
    mov ds, ax
    mov es, ax

    ;In Mess1        
    lea dx, Mess1
    mov ah, 9
    int 21h
    
    ;Nhap a
    mov ah, 1
    int 21h
    sub al, 48
    mov a, al
    
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    ;Nhap b
    mov ah, 1
    int 21h
    sub al, 48
    mov b, al
    
    
    call ThietLapDoHoa
     
    call KeTrucDecac
    
    call VeDuongThang
    
    call VeParapol
    ;Cho de ket thuc    
    mov ah, 1
    int 21h

    mov ax, 4c00h ; exit to operating system.
    int 21h
ends  

VeParapol PROC
    push ax
    push bx
    push cx
    push dx
    

    mov count, 0
    ;Vong lap ngoai cung la de noi cac diem roi lai voi nhau
    VeParapolLap2:
        xor bx, bx
        xor cx, cx
        VeParapolLap1:
        ;+ax^2
        xor ax, ax
        cmp cl, 14
        jg  VeParapolLap3
        mov al, cl
        mul cl
        mul a
        jo  VeParapolLap3
        mov dx, ax
        
        ;+c
        mov bl, b
        add dx, bx
        

        
        
        ;Truc toa do nguoc voi Decac nen ta chuyen lai
        ;Dao nguoc y
        neg dx
        ;Chinh truc toa do vao giua man hinh
        add dx, 100
        mov temp1, cx
        add cx, 160
        sub cx, temp1
        sub cx, temp1
        
        ;KT neu nam trong man hinh thi ve tiep k thi ket thuc    
        cmp dx, 0
        jl VeParapolLap3
        cmp dx, 200
        jg VeParapolLap3    
        
        ;Chon ngat ve pixel
        mov ah, 0Ch
        ;Mau
        mov al, 1111b
        ;Vi tri Bat Dau
        int 10h
        ;Ve vi tri that
        add cx, temp1
        add cx, temp1
        sub cx, 160
        
        
        inc cx
        jmp VeParapolLap1
        VeParapolLap3:
        cmp ax, ax
    jne VeParapolLap2
    
        mov count, 0
    ;Vong lap ngoai cung la de noi cac diem roi lai voi nhau
    VeParapolLap5:
        xor bx, bx
        xor cx, cx
        VeParapolLap4:
        ;+ax^2
        xor ax, ax
        cmp cl, 14
        jg  VeParapolLap6
        mov al, cl
        mul cl
        mul a
        jo  VeParapolLap6
        mov dx, ax
        
        ;+c
        mov bl, b
        add dx, bx
        

        
        
        ;Truc toa do nguoc voi Decac nen ta chuyen lai
        ;Dao nguoc y
        neg dx
        ;Chinh truc toa do vao giua man hinh
        add dx, 100
        add cx, 160
        
        ;KT neu nam trong man hinh thi ve tiep k thi ket thuc    
        cmp dx, 0
        jl VeParapolLap6
        cmp dx, 200
        jg VeParapolLap6    
        
        ;Chon ngat ve pixel
        mov ah, 0Ch
        ;Mau
        mov al, 1111b
        ;Vi tri Bat Dau
        int 10h
        ;Ve vi tri that
        sub cx, 160
        
        
        inc cx
        jmp VeParapolLap4
        VeParapolLap6:
        cmp ax, ax
    jne VeParapolLap5
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeParapol ENDP 

ThietLapDoHoa PROC
    push ax
    
    mov ah, 00h
    mov al, 13h
    int 10h
    
    pop ax
    ret
ThietLapDoHoa ENDP

KeTrucDecac PROC
    push ax
    push cx
    push dx
    
    
    
    mov ah, 0Ch
    ;Mau
    mov al, 1
    ;Vi tri Bat Dau
    mov cx, 160
    mov dx, 0
    int 10h
        
    KeTrucDecacLap1:
    inc dx
    int 10h
    ;Vi tri ket thuc
    cmp dx, 200
    jne KeTrucDecacLap1
    
    ;Vi tri Bat Dau
    mov cx, 0
    mov dx, 100
    int 10h
        
    KeTrucDecacLap2:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 320
    jne KeTrucDecacLap2
    
    pop dx
    pop cx
    pop ax
    ret
KeTrucDecac ENDP 


VeDuongThang PROC
    push ax
    push bx
    push cx
    push dx
    
    mov bl, b
    push bx
    
    mov count, 0
    ;Vong lap ngoai cung la de noi cac diem roi lai voi nhau
    VeDuongThangLap5:
        xor bx, bx
        inc b
        xor bx, bx
        xor cx, cx
        VeDuongThangLap4:
        ;y = ax
        xor ax, ax
        mov al, a
        mul cl
        mov dx, ax
        
        ;+b
        mov bl, b
        add dx, bx
        
        ;Truc toa do nguoc voi Decac nen ta chuyen lai
        ;Dao nguoc y
        neg dx
        ;Chinh truc toa do vao giua man hinh
        add dx, 101
        add cx, 160
        
        ;KT neu nam trong man hinh thi ve tiep k thi ket thuc    
        cmp dx, 0
        jl VeDuongThangLap6
        cmp dx, 200
        jg VeDuongThangLap6    
        cmp cx, 0
        jl VeDuongThangLap6
        cmp cx, 320
        jg VeDuongThangLap6
                
        ;Chon ngat ve pixel
        mov ah, 0Ch
        ;Mau
        mov al, 1111b
        ;Vi tri Bat Dau
        int 10h
        ;Tra ve toa do that
        sub cx, 160
        inc cx
        jmp VeDuongThangLap4
        VeDuongThangLap6:
        inc count
        mov bl, a
        cmp count, bl
    jl VeDuongThangLap5
    
    pop bx
    mov b ,bl
    push bx
    
    mov count, 0
    ;Vong lap ngoai cung la de noi cac diem roi lai voi nhau
    VeDuongThangLap2:
        xor bx, bx
        xor cx, cx
        VeDuongThangLap1:
        xor dx, dx
        ;y = ax
        xor ax, ax
        mov al, a
        mul cl
        sub dx, ax
        
        ;+b
        mov bl, b
        sub dx, bx
        
        ;Truc toa do nguoc voi Decac nen ta chuyen lai
        ;Dao nguoc y
        neg dx
        ;Chinh truc toa do vao giua man hinh 
        add dx, 99
        sub dl, b
        sub dl, b
        add dl, 2
        mov temp1, cx
        add cx, 159
        sub cx, temp1
        sub cx, temp1
        ;KT neu nam trong man hinh thi ve tiep k thi ket thuc    
        cmp dx, 0
        jl VeDuongThangLap3
        cmp dx, 200
        jg VeDuongThangLap3    
        cmp cx, 0
        jl VeDuongThangLap3
        cmp cx, 320
        jg VeDuongThangLap3
                
        ;Chon ngat ve pixel
        mov ah, 0Ch
        ;Mau
        mov al, 1111b
        ;Vi tri Bat Dau
        int 10h
        
        
        
        ;Tra ve toa do that
        sub dl, 2
        add dl, b
        add dl, b
        add cx, temp1
        add cx, temp1
        sub cx, 159
        inc cx
        jmp VeDuongThangLap1
        VeDuongThangLap3:
        dec b
        inc count
        mov bl, a
        cmp count, bl
    je VeDuongThangLap2

    pop bx
    mov b ,bl
   
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeDuongThang ENDP
    

end start ; set entry point and stop the assembler.
