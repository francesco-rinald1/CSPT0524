# importa libreria math
import math

# print di benvenuto
print("\nBenvenuto nell'esercizio W6D4, un Programma scritto in Python, per calcolare velocemente il perimetro di diverse figure geometriche.\nSei Pronto? Iniziamo!!")
print("\nAbbiamo tre figure: ")

# inizio ciclo programma
while True:
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("0. Chiudi App")

    # inizio gestione degli errori
    try:
        # dichiara e ricevi numero input
        scelta_figura = int(input("Scegli una figura: "))

        # condizione di scelta delle figure
        if scelta_figura == 1 :
            lato_quadrato = float(input("Inserisci un numero per determinare il lato del Quadrato: "))
            perim_quadrato = lato_quadrato * 4
            print("- Il Perimetro del Quadrato con un lato di", lato_quadrato, "cm, è di", int(perim_quadrato), "cm\n")
            print("Vuoi provare un'altra figura?")
        elif scelta_figura == 2 :
            raggio_cerchio = float(input("Inserisci un numero per determinare il raggio del Cerchio: "))
            circonferenza = 2 * math.pi * raggio_cerchio
            decimali_circonferenza = round(circonferenza,2)
            print("- La Circonferenza del Cerchio con un raggio di", raggio_cerchio, "cm, è di", decimali_circonferenza, "cm\n")
            print("Vuoi provare un'altra figura?")
        elif scelta_figura == 3 :
            base_rettangolo = float(input("Inserisci un numero per determinare la base del Rettangolo: "))
            altezza_rettangolo = float(input("Inserisci un numero per determinare l'altezza del Rettangolo: "))
            perim_rettangolo = base_rettangolo * 2 + altezza_rettangolo * 2
            print("- Il Perimetro del Rettangolo con una Base di ", base_rettangolo, "cm, e altezza di ", altezza_rettangolo, "cm, è di ", int(perim_rettangolo), "cm\n")
            print("Vuoi provare un'altra figura?")
        elif scelta_figura == 0 :
            print("Grazie, alla prossima!!")
            break
        else :
            print("Scelta non valida! Riprova!!\n")

    # fine gestione errori
    except ValueError:
        print("Ops!!! Hai inserito un carattere.\nInserisci un numero Valido!\n")