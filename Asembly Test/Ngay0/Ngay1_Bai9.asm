; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap chuoi 1: $"
    Str1 db 100, ?, 100 dup(0)
    Mess2 db 0ah, 0dh, "Nhap chuoi 2: $"
    Mess3 db 0ah, 0dh, "Chuoi sau khi ghep la: $"
    Str2 db 100, ?, 100 dup(0)
    Str3 db 200, ?, 200 dup(0)
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

    ;In Mess1        
    lea dx, Mess1
    mov ah, 9
    int 21h
    
    ;Nhap Str1
    mov dx, offset Str1
    mov ah, 10
    int 21h
    
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    ;Nhap Str2
    mov dx, offset Str2
    mov ah, 10
    int 21h
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    
    ;Copy Str1 vao Str3
    xor cx, cx
    mov cl, Str1[1]
    
    xor bx, bx
    Loop1:
    mov dl, Str1[bx+2] 
    mov Str3[bx], dl
    inc bx
    Loop Loop1
    ;Luu vi tri hien tai cua Str3 vao ax
    mov ax, bx
        
    ;Copy Str2 vao Str3
    xor cx, cx
    mov cl, Str2[1]
    
    xor bx, bx
    Loop2:
    mov dl, Str2[bx+2]
    add bx, ax
    mov Str3[bx], dl
    sub bx, ax
    inc bx
    Loop Loop2
    
    ;Them ki tu ket thuc cho Str3
    add bx, ax
    mov Str3[bx], '$'
	
    ;In Str1
    mov dx, offset Str3
    mov ah, 9
    int 21h
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h

    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
