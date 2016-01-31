; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Ten: Le An$"
    Mess2 db 0ah, 0dh, "Tuoi: 20$"
    Mess3 db 0ah, 0dh, "Lop: AT9d$"
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
                   
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h   

    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    ;Cho de ket thuc    
    mov ah, 1
    int 21h

    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

end start ; set entry point and stop the assembler.
