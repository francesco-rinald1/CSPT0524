# Definisci una lista di parole (ORIZZONTALE)
lista_A = ["Epicode", "Cybersecurity", "Python", "Programmazione", "Hacker"]


# funzione per printare parole e interi
def parole():

    # metti la lista in colonna e stampa un trattino a inizio frase
    print("\nLista di Parole:")
    for lista in lista_A:
        print("-", lista)

    # stampa la seconda lista con stringhe + interi    
    print("\nLista con Interi:")
    for lista in lista_A:
        print("-La parola", lista, "contiene", len(lista), "interi")


# chiama la funzione
parole()