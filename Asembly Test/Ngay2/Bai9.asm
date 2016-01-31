; multi-segment executable file template.

data segment
    ; add your data here!
    pkey db "press any key...$"
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

    call ThietLapDoHoa
    
    mov dh, 12
	mov dl, 17
	mov bh, 0
	mov ah, 2
	int 10h
	
    mov ah, 9
    mov al, 'H'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h 
    
    mov dh, 12
	mov dl, 18
	mov bh, 0
	mov ah, 2
	int 10h
    
    mov ah, 9
    mov al, 'V'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h
    
    mov dh, 12
	mov dl, 19
	mov bh, 0
	mov ah, 2
	int 10h
	
    mov ah, 9
    mov al, 'K'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h 
    
    mov dh, 12
	mov dl, 20
	mov bh, 0
	mov ah, 2
	int 10h
    
    mov ah, 9
    mov al, 'T'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h
    
    mov dh, 12
	mov dl, 21
	mov bh, 0
	mov ah, 2
	int 10h
	
    mov ah, 9
    mov al, 'M'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h 
    
    mov dh, 12
	mov dl, 22
	mov bh, 0
	mov ah, 2
	int 10h
    
    mov ah, 9
    mov al, 'M'
    mov bh, 0
    mov bl, 0100b
    mov cx, 1
    int 10h
    
    ; wait for any key....    
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends

ThietLapDoHoa PROC
    push ax
    
    mov ah, 00h
    mov al, 13h
    int 10h
    
    pop ax
    ret
ThietLapDoHoa ENDP

end start ; set entry point and stop the assembler.
