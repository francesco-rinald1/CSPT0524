# importa moduli essenziali
import random # modulo per printare caratteri a random
import string # modulo per usare diversi tipi di carateri

# definisci funzione che genera password
def generatorePasswd():
    print("\nGeneratore di Password.")

    # dichiara lista delle Opzioni orizzontale
    opzioni = ["Semplice", "Complessa", "Chiudi Generatore"]

    # metti lista delle opzioni in colonna e assegna un numero crescente alle stringhe
    #per usare enumerate va creta una nuova variabile nel ciclo for
    #assegnare numero di partenza con start=n
    for numeri, op_list in enumerate(opzioni, start=1):
        print(f"{numeri}. {op_list}")

    # dichiara variabili per passwd
    # -ascii_letters usa tutte le lettere dell'alfabeto sia maiuscole che minuscole.
    # -digits        usa tutti i numeri decimali da 0 a 9
    semplice = string.ascii_letters + string.digits
    complessa = string.printable.strip()

    # avvia ciclo 
    while True:
        # inizio gestione degli errori
        try:
            # dichiara input utente che va a scegliere una opizione
            scelta = int(input("Seleziona il tipo di Password che vuoi creare. 1, 2 o 0 per Chiudere: "))
            # inizio condizione if elif else per gestire la scelta
            if scelta == 1:
                password = "".join(random.choices(semplice, k=8))
                print(f"\nPassword Semplice: {password}\n")
            elif scelta == 2:
                password = "".join(random.choices(complessa, k=20))
                print(f"\nPassword Complessa: {password}\n")
            elif scelta == 3:
                print("Grazie, alla prossima!")
                break
            else: 
                print("Digita un numero valido!")
        # fine gestione errori
        except ValueError:
            print("C'è un Errore!")

generatorePasswd()
