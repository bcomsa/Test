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
   
    call VeHCN1
    call VeHCN2
    
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

VeHCN1 PROC
    push ax
    push cx
    push dx
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 0100b
    ;Vi tri Bat Dau
    mov cx, 50
    mov dx, 60
    int 10h
    
    VeHCN1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeHCN1Lap1

    VeHCN1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeHCN1Lap2    

    VeHCN1Lap3:
    dec cx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHCN1Lap3     
    
    VeHCN1Lap4:
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHCN1Lap4     
    
     
    pop dx
    pop cx
    pop ax
    ret
VeHCN1 ENDP 

VeHCN2 PROC
    push ax
    push cx
    push dx
    
    ;(53, 63) - (67, 77)
    mov ah, 0Ch
    mov al, 0001b
    ;Vi tri Bat Dau
    mov cx, 53
    mov dx, 63
    int 10h
    
    VeHCN2Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 67
    jne VeHCN2Lap1

    VeHCN2Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 77
    jne VeHCN2Lap2    

    VeHCN2Lap3:
    dec cx 
    int 10h
    ;Vi tri ket thuc
    cmp cx, 53
    jne VeHCN2Lap3     
    
    VeHCN2Lap4:
    dec dx
    int 10h 
    ;Vi tri ket thuc
    cmp dx, 63
    jne VeHCN2Lap4     
    
     
    pop dx
    pop cx
    pop ax
    ret
VeHCN2 ENDP

end start ; set entry point and stop the assembler.
