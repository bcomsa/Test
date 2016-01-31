; multi-segment executable file template.

data segment
    ; add your data here!
    Mess1 db "Nhap so co toi da 3 chu so: $"
    Mess2 db 0ah, 0dh, "So  ban nhap doc la: $"
    Str1 db 100, ?, 100 dup (0)
    
    DonVi0 db " khong don vi$"
    DonVi1 db " mot don vi$"
    DonVi2 db " hai don vi$"
    DonVi3 db " ba don vi$"
    DonVi4 db " bon don vi$"
    DonVi5 db " nam don vi$"
    DonVi6 db " sau don vi$"
    DonVi7 db " bay don vi$"
    DonVi8 db " tam don vi$"
    DonVi9 db " chin don vi$"
    
    Chuc0 db " khong chuc$"
    Chuc1 db " mot chuc$"
    Chuc2 db " hai chuc$"
    Chuc3 db " ba chuc$"
    Chuc4 db " bon chuc$"
    Chuc5 db " nam chuc$"
    Chuc6 db " sau chuc$"
    Chuc7 db " bay chuc$"
    Chuc8 db " tam chuc$"
    Chuc9 db " chin chuc$"
    
    Tram0 db "khong tram$"
    Tram1 db "mot tram$"
    Tram2 db "hai tram$"
    Tram3 db "ba tram$"
    Tram4 db "bon tram$"
    Tram5 db "nam tram$"
    Tram6 db "sau tram$"
    Tram7 db "bay tram$"
    Tram8 db "tam tram$"
    Tram9 db "chin tram$"
    
    
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

    ; add your code here
    
    ;In Mess1        
    lea dx, Mess1
    mov ah, 9
    int 21h        
    
    ;Nhap so
    lea dx, Str1
    mov ah, 10
    int 21h        
    
    ;In Mess2
    lea dx, Mess2
    mov ah, 9
    int 21h   
    
    Call DocTram
    Call DocChuc
    Call DocDonVi
    
    
    
    
    ;Cho thoat   
    mov ah, 1
    int 21h
    
    mov ax, 4c00h ; exit to operating system.
    int 21h    
ends


DocDonVi PROC
    push dx
    push ax
    push bx
    
    xor bx, bx
    mov bl, Str1[1]
    add bx, 1
    
    lea dx, DonVi0
    cmp Str1[bx], '0'
    je DocDonViSkip
    lea dx, DonVi1
    cmp Str1[bx], '1'
    je DocDonViSkip
    lea dx, DonVi2
    cmp Str1[bx], '2'
    je DocDonViSkip
    lea dx, DonVi3
    cmp Str1[bx], '3'
    je DocDonViSkip
    lea dx, DonVi4
    cmp Str1[bx], '4'
    je DocDonViSkip
    lea dx, DonVi5
    cmp Str1[bx], '5'
    je DocDonViSkip
    lea dx, DonVi6
    cmp Str1[bx], '6'
    je DocDonViSkip
    lea dx, DonVi7
    cmp Str1[bx], '7'
    je DocDonViSkip
    lea dx, DonVi8
    cmp Str1[bx], '8'
    je DocDonViSkip
    lea dx, DonVi9
    
    DocDonViSkip:
    mov ah, 9
    int 21h 
    
    pop bx
    pop ax
    pop dx
    ret
DocDonVi ENDP

DocChuc PROC
    push dx
    push ax
    push bx
    
    xor bx, bx
    mov bl, Str1[1]
    
    cmp Str1[1], 1
    jng DocChucSkip2
    
    lea dx, Chuc0               
    cmp Str1[bx], '0'
    je DocChucSkip
    lea dx, Chuc1              
    cmp Str1[bx], '1'
    je DocChucSkip
    lea dx, Chuc2
    cmp Str1[bx], '2'
    je DocChucSkip
    lea dx, Chuc3
    cmp Str1[bx], '3'
    je DocChucSkip
    lea dx, Chuc4
    cmp Str1[bx], '4'
    je DocChucSkip
    lea dx, Chuc5
    cmp Str1[bx], '5'
    je DocChucSkip
    lea dx, Chuc6
    cmp Str1[bx], '6'
    je DocChucSkip
    lea dx, Chuc7
    cmp Str1[bx], '7'
    je DocChucSkip
    lea dx, Chuc8
    cmp Str1[bx], '8'
    je DocChucSkip
    lea dx, Chuc9
    
    DocChucSkip:
    mov ah, 9
    int 21h 
    
    DocChucSkip2:
    pop bx
    pop ax
    pop dx
    ret
DocChuc ENDP

DocTram PROC
    push dx
    push ax
    push bx
    
    xor bx, bx
    mov bl, Str1[1]
    dec bx
    
    cmp Str1[1], 2
    jng DocTramSkip2
    
    lea dx, Tram0               
    cmp Str1[bx], '0'
    je DocTramSkip
    lea dx, Tram1              
    cmp Str1[bx], '1'
    je DocTramSkip
    lea dx, Tram2
    cmp Str1[bx], '2'
    je DocTramSkip
    lea dx, Tram3
    cmp Str1[bx], '3'
    je DocTramSkip
    lea dx, Tram4
    cmp Str1[bx], '4'
    je DocTramSkip
    lea dx, Tram5
    cmp Str1[bx], '5'
    je DocTramSkip
    lea dx, Tram6
    cmp Str1[bx], '6'
    je DocTramSkip
    lea dx, Tram7
    cmp Str1[bx], '7'
    je DocTramSkip
    lea dx, Tram8
    cmp Str1[bx], '8'
    je DocTramSkip
    lea dx, Tram9
    
    DocTramSkip:
    mov ah, 9
    int 21h 
    
    DocTramSkip2:
    pop bx
    pop ax
    pop dx
    ret
DocTram ENDP

end start ; set entry point and stop the assembler.
