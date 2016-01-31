; multi-segment executable file template.

data segment
    ; add your data here!
    pkey db "press any key...$"
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
    
    mov ax, 01; hien chuot
    int 33h
    
    BatTrangThaiChuot:
    mov ax, 03
    int 33h
    
    cmp bx, 1
    je  BatChuong1
    cmp bx, 2
    je  BatChuong2
    
    jmp BatTrangThaiChuot
    
    BatChuong1:
    mov dl, 7
    mov ah, 02
    int 21h
    jmp BatTrangThaiChuot
    
    BatChuong2:
    mov dl, 7
    mov ah, 02
    int 21h
    int 21h
    jmp BatTrangThaiChuot
    
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends

end start ; set entry point and stop the assembler.
