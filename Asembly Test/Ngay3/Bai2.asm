; multi-segment executable file template.

data segment
    Mess2 db 0ah, 0dh, "Nhap chuoi 1: $"
    Str1 db 100, ?, 100 dup(0)
    Mess3 db 0ah, 0dh, "Nhap chuoi 2: $"    
    Str2 db 100, ?, 100 dup(0)
    Str3 db 200, ?, 200 dup('$')
    NewLine db 0ah, 0dh, "Chuoi dc nhap la: $"
    
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
    
    ;Nhap sau 
    Call Func1
    
    ;Khoi tao String 3 rong
    mov Str3[0], '$'
     
    ;Khoi tao chuot
    mov ax, 00
    int 33h
    
    mov ax, 01; hien chuot
    int 33h
    
    BatTrangThaiChuot:
    mov ax, 03
    int 33h
    
    cmp bx, 1
    je  ChuotTrai
    cmp bx, 2
    je  ChuotPhai
    cmp bx, 3
    je  KetThuc
    
    jmp BatTrangThaiChuot
    
    ChuotTrai:
    call Func3
    jmp BatTrangThaiChuot
    
    ChuotPhai:
    call Func4
    jmp BatTrangThaiChuot
    
    KetThuc:
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

Func1 PROC
    push dx
    push ax
    
    xor ax, ax
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    ;Nhap Str1
    mov dx, offset Str1
    mov ah, 10
    int 21h
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    ;Nhap Str2
    mov dx, offset Str2
    mov ah, 10
    int 21h
    
    pop dx
    pop ax
    ret
Func1 ENDP

Func3 PROC
    push ax
    push bx
    push cx
    push dx
    
    ;Copy Str1 vao Str3
    xor cx, cx
    mov cl, Str1[1]
    
    xor bx, bx
    Loop2:
    mov dl, Str1[bx+2] 
    mov Str3[bx], dl
    inc bx
    Loop Loop2
    ;Luu vi tri hien tai cua Str3 vao ax
    mov ax, bx
        
    ;Copy Str2 vao Str3
    xor cx, cx
    mov cl, Str2[1]
    
    xor bx, bx
    Loop3:
    mov dl, Str2[bx+2]
    add bx, ax
    mov Str3[bx], dl
    sub bx, ax
    inc bx
    Loop Loop3
    
    ;Them ki tu ket thuc cho Str3
    add bx, ax
    mov Str3[bx], '$'
	
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func3 ENDP

Func4 PROC
    push ax
    push dx 
	
	;Xuong Dong
	mov dx, offset NewLine
    mov ah, 9
    int 21h
    ;In Str3
    mov dx, offset Str3
    mov ah, 9
    int 21h
    
    pop dx
    pop ax
    ret
Func4 ENDP


end start ; set entry point and stop the assembler.
