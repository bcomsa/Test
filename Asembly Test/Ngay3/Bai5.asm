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
    cmp bx, 3
    je  KetThuc
    
    jmp BatTrangThaiChuot
    
    ChuotTrai:
	call VeTamGiacVuongCan1
    jmp BatTrangThaiChuot
    
    ChuotPhai:
	call VeHCN1
    jmp BatTrangThaiChuot
    
    KetThuc:
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
    
    call ThietLapDoHoa
    
    ;(50, 60) - (80, 100)
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
    cmp cx, 80
    jne VeHCN1Lap1

    VeHCN1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 100
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

VeTamGiacVuongCan1 PROC
    push ax
    push cx
    push dx
    
    call ThietLapDoHoa
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 0100b
    ;Vi tri Bat Dau
    mov cx, 50
    mov dx, 60
    int 10h
    
    VeTamGiacVuongCan1Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 70
    jne VeTamGiacVuongCan1Lap1

    VeTamGiacVuongCan1Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 80
    jne VeTamGiacVuongCan1Lap2    

    VeTamGiacVuongCan1Lap3:
    dec cx
    dec dx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeTamGiacVuongCan1Lap3
     
    pop dx
    pop cx
    pop ax
    ret
VeTamGiacVuongCan1 ENDP
end start ; set entry point and stop the assembler.
