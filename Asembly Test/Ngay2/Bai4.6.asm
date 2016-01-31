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
   
    call VeHCNToMau1
    call VeHinhThoiToMau1
    
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
 
VeHCNToMau1 PROC
    push ax
    push bx
    push cx
    push dx
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 0001b
    ;Vi tri Bat Dau
    mov cx, 50    
    mov dx, 60
    mov bx, 60+1
    int 10h
    
    VeHCNToMau1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeHCNToMau1Lap1

    VeHCNToMau1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeHCNToMau1Lap2    

    VeHCNToMau1Lap3:
    dec cx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHCNToMau1Lap3     
    
    VeHCNToMau1Lap4:
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHCNToMau1Lap4     
    
    ;To mau do
    mov al, 0100b
    VeHCNToMau1Lap5:
        mov cx, 50 
        mov dx, bx
        VeHCNToMau1Lap6:
            inc cx
            int 10h
            ;Vi tri ket thuc
            cmp cx, 70-1
        jne VeHCNToMau1Lap6
        inc bx
        cmp bx, 80
    jne VeHCNToMau1Lap5
    
    
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeHCNToMau1 ENDP

VeHinhThoiToMau1 PROC
    push ax
    push bx
    push cx
    push dx
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 0001b
    ;Vi tri Bat Dau
    mov cx, 50    
    mov dx, (60+80)/2
    int 10h
    
    VeHinhThoiToMau1Lap1:
    inc cx
    inc dx
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeHinhThoiToMau1Lap1

    VeHinhThoiToMau1Lap2:
    inc cx
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeHinhThoiToMau1Lap2    

    VeHinhThoiToMau1Lap3:
    dec cx
    dec dx
    int 10h 
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHinhThoiToMau1Lap3     
    
    VeHinhThoiToMau1Lap4:
    dec cx
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHinhThoiToMau1Lap4     
    
    ;To mau xanh
    mov al, 0001b
    xor bx, bx
    dec dx
    VeHinhThoiToMau1Lap5:
        inc cx
        inc dx
        push bx
        push cx
        push dx
        xor bx, bx
        VeHinhThoiToMau1Lap6:
            int 10h
            inc bx
            inc cx
            dec dx
            cmp bx, 9
        jl VeHinhThoiToMau1Lap6
        
        pop dx
        pop cx
        pop bx
        inc bx
        cmp bx, 9
    jl VeHinhThoiToMau1Lap5
    
    ;Vi tri Bat Dau
    mov cx, 50    
    mov dx, (60+80)/2
    xor bx, bx
    dec dx
    inc cx
    VeHinhThoiToMau1Lap7:
        inc cx
        inc dx
        push bx
        push cx
        push dx
        xor bx, bx
        VeHinhThoiToMau1Lap8:
            int 10h
            inc bx
            inc cx
            dec dx
            cmp bx, 9
        jl VeHinhThoiToMau1Lap8
        
        pop dx
        pop cx
        pop bx
        inc bx
        cmp bx, 9
    jl VeHinhThoiToMau1Lap7    
    
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeHinhThoiToMau1 ENDP

end start ; set entry point and stop the assembler.
