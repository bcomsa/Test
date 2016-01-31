; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap ten cua ban: $"
    Str1 db 100, ?, 100 dup(0)
    Mess2 db 0ah, 0dh, "Hello, $"
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
   
    ;Them ki tu ket thuc $ vao cuoi Str1
    xor bx, bx
    mov bl, Str1[1]
    mov Str1[bx+2], '$'
	
    ;In Str1
    mov dx, offset Str1 + 2
    mov ah, 9
    int 21h
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h

    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
