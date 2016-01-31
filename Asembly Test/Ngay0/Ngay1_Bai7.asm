; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap vao 1 ky tu: $"
    Mess2 db 0ah, 0dh, "Ky tu ban nhap la so$"
    Mess3 db 0ah, 0dh, "Ky tu ban nhap khong phai la so$"
    NewLine db 0ah, 0dh, "$"
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
    
    ;Cho nhap 1 ki ty    
    mov ah, 1
    int 21h
    
    ;Mac dinh ky tu k la so
    lea dx, Mess3
    
    ;So sanh neu ky tu dung la so thi thay doi k thi thoi
    cmp al, '0'
    jl Skip1
    cmp al, '9'
    jg Skip1
    lea dx, Mess2
    Skip1:
            
    ;In Mess2 or Mess3 tuy thuoc vao al tro vao dau?        
    mov ah, 9
    int 21h    
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
