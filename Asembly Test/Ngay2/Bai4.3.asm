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
   
    call VeHCNToMauCaro1
    
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

VeHCNToMauCaro1 PROC
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
    int 10h
    
    VeHCNToMauCaro1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeHCNToMauCaro1Lap1

    VeHCNToMauCaro1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeHCNToMauCaro1Lap2    

    VeHCNToMauCaro1Lap3:
    dec cx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHCNToMauCaro1Lap3     
    
    VeHCNToMauCaro1Lap4:
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHCNToMauCaro1Lap4     
    
    ;To mau do
    mov al, 0100b
    
    mov bx, 60+2
    VeHCNToMauCaro1Lap5:
        mov cx, 50 
        mov dx, bx
        VeHCNToMauCaro1Lap6:
            inc cx
            int 10h
            ;Vi tri ket thuc
            cmp cx, 70-1
        jne VeHCNToMauCaro1Lap6
        add bx, 2
        cmp bx, 80
    jl VeHCNToMauCaro1Lap5
    
    
    mov bx, 50+2
    VeHCNToMauCaro1Lap7:
        mov dx, 60 
        mov cx, bx
        VeHCNToMauCaro1Lap8:
            inc dx
            int 10h
            ;Vi tri ket thuc
            cmp dx, 80-1
        jne VeHCNToMauCaro1Lap8
        add bx, 2
        cmp bx, 70
    jl VeHCNToMauCaro1Lap7
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
VeHCNToMauCaro1 ENDP 

end start ; set entry point and stop the assembler.
