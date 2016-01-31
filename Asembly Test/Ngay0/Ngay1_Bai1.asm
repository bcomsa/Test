; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap vao 1 ky tu: $"
    Mess2 db 0ah, 0dh, "Ky tu ban vua nhap la: $"
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

    ;In Mess1        
    lea dx, Mess1
    mov ah, 9
    int 21h        
    
    ;Cho nhap 1 ki ty    
    mov ah, 1
    int 21h
    mov KyTu, al
                   
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h 
    
    ;In ky tu vua nhap
    mov ah, 2
    mov dl, KyTu
    int 21h
    
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
