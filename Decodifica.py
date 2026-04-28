from input_password.password_personale import inserisci_password
import time
password_corretta = inserisci_password()

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

    while lunghezza <= max_lunghezza:
        indici = [0] * lunghezza

        while indici is not None:
            tentativo = ''.join(charset[i] for i in indici)
            tentativi += 1

            print(f"\rTentativi: {tentativi}", end="", flush=True)

            if tentativo == password_target:
                end_time = time.time()
                print("\n\nPassword trovata!")
                print(f"Password: {tentativo}")
                print(f"Tentativi totali: {tentativi}")
                print(f"Tempo impiegato: {end_time - start_time:.2f} secondi")
                return tentativo

            indici = incrementa(indici, len(charset))

        lunghezza += 1

    print("Password non trovata entro il limite di lunghezza.")

brute_force(password_corretta)