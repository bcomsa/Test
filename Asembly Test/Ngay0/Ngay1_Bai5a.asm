; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap chuoi cua ban: $"
    Mess2 db 0ah, 0dh, "Chuoi IN HOA la: $"
    Str1 db 100, ?, 100 dup(0)
ends

stack segment
    dw   512  dup(0)
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
    
    ;Cho nhap 1 ki tu roi bo vao stack cho den khi nhan nut enter
    xor bx, bx   
    Lap1:
    mov ah, 1
    int 21h
    cmp al, 'a'
    jl  Skip2:
    cmp al, 'z'
    jg  Skip2:
    sub al, 20h
    Skip2:              
    mov Str1[bx], al
    inc bx
    cmp al, 0dh
    jne Lap1
    
    Skip1:
    mov Str1[bx], '$'
    
    
    ;In Mess2         
    lea dx, Mess2
    mov ah, 9
    int 21h 
    
    ;In Str1         
    lea dx, Str1
    mov ah, 9
    int 21h    
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h    
    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
