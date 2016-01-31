; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap vao 1 so: $"
    Mess2 db 0ah, 0dh, "So ban vua nhap la: $"
    Mess3 db "Loi!!! (Vui long nhap so)$"
    
    NewLine db 0ah, 0dh, "$"  
    
    KyTu0 db "Khong$"
    KyTu1 db "Mot$"
    KyTu2 db "Hai$"
    KyTu3 db "Ba$"
    KyTu4 db "Bon$"
    KyTu5 db "Nam$"
    KyTu6 db "Sau$"
    KyTu7 db "Bay$"
    KyTu8 db "Tam$"
    KyTu9 db "Chin$"
    
    
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
    
    cmp KyTu, '0'
    lea dx, KyTu0
    je Skip1
    cmp KyTu, '1'
    lea dx, KyTu1
    je Skip1
    cmp KyTu, '2'
    lea dx, KyTu2
    je Skip1
    cmp KyTu, '3'
    lea dx, KyTu3
    je Skip1
    cmp KyTu, '4'
    lea dx, KyTu4
    je Skip1
    cmp KyTu, '5'
    lea dx, KyTu5
    je Skip1
    cmp KyTu, '6'
    lea dx, KyTu6
    je Skip1
    cmp KyTu, '7'
    lea dx, KyTu7
    je Skip1
    cmp KyTu, '8'
    lea dx, KyTu8
    je Skip1
    cmp KyTu, '9'
    lea dx, KyTu9
    je Skip1
    lea dx, Mess3
    
    Skip1:
    ;In ky tu vua nhap
    mov ah, 9
    int 21h
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
