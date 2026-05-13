from wordfreq import word_frequency
import time


def analizza_frase(frase, lingua="it"):
    parole = frase.lower().split()

    totale_score = 0
    analisi = []

    for parola in parole:
        freq = word_frequency(parola, lingua)

        # trasformiamo frequenza in "difficoltà"
        if freq == 0:
            difficolta = "sconosciuta (molto rara)"
            score = 5
        elif freq > 1e-2:
            difficolta = "molto comune"
            score = 1
        elif freq > 1e-4:
            difficolta = "media"
            score = 2
        elif freq > 1e-6:
            difficolta = "rara"
            score = 3
        else:
            difficolta = "molto rara"
            score = 4

        totale_score += score

        analisi.append((parola, freq, difficolta))

    return analisi, totale_score


def stima_tentativi(score_totale):
    # simulazione teorica (NON brute force reale)
    base = 10 ** score_totale
    return base


def stima_tempo(tentativi, speed_per_sec=1_000_000):
    secondi = tentativi / speed_per_sec

    if secondi < 60:
        return f"{secondi:.4f} secondi"
    elif secondi < 3600:
        return f"{secondi/60:.2f} minuti"
    elif secondi < 86400:
        return f"{secondi/3600:.2f} ore"
    else:
        return f"{secondi/86400:.2f} giorni"


def main():
    frase = input("Inserisci una frase o 'password': ")

    print("\n🔍 Analisi in corso...\n")
    time.sleep(0.5)

    analisi, score = analizza_frase(frase)

    for parola, freq, diff in analisi:
        print(f"- {parola:15} | freq: {freq:.8f} | {diff}")

    tentativi = stima_tentativi(score)
    tempo = stima_tempo(tentativi)

    print("\n📊 RISULTATI")
    print(f"Punteggio complessivo: {score}")
    print(f"Numero stimato combinazioni: {tentativi:.2e}")
    print(f"Tempo stimato di attacco teorico: {tempo}")

    print("\n⚠️ Nota: è una simulazione matematica, non un attacco reale.")


if __name__ == "__main__":
    main()