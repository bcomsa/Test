; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap vao 1-6: $"
    Mess2 db 0ah, 0dh, "Chuoi nhap vao la so!$"
    Mess3 db 0ah, 0dh, "Chuoi nhap vao ko la so!$"
    Mess4 db 0ah, 0dh, "Nhap sai!$"
    Mess5 db 0ah, 0dh, "Xin moi nhap chuoi: $"
    Mess6 db 0ah, 0dh, "Chuoi ban nhap la: $"
    Mess7 db 0ah, 0dh, "Chuoi nguoc chuoi ban nhap la: $"
    Mess8 db 0ah, 0dh, "Da IN HOA chuoi cua ban$"
    
    Str1 db 100, ?, 100 dup(0)
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
    
    cmp KyTu, '1'
    je CallFunc1
    cmp KyTu, '2'
    je CallFunc2
    cmp KyTu, '3'
    je CallFunc3
    cmp KyTu, '4'
    je CallFunc4
    cmp KyTu, '5'
    je CallFunc5
    cmp KyTu, '6'
    je KetThuc:
    ;In Mess4 (Nhap sai)        
    lea dx, Mess4
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
    
    ;In Mess5        
    lea dx, Mess5
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
    push dx
    push ax
    
    ;In Mess6        
    lea dx, Mess6
    mov ah, 9
    int 21h 
    
    ;In Str1
    mov dx, offset Str1 + 2
    mov ah, 9
    int 21h
    
    pop ax
    pop dx
    ret
Func2 ENDP

Func3 PROC
    push cx
    push ax
    push dx
    
    ;In Mess7        
    lea dx, Mess7
    mov ah, 9
    int 21h 
    
    xor cx, cx
    mov cl, Str1[1]
    mov bx, cx
    add bx, 2
    
    loop2:
    mov ah, 2
    dec bx
    mov dl, Str1[bx]
    int 21h
    loop loop2
    
    pop dx
    pop ax
    pop cx
    ret
Func3 ENDP

Func4 PROC
    push cx
    push ax
    push bx
    push dx
    
    ;In Mess8        
    lea dx, Mess8
    mov ah, 9
    int 21h 
    
    
    xor cx, cx
    mov cl, Str1[1]
    mov bx, 2
    
    loop3:
    cmp Str1[bx], 'a'
    jl  Skip1
    cmp Str1[bx], 'z'
    jg  Skip1
    Sub Str1[bx], 20h
    Skip1:
    inc bx
    loop loop3
    Call Func2
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
Func4 ENDP

Func5 PROC
    push cx
    push ax
    push bx
    push dx
    
    xor cx, cx
    mov cl, Str1[1]
    mov bx, 2     
    
    ;Lap tung ki tu trong Str neu co ki tu nao k phai la so thi
    ;Sua lai xuat ra Mess3 k phai Mess2 nua
    loop4:
    cmp Str1[bx], '0'
    jl  Skip2:
    cmp Str1[bx], '9'
    jg  Skip2:
    inc bx
    loop loop4    
    
    ;In ra Mess2
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
    
    Skip2:
    
    ;In ra Mess3
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    pop cx
    ret
Func5 ENDP

end start ; set entry point and stop the assembler.
