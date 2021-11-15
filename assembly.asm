section .bss
        buf resb 8  ; define an array of 8 uninitialised bytes
section .text

global _start
_start:
    mov rax, 3  ; system call number (sys_read)
    xor rbx, rbx    ; file descriptor 0 (stdin)
    mov rcx, buf    ; buffer to store data
    mov rdx, 8  ; Lenght of buffer
    int 0x80

    xor rax,rax ; rax = 0
    mov rbx, buf    ; rbx = &buf
    xor rcx, rcx    

StrToDec:
        mov cl, [rbx]   ; cl = *rbx 
        cmp rcx, 0      ; check for nul THIS IS WRONG
        cmp rcx, 10     ; we have to check for NL ascii code 
        je end          ; if rcx == 0 goto end
        imul rax, 10    ; rax *= 10
        sub rcx, 48     ; rcx -= 48 (48 is acii for '0')
        add rax, rcx    ; rax += rcx
        inc rbx         ; rbx++
        jmp StrToDec

end:
    mov rbx, rax    ; rbx = rax
    mov rax, 1      ; rax = 1
    int 0x80
