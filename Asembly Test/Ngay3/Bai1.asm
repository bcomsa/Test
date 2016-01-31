; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db 0ah, 0dh, "Nhap vao 1-6: $"
    Mess2 db 0ah, 0dh, "Nhap chuoi 1: $"
    Mess3 db 0ah, 0dh, "Nhap chuoi 2: $"
    Mess4 db 0ah, 0dh, "Nhap sai!$"
    Mess5 db 0ah, 0dh, "Xin moi nhap chuoi: $"
    
    Str1 db 100, ?, 100 dup(0)
    
    Str2 db 100, ?, 100 dup(0)
    Str3 db 100, ?, 100 dup(0)
    Str4 db 100, ?, 100 dup(0)
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
    je CallFunc4
    cmp KyTu, '5'
    je CallFunc5
    cmp KyTu, '6'
    je KetThuc:
    ;In Mess4 (Nhap sai)        
    lea dx, Mess4
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
    
    CallFunc4:
    call Func4
    jmp Loop1
    
    CallFunc5:
    call Func5
    jmp Loop1
    
    KetThuc:    
    mov ax, 4c00h ; exit to operating system.
    int 21h
ends

Func1 PROC
    push dx
    push ax
    push bx
    push dx
    
    ;In Mess5        
    lea dx, Mess5
    mov ah, 9
    int 21h 
    
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
    pop dx
    ret
Func1 ENDP

Func2 PROC 
    push ax
    push bx
    push cx
    push dx 
    
    ;Xuat Str1 ra may in
    ;Xac dinh so lan lap
    xor cx, cx
    mov cl, Str1[1]
    mov ah, 5
    xor bx, bx
    
    ;Xuat lan luot tung ki tu ra man hinh theo so ky tu cu chuoi
    Func2Lap1:
        mov dl, Str1[bx+2]
    	int 21h
    	inc bx
    Loop Func2Lap1:
    
    ;Xuong dong
    mov dl, 0ah
	int 21h
    mov dl, 0dh
	int 21h    
	
    
    pop  dx
    pop  cx
    pop  bx
    pop  ax
    ret
Func2 ENDP

Func3 PROC
    push cx
    push ax
    push dx
    
    xor cx, cx
    mov cl, Str1[1]
    mov bx, cx
    add bx, 2
    mov ah, 5
    
    Func3Loop1:
    dec bx
    mov dl, Str1[bx]
    int 21h
    loop Func3Loop1
    
    ;Xuong dong
    mov dl, 0ah
	int 21h
    mov dl, 0dh
	int 21h 
    
    pop dx
    pop ax
    pop cx
    ret
Func3 ENDP

Func4 PROC
    push dx
    push ax
    
    xor ax, ax
    ;In Mess2        
    lea dx, Mess2
    mov ah, 9
    int 21h
    
    ;Nhap Str1
    mov dx, offset Str2
    mov ah, 10
    int 21h
    
    ;In Mess3        
    lea dx, Mess3
    mov ah, 9
    int 21h
    
    ;Nhap Str2
    mov dx, offset Str3
    mov ah, 10
    int 21h
    
    pop dx
    pop ax
    ret
Func4 ENDP

Func5 PROC
    push ax
    push bx
    push cx
    push dx
    mov ah, 05h
    
    ;In sau 1 ra may in
    ;Lay so ki tu sau 1
    xor cx, cx
    mov cl, Str2[1]
    
    ;In tung ki tu sau 1
    xor bx, bx
    Func5Loop2:
    mov dl, Str2[bx+2]
    int 21h
    inc bx
    Loop Func5Loop2
        
    ;In sau 2 ra may in
    ;Lay so ki tu sau 2
    xor cx, cx
    mov cl, Str3[1]
    
    ;In tung ki tu sau 2
    xor bx, bx
    Func5Loop3:
    mov dl, Str3[bx+2]
    int 21h
    inc bx
    Loop Func5Loop3
	
	    
    ;Xuong dong
    mov dl, 0ah
	int 21h
    mov dl, 0dh
	int 21h 
	
    pop dx
    pop cx
    pop bx
    pop ax
    ret
Func5 ENDP

end start ; set entry point and stop the assembler.
