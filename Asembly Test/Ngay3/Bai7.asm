; multi-segment executable file template.

data segment
    ; add your data here!
    Two dw 2
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
    mov ax, 00h
    int 33h
    
    mov ax, 01h; hien chuot
    int 33h
    
    call ThietLapDoHoa
    
    BatTrangThaiChuot:
    mov ax, 03h
    int 33h
    
    cmp bx, 1h
    je  ChuotTrai
    cmp bx, 2h
    je  ChuotPhai
    
    jmp BatTrangThaiChuot
    
    ChuotTrai:
    shr cx, 1
    ; ham ve
    mov al, 0100b
    mov ah, 0ch
    int 10h
    jmp BatTrangThaiChuot
    
    ChuotPhai:
    jmp BatTrangThaiChuot
    
    
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

end start ; set entry point and stop the assembler.
