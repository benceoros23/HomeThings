.intel_syntax noprefix              # Intel szintaxis használata
.section .rodata                    # Csak olvasható adat szekció
MSG:    .string "Hello %s\n"        # Kiírandó formátumszöveg

.section .text                      # Kód szekció
.globl main                         # main függvény globálissá tétele

main:

        cmp     edi, 2              # Összehasonlítja argc-et (edi) 2-vel
        jl      end                 # Ha argc < 2, ugrik end-re

        mov     rsi, [rsi+8]        # rsi-be betölti argv[1] címét
        lea     rdi, MSG            # rdi-be betölti a formátumszöveg címét
        xor     eax, eax            # eax = 0 
        call    printf              # Meghívja a printf-et

end:
        mov     eax, 0              # Visszatérési érték = 0
        ret                          # Visszatérés a rendszernek
