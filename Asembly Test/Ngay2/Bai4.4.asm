; multi-segment executable file template.

data segment
    Two db 3
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
   
    call VeHCNToMauSocXeo1
    
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

VeHCNToMauSocXeo1 PROC
    push ax
    push bx
    push cx
    push dx
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 1111b
    ;Vi tri Bat Dau
    mov cx, 50    
    mov dx, 60
    mov bx, 60+1
    int 10h
    
    VeHCNToMauSocXeo1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeHCNToMauSocXeo1Lap1

    VeHCNToMauSocXeo1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeHCNToMauSocXeo1Lap2    

    VeHCNToMauSocXeo1Lap3:
    dec cx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHCNToMauSocXeo1Lap3     
    
    VeHCNToMauSocXeo1Lap4:
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHCNToMauSocXeo1Lap4     
    
    ;To mau do
    mov al, 0100b
    VeHCNToMauSocXeo1Lap5:
        mov cx, 50 
        mov dx, bx
        VeHCNToMauSocXeo1Lap6:
            inc cx
                push ax
                    mov ax, cx
                    add ax, dx
                    div Two
                    cmp ah, 1
                    jne  VeHCNToMauSocXeo1Skip1:
                        pop ax
                        int 10h
                        push ax
                    VeHCNToMauSocXeo1Skip1:
                pop ax
            ;Vi tri ket thuc
            cmp cx, 70-1
        jne VeHCNToMauSocXeo1Lap6
        inc bx
        cmp bx, 80
    jne VeHCNToMauSocXeo1Lap5
    
    
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeHCNToMauSocXeo1 ENDP 

end start ; set entry point and stop the assembler.
