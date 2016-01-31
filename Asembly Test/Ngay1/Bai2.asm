; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap vao 1-4: $"
    
    Mess2 db 0ah, 0dh, "Nhap chuoi 1: $"
    Str1 db 100, ?, 100 dup(0)
    Mess3 db 0ah, 0dh, "Nhap chuoi 2: $"
    Mess4 db 0ah, 0dh, "Nhap sai nhap lai. $"
    Mess5 db 0ah, 0dh, "Chuoi 1 la: $"
    Mess6 db 0ah, 0dh, "Chuoi 2 la: $"
    Mess7 db 0ah, 0dh, "Chuoi sau khi ghep la: $"
    
    ;Mess4 db 0ah, 0dh, "Chuoi sau khi ghep la: $"
    Str2 db 100, ?, 100 dup(0)
    Str3 db 200, ?, 200 dup(0)    
    
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
    
    KetThuc:    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

Func1 PROC
    push dx
    push ax
    
    xor ax, ax
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    ;Nhap Str1
    mov dx, offset Str1
    mov ah, 10
    int 21h
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    ;Nhap Str2
    mov dx, offset Str2
    mov ah, 10
    int 21h
    
    pop dx
    pop ax
    ret
Func1 ENDP

Func2 PROC
    push ax
    push bx
    push dx
    
    ;In Mess5        
    lea dx, Mess5
    mov ah, 9
    int 21h
    
    ;In Str1
    xor bx, bx
    mov bl, Str1[1]
    mov Str1[bx+2], '$'
    mov dx, offset Str1 + 2
    mov ah, 9
    int 21h
    
    ;In Mess6        
    lea dx, Mess6
    mov ah, 9
    int 21h
    
    ;In Str2
    xor bx, bx
    mov bl, Str2[1]
    mov Str2[bx+2], '$'
    mov dx, offset Str2 + 2
    mov ah, 9
    int 21h
    
    pop dx
    pop bx
    pop ax
    ret
Func2 ENDP

Func3 PROC
    push ax
    push bx
    push cx
    push dx
    
    ;Copy Str1 vao Str3
    xor cx, cx
    mov cl, Str1[1]
    
    xor bx, bx
    Loop2:
    mov dl, Str1[bx+2] 
    mov Str3[bx], dl
    inc bx
    Loop Loop2
    ;Luu vi tri hien tai cua Str3 vao ax
    mov ax, bx
        
    ;Copy Str2 vao Str3
    xor cx, cx
    mov cl, Str2[1]
    
    xor bx, bx
    Loop3:
    mov dl, Str2[bx+2]
    add bx, ax
    mov Str3[bx], dl
    sub bx, ax
    inc bx
    Loop Loop3
    
    ;Them ki tu ket thuc cho Str3
    add bx, ax
    mov Str3[bx], '$'
	
	;In Mess7        
    lea dx, Mess7
    mov ah, 9
    int 21h 
	
    ;In Str3
    mov dx, offset Str3
    mov ah, 9
    int 21h
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func3 ENDP

end start ; set entry point and stop the assembler.
