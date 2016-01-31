; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap lenh: $"
    Mess3 db 0ah, 0dh, "Nhap sai!$"
    NewLine db 0ah, 0dh, "$"
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
    
    cmp KyTu, 'd'
    je CallFunc1
    cmp KyTu, 'D'
    je CallFunc1
    cmp KyTu, 'v'
    je CallFunc2
    cmp KyTu, 'V'
    je CallFunc2
    cmp KyTu, 'c'
    je CallFunc3
    cmp KyTu, 'C'
    je CallFunc3
    cmp KyTu, 't'
    je CallFunc4
    cmp KyTu, 'T'
    je CallFunc4
    cmp KyTu, 'e'
    je KetThuc:
    cmp KyTu, 'E'
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
    
    CallFunc4:
    call Func4
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
Func1 ENDP

Func2 PROC  
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
Func2 ENDP

Func3 PROC
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
    
    VeHCN2Lap1:
    inc cx
    int 10h
    ;Vi tri ket thuc
    cmp cx, 80
    jne VeHCN2Lap1

    VeHCN2Lap2:
    inc dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 100
    jne VeHCN2Lap2    

    VeHCN2Lap3:
    dec cx
    int 10h 
    ;Vi tri ket thuc
    cmp cx, 50
    jne VeHCN2Lap3     
    
    VeHCN2Lap4:
    dec dx 
    int 10h
    ;Vi tri ket thuc
    cmp dx, 60
    jne VeHCN2Lap4     
    
     
    pop dx
    pop cx
    pop ax
    ret
Func3 ENDP

Func4 PROC
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
Func4 ENDP

Func5 PROC
   
    ret
Func5 ENDP

end start ; set entry point and stop the assembler.
