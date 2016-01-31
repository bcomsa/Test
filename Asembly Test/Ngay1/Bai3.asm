; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap lenh: $"
    Mess2 db 0ah, 0dh, "Nhap xau: $"
    Mess3 db 0ah, 0dh, "Nhap sai!$"
    Mess4 db 0ah, 0dh, "Chuoi nhap vao la so!$"
    Mess5 db 0ah, 0dh, "Chuoi nhap vao ko la so!$"
    Mess6 db 0ah, 0dh, "Chuoi ban nhap la so dien thoai$"
    Mess7 db 0ah, 0dh, "Chuoi ban nhap ko la so dien thoai$"
    Mess8 db 0ah, 0dh, "Chuoi sau khi sap xep la: $"
    Str1 db 100, ?, 100 dup(0)
    Str2 db 100, ?, 100 dup(0)    
    Count db 0
    
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
    
    cmp KyTu, 'i'
    je CallFunc1
    cmp KyTu, 'I'
    je CallFunc1
    cmp KyTu, 'n'
    je CallFunc2
    cmp KyTu, 'N'
    je CallFunc2
    cmp KyTu, 'm'
    je CallFunc3
    cmp KyTu, 'M'
    je CallFunc3
    cmp KyTu, 's'
    je CallFunc4
    cmp KyTu, 'S'
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

Func1 PROC
    push dx
    push ax
    push bx
    push dx
    
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h 
    
    ;Nhap Str1
    mov dx, offset Str1
    mov ah, 10
    int 21h
    ;Them ki tu ket thuc $ vao cuoi Str1
    xor bx, bx
    mov bl, Str1[1]
    mov Str1[bx+2], '$'
    
    pop dx
    pop bx
    pop ax
    pop dx   
    ret
Func1 ENDP

Func2 PROC  
    push cx
    push ax
    push bx
    push dx
    
    xor cx, cx
    mov cl, Str1[1]
    mov bx, 2     
    
    ;Lap tung ki tu trong Str neu co ki tu nao k phai la so thi
    ;Sua lai xuat ra Mess3 k phai Mess2 nua
    loop2:
    cmp Str1[bx], '0'
    jl  Skip1:
    cmp Str1[bx], '9'
    jg  Skip1:
    inc bx
    loop loop2    
    
    ;In ra Mess4
    lea dx, Mess4
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
    
    Skip1:
    
    ;In ra Mess5
    lea dx, Mess5
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
Func2 ENDP

Func3 PROC
    push cx
    push ax
    push bx
    push dx
    
    ;Do theo fomart tung ki tu
    ;4 ki tu so dau
    cmp Str1[2], '0'
    jl  Skip2:
    cmp Str1[2], '9'
    jg  Skip2:    

    cmp Str1[3], '0'
    jl  Skip2:
    cmp Str1[3], '9'
    jg  Skip2:    
    
    cmp Str1[4], '0'
    jl  Skip2:
    cmp Str1[4], '9'
    jg  Skip2:    
    
    cmp Str1[5], '0'
    jl  Skip2:
    cmp Str1[5], '9'
    jg  Skip2:    
    
    cmp Str1[6], '-'
    jl  Skip2:
    
    cmp Str1[7], '0'
    jl  Skip2:
    cmp Str1[7], '9'
    jg  Skip2:    
    
    cmp Str1[8], '0'
    jl  Skip2:
    cmp Str1[8], '9'
    jg  Skip2:    
    
    cmp Str1[9], '0'
    jl  Skip2:
    cmp Str1[9], '9'
    jg  Skip2:    
    
    cmp Str1[10], '-'
    jl  Skip2:
    
    cmp Str1[11], '0'
    jl  Skip2:
    cmp Str1[11], '9'
    jg  Skip2:    
    
    cmp Str1[12], '0'
    jl  Skip2:
    cmp Str1[12], '9'
    jg  Skip2:    
    
    cmp Str1[13], '0'
    jl  Skip2:
    cmp Str1[13], '9'
    jg  Skip2:    
    
    cmp Str1[14], '$'
    jne  Skip2:
    
    ;In ra Mess6
    lea dx, Mess6
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
    
    Skip2:
    
    ;In ra Mess7
    lea dx, Mess7
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
Func3 ENDP

Func4 PROC
    push ax
    push bx
    push cx
    push dx
    
    xor ax, ax
    xor bx, bx
    xor cx, cx
    xor dx, dx
    
    mov KyTu, 0
    Loop3:
        mov cl, Str1[1]
        Loop4:
        mov bl, cl
        mov al, Str1[bx+1]
        cmp al, KyTu
        jne Skip3
            mov dl, Str1[bx+1]
            push bx
            mov bl, Count
            mov Str2[bx], dl
            inc Count
            pop bx
        Skip3:
        Loop Loop4
    inc KyTu
    cmp KyTu, 255
    jg Loop3 
    
    ;Gan tra lai Str1
    xor bx, bx
    xor cx, cx
    xor dx, dx  
    mov cl, Str1[1]
    Loop5:
        mov bl, cl
        mov dl ,Str2[bx-1]
        mov Str1[bx+1], dl    
    Loop Loop5
    
    ;In Mess8        
    lea dx, Mess8
    mov ah, 9
    int 21h 
    
    ;In chuoi da dc sap xep
    mov dx, offset Str1 + 2
    mov ah, 9
    int 21h
        
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func4 ENDP

Func5 PROC
   
    ret
Func5 ENDP

end start ; set entry point and stop the assembler.
