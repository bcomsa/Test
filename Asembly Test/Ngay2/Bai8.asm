; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap lenh: $"
    Mess3 db 0ah, 0dh, "Nhap sai!$"
    NewLine db 0ah, 0dh, "$"
    Four db 4
    KyTu db 0
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

    
                      
    Loop1:
    ;In Mess1        
    lea dx, Mess1
    mov ah, 9
    int 21h 
    
    ;Cho nhap 1 ki tu    
    mov ah, 1
    int 21h
    mov KyTu, al
    
    cmp KyTu, '1'
    je CallFunc1
    cmp KyTu, '2'
    je CallFunc2
    cmp KyTu, '3'
    je CallFunc3
    cmp KyTu, '4'
    je KetThuc:
    ;In Mess3 (Nhap sai)        
    lea dx, Mess3
    mov ah, 9
    int 21h
    jmp Loop1
    
    CallFunc1:
    call Func1
    jmp Loop1
    
    CallFunc2:
    call Func2
    jmp Loop1
    
    CallFunc3:
    call Func3
    jmp Loop1
    
    CallFunc5:
    call Func5
    jmp Loop1
    
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

Func1 PROC
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
    mov al, 0100b
    int 10h
        ;To mau
        push cx
        inc cx
        VeTamGiacVuongCan1Lap4:
        cmp cx, 70        
        jge VeTamGiacVuongCan1BoQua1
            mov al, 1
            int 10h
            inc cx
        jmp VeTamGiacVuongCan1Lap4:
        VeTamGiacVuongCan1BoQua1:  
        pop cx 
    ;Vi tri ket thuc
    dec cx
    dec dx
    cmp cx, 50
    jne VeTamGiacVuongCan1Lap3
     
    pop dx
    pop cx
    pop ax
    ret
Func1 ENDP

Func2 PROC  
    push ax
    push bx
    push cx
    push dx
    
    call ThietLapDoHoa
    
    ;(50, 60) - (70, 80)
    mov ah, 0Ch
    mov al, 1
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
    
    push bx
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
                    div Four
                    cmp ah, 0
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
    pop bx
    ;To mau do
    mov al, 0100b
    VeHCNToMauSocXeo1Lap7:
        mov cx, 50 
        mov dx, bx
        VeHCNToMauSocXeo1Lap8:
            inc cx
                push ax
                    mov ax, cx
                    sub ax, dx
                    jns VeHCNToMauSocXeo1Skip4
                    neg ax
                    VeHCNToMauSocXeo1Skip4: 
                    div Four
                    cmp ah, 0
                    jne  VeHCNToMauSocXeo1Skip3:
                        pop ax
                        int 10h
                        push ax
                    VeHCNToMauSocXeo1Skip3:
                pop ax
            ;Vi tri ket thuc
            cmp cx, 70-1
        jne VeHCNToMauSocXeo1Lap8
        inc bx
        cmp bx, 80
    jne VeHCNToMauSocXeo1Lap7
    
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func2 ENDP

Func3 PROC
    push ax
    push bx
    push cx
    push dx
    
    call ThietLapDoHoa
    call Func2
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
    mov al, 0
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
    
    
    mov al, 0
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
    
    mov al, 1
    ;Vi tri Bat Dau
    mov cx, 50    
    mov dx, (60+80)/2
    xor bx, bx
    dec dx
    inc cx
    VeHinhThoiToMau1Lap9:
        inc cx
        inc dx
        inc cx
        inc dx
        push bx
        push cx
        push dx
        xor bx, bx
        VeHinhThoiToMau1Lap10:
            int 10h
            inc bx
            inc cx
            dec dx
            inc cx
            dec dx
            cmp bx, 5
        jl VeHinhThoiToMau1Lap10
        
        pop dx
        pop cx
        pop bx
        inc bx
        cmp bx, 5
    jl VeHinhThoiToMau1Lap9    
    
     
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func3 ENDP



Func5 PROC
   
    ret
Func5 ENDP

end start ; set entry point and stop the assembler.
