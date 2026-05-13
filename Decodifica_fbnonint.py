# Decodifica_fbnonint = Decodifica_forzabruta_nonintelligente

import time

password_corretta = input("> ")

charset = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')


def incrementa(lista_indici, base):
    i = len(lista_indici) - 1
    while i >= 0:
        if lista_indici[i] < base - 1:
            lista_indici[i] += 1
            return lista_indici
        lista_indici[i] = 0
        i -= 1
    return None


def brute_force(password_target):
    tentativi = 0
    start_time = time.time()
    lunghezza = 1
    max_lunghezza = 100

    charset_size = len(charset)

    while lunghezza <= max_lunghezza:
        indici = [0] * lunghezza
        totale_combinazioni = charset_size ** lunghezza
        gia_viste = 0

        while indici is not None:
            tentativo = ''.join(charset[i] for i in indici)

            tentativi += 1
            gia_viste += 1

            elapsed = time.time() - start_time

            # ⚡ velocità
            speed = tentativi / elapsed if elapsed > 0 else 0

            # ⏳ combinazioni rimanenti
            remaining = totale_combinazioni - gia_viste

            # 📊 stima tempo rimanente
            eta = remaining / speed if speed > 0 else 0

            print(
                f"\rTentativi: {tentativi} | Tempo: {elapsed:.2f}s | Tempo stimato: {eta:.2f}s",
                end="",
                flush=True
            )

            if tentativo == password_target:
                end_time = time.time()
                print("\n\n✅ Password trovata!")
                print(f"Password: {tentativo}")
                print(f"Tentativi totali: {tentativi}")
                print(f"Tempo impiegato: {end_time - start_time:.2f} secondi")
                return tentativo

            indici = incrementa(indici, charset_size)

        lunghezza += 1

    print("\nPassword non trovata entro il limite di lunghezza.")


brute_force(password_corretta)