; multi-segment executable file template.

data segment
    ; add your data here!
    Two db 2
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
    
    ;Neu chuot nam trong man hinh thi thuc hien tiep
    ;Con k thi quay nguoc lai
    cmp cx, 0
    jl  BatTrangThaiChuot
    cmp cx, 640
    jg  BatTrangThaiChuot
    cmp dx, 0
    jl  BatTrangThaiChuot
    cmp dx, 200
    jg  BatTrangThaiChuot    
    
    mov ax, cx
    div Two
    mov cx, ax
    mov al, 0100b
    mov ah, 0ch
    int 10h
    
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
