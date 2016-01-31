; multi-segment executable file template.

data segment
    ; add your data here!
    Str1 db "Hello", 0ah, 0dh, '$'
    Str2 db "Goodbye", 0ah, 0dh, '$'
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
    je  ChuotTrai
    cmp bx, 2
    je  ChuotPhai
    
    jmp BatTrangThaiChuot
    
    ChuotTrai:
	mov dx, offset Str1
	mov ah, 9
	int 21h
    jmp BatTrangThaiChuot
    
    ChuotPhai:
	mov dx, offset Str2
	mov ah, 9
	int 21h
    jmp BatTrangThaiChuot
    
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends

end start ; set entry point and stop the assembler.
