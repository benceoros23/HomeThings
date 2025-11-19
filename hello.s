        .intel_syntax noprefix
        .section   .rodata
.TXT:   .string    "Hello world!\n"

        .globl     main
        .text
main:
        push       rbp
        mov        rbp, rsp
        and        rsp, 0xfffffffffffffff0      # igazítás 16 bájtra

        lea        rdi, [.TXT]                  # printf formátum string
        mov        eax, 0                       # nincs float parameter
        call       printf

        mov        rsp, rbp
        pop        rbp
        ret
