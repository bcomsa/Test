; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap vao 1-4: $"
    Mess2 db 0ah, 0dh, "Nhap sai!$"
    FileName db "asm.txt", 0
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
    ;In Mess2 (Nhap sai)        
    lea dx, Mess2
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
    push ax
    push cx
    push dx
    
    mov	AH, 43h
    mov	AL, 1
    lea	DX, FileName 
    mov	CX, 2 ;thuoc tinh file an da duoc to hop
    int	21h
    
    pop dx
    pop cx
    pop ax
    ret
Func1 ENDP

Func2 PROC   
    push ax
    push cx
    push dx
    
    mov	AH, 43h
    mov	AL, 1
    lea	DX, FileName 
    mov	CX, 0 ;thuoc tinh nomal
    int	21h
    
    pop dx
    pop cx
    pop ax
    ret
Func2 ENDP

Func3 PROC 
    push ax
    push cx
    push dx
    
    mov	AH, 43h
    mov	AL, 1
    lea	DX, FileName 
    mov	CX, 1 ;thuoc tinh chi doc
    int	21h
    
    pop dx
    pop cx
    pop ax
    ret
Func3 ENDP
end start ; set entry point and stop the assembler.




