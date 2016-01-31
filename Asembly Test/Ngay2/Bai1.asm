; multi-segment executable file template.

data segment
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

    call ThietLapDoHoa 
   
    ;wait for any key....    
    mov ah, 1
    int 21h
   
    call VeDoanThang1
    call VeDoanThang2
    
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

VeDoanThang1 PROC
    push ax
    push cx
    push dx
    
    
    
    mov ah, 0Ch
    ;Mau
    mov al, 1111b
    ;Vi tri Bat Dau
    mov cx, 100
    mov dx, 100
    int 10h
        
    VeDoanThang1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 200
    jne VeDoanThang1Lap1
    
    pop dx
    pop cx
    pop ax
    ret
VeDoanThang1 ENDP

VeDoanThang2 PROC
    push ax
    push cx
    push dx
    
    
    
    mov ah, 0Ch
    ;Mau
    mov al, 1111b
    ;Vi tri Bat Dau
    mov cx, 200
    mov dx, 200
    int 10h
    
    VeDoanThang2Lap1:
    dec cx
    dec dx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 100
    jne VeDoanThang2Lap1
    
    pop dx
    pop cx
    pop ax
    ret
VeDoanThang2 ENDP

end start ; set entry point and stop the assembler.
