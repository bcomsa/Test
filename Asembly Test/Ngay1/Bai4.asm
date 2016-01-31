; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap so thap phan 2 chu so: $"
    Mess2 db 0ah, 0dh, "Chuyen sang co so 2: $"
    Mess3 db 0ah, 0dh, "Chuyen sang co so 8: $" 
    Mess4 db 0ah, 0dh, "Chuyen sang co so 16: $"
    Str1 db 100, ?, 100 dup(0)
    Num db 0
    Two db 2
    Eight db 8
    Sixteen db 16
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
    
    Call ReadString
    Call StringToInt
    
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h 
    
    Call PrintBin
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h 
    
    Call PrintOct
    
    ;In Mess4        
    lea dx, Mess4
    mov ah, 9
    int 21h
    
    Call PrintHex
    
    
    ;Cho ket thuc
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends

ReadString PROC
    push ax
    push bx
    push dx
    
    ;Nhap Str1
    mov dx, offset Str1
    mov ah, 10
    int 21h
    ;Them ki tu ket thuc $ vao cuoi Str1
    xor bx, bx
    mov bl, Str1[1]
    mov Str1[bx+2], '$'
    
    pop dx
    pop bx
    pop ax
    ret
ReadString ENDP

StringToInt PROC
    push ax
    push bx
    
    xor ax, ax
    mov bx, 10
    mov al ,Str1[2]
    sub ax, 48
    mul bx
    
    mov bl, Str1[3]
    sub ax, 48
    add ax, bx
    mov Num, al
    
    pop bx
    pop ax
    ret
StringToInt ENDP

PrintBin PROC
    push ax
    push bx
    push dx
    
    
    xor bx, bx
    mov bl, Num
    
    mov dx, sp
    
    
    PrintBinLap1:
    mov ax, bx
    div Two
    mov bl, al
    push ax
    
    cmp bx, 0
    jne PrintBinLap1
    
    
    PrintBinLap2:
        pop ax
    	push dx
    	    mov dl, '0'
        	add dl, ah
        	mov ah, 2
        	int 21h
    	pop dx	
    cmp dx, sp
    jne PrintBinLap2
    
    
    pop dx
    pop bx
    pop ax
    ret
PrintBin ENDP

PrintOct PROC
    push ax
    push bx
    push dx
    
    
    xor bx, bx
    mov bl, Num
    
    mov dx, sp
    
    
    PrintOctLap1:
    mov ax, bx
    div Eight
    mov bl, al
    push ax
    
    cmp bx, 0
    jne PrintOctLap1
    
    
    PrintOctLap2:
        pop ax
    	push dx
    	    mov dl, '0'
        	add dl, ah
        	mov ah, 2
        	int 21h
    	pop dx	
    cmp dx, sp
    jne PrintOctLap2
    
    
    pop dx
    pop bx
    pop ax
    ret
PrintOct ENDP

PrintHex PROC
    push ax
    push bx
    push dx
    
    
    xor bx, bx
    mov bl, Num
    
    mov dx, sp
    
    
    PrintHexLap1:
    mov ax, bx
    div Sixteen
    mov bl, al
    push ax
    
    cmp bx, 0
    jne PrintHexLap1
    
    
    PrintHexLap2:
        pop ax
    	push dx
    	    cmp ah, 10
    	    jl PrintHexSkip1
    	    mov dl, 55
    	    add dl, ah
    	    jmp PrintHexSkip2
    	    
    	    PrintHexSkip1:
    	    mov dl, '0'
        	add dl, ah
        	
        	PrintHexSkip2:
        	mov ah, 2
        	int 21h
    	pop dx	
    cmp dx, sp
    jne PrintHexLap2
    
    
    pop dx
    pop bx
    pop ax
    ret
PrintHex ENDP

end start ; set entry point and stop the assembler.
