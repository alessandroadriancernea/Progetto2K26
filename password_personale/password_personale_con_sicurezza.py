# Questo programma chiede all'utente di inserire una password e verifica se è sicura
# se la password a almeno 8 caratteri alla password viene assegnato il livello 1
# se la password contiene almeno una lettera maiuscola alla password viene assegnato il livello 2
# se la password contiene almeno 5 lettere minuscole alla password viene assegnato il livello 3
# se la password contiene almeno 5 numeri alla password viene assegnato il livello 4
# se la password contiene almeno un carattere speciale alla password viene assegnato il livello 5
# e alla fine viene stampato il livello di sicurezza della password se 5 la password è molto sicura se 4 la password è sicura se 3 la password è debole se 2 la password è molto debole se 1 la password è estremamente debole


password = input("Inserisci la tua password: ")
livello = 0

if len(password) >= 8:
    livello = 1

if any(char.isupper() for char in password):
    livello = 2

if sum(char.islower() for char in password) >= 5:
    livello = 3

if sum(char.isdigit() for char in password) >= 5:
    livello = 4

if any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in password):
    livello = 5

if livello == 5:
    print("La tua password è molto sicura!")
elif livello == 4:
    print("La tua password è sicura!")
elif livello == 3:
    print("La tua password è debole!")
elif livello == 2:
    print("La tua password è molto debole!")
elif livello == 1:
    print("La tua password è estremamente debole!")
    