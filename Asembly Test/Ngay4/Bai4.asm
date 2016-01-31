; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap vao 1-4: $"
    Mess2 db 0ah, 0dh, "Nhap sai!$"
    Mess3 db 0ah, 0dh, "Nhap ten thu muc: $"
    FilePath db 100, ?, 100 dup(0)
    KyTu db 0
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
    
    ;Khoi tao chuot
    mov ax, 00
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
    call Func2
    jmp BatTrangThaiChuot
    
    ChuotPhai:
    jmp KetThuc
    jmp BatTrangThaiChuot
    
    KetThuc:    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

Func1 PROC
    push ax
    push bx
    push dx
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h 
    
    ;Nhap FilePath
    mov dx, offset FilePath
    mov ah, 10
    int 21h
    
    ;Them ki tu ket thuc 00h vao cuoi Str1
    xor bx, bx
    mov bl, FilePath[1]
    mov FilePath[bx+2], 0
    
    pop dx
    pop bx
    pop ax
    ret
Func1 ENDP

Func2 PROC   
    push ax
    push cx
    push dx
    
    call Func1
    
    
    mov dx, offset FilePath + 2
    mov ah, 39h
    int 21h
    
    pop dx
    pop cx
    pop ax
    ret
Func2 ENDP
end start ; set entry point and stop the assembler.




