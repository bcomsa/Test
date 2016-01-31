; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap chuoi cua ban: $"
    Mess2 db 0ah, 0dh, "Chuoi dao nguoc la:", 0ah, 0dh, "$"
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
    
    ;Luu vi tri bat dau chuoi tren stack vao bx
    mov bx, sp
    
    
    ;Cho nhap 1 ki tu roi bo vao stack cho den khi nhan nut enter    
    Lap1:
    mov ah, 1
    int 21h
    cmp al, 0dh
    push ax
    jne Lap1
    
    ;In Mess2         
    lea dx, Mess2
    mov ah, 9
    int 21h 
    
    
    ;Xuat tung ki tu tren stack cho den khi ve vi tri cu (bx)
    Lap2:
    pop ax
    mov ah, 2
    mov dl, al
    int 21h
    cmp bx, sp
    jne Lap2
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h    
    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
