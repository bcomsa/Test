; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap a: $"
    a db 0
    Mess2 db 0ah, 0dh, "Nhap b: $"
    b db 0
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
     
    call VeDuongThang
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h

    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

ThietLapDoHoa PROC
    push ax
    
    mov ah, 00h
    mov al, 13h
    int 10h
    
    pop ax
    ret
ThietLapDoHoa ENDP


VeDuongThang PROC
    push ax
    push bx
    push cx
    push dx
    

    mov count, 0
    ;Vong lap ngoai cung la de noi cac diem roi lai voi nhau
    VeDuongThangLap2:
        xor bx, bx
        inc b
        xor bx, bx
        xor cx, cx
        VeDuongThangLap1:
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
        ;Ha truc toa do xuong 199 don vi (tu` 0 -> 199)
        add dx, 199
        
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
        
        inc cx
        jmp VeDuongThangLap1
        VeDuongThangLap3:
        inc count
        mov bl, a
        cmp count, bl
    jl VeDuongThangLap2
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeDuongThang ENDP    

end start ; set entry point and stop the assembler.
