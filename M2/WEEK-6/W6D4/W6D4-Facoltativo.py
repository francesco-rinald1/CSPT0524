import math

# Print di Benvenuto
print("\nBenvenuto Nel Programma Facoltativo W6D4")

# variabili
figure = ["1 -> Quadrato", "2 -> Cerchio", "3 -> Rettangolo", "0 -> Chiudi Applicazione"]

# print lista menu
def lista():
    print("\nFigure Disponibili:")
    return "\n".join(figure)
    # print("Figure Disponibili:")
    # print(figure[0])
    # print(figure[1])
    # print(figure[2])

# Funzione per ricevere un numero dall' utente
def input_numero():
    global numero
    try:
        numero = float(input("\nDigita un Numero: "))
        if numero <= 0 :
            print("Mi Dispiace, non accetto Numeri Negativi!")
            input_numero()
    except ValueError:
        print("Mi Dispiace, non accetto Lettere")
        input_numero()

# funzione per scegliere la figura
def input_figura():
    global figura
    try:
        figura = int(input("\nSeleziona una Figura o Premi 0 per Uscire: "))
    except ValueError:
        print("Mi Dispiace, non accetto Lettere")
        print(lista())
        input_figura()

# funzione per definire altezza rettangolo
def input_altezza():
    global altezza
    while True:
        try:
            altezza = float(input("Inserisci un numero per l'altezza del Rettangolo: "))
            if altezza <= 0:
                print("Mi Dispiace, non accetto numeri negativi o zero!")
            else:
                break
        except ValueError:
            print("Mi Dispiace, non accetto caratteri. Inserisci un numero valido.")


# Funzione prima scelta
def sceltaIniziale():
    global area_quadrato
    global area_cerchio
    global area_rettangolo
    while True:
            if figura == 1:
                perimetro_quadrato = numero * 4
                area_quadrato = numero * numero
                print("\n---------------------------------------------")
                print("Quadrato:")
                print("-Lato = ", round(numero), "cm")
                print("    -> Area      = ", round(area_quadrato), "cm (", round(numero), "*", round(numero), ")", sep="")
                print("    -> Perimetro = ", round(perimetro_quadrato),"cm (", round(numero), "*4)", sep="")
                print("-----------------------------------------------")
                print("Il numero inserito", numero, ", viene sostituito da", area_quadrato, "(Area Quadrato)")
                del figure[0]
                print(lista())
                input_figura()
                sceltaQuadrato()
            elif figura == 2:
                circonferenza_cerchio = 2 * math.pi * float(numero)
                area_cerchio = float(numero) ** 2 * math.pi
                print("\n---------------------------------------------")
                print("Cerchio:")
                print("-Raggio = ", numero, "cm")
                print("    -> Area          = ", round(area_cerchio, 2),"cm (", round(numero), "**2)*3.14", sep="")
                print("    -> Circonferenza = ", round(circonferenza_cerchio, 2), "cm (2*3.14*", round(numero), ")", sep="")
                print("---------------------------------------------")
                print("Il numero inserito", numero, ", viene sostituito da", round(area_cerchio,2), "(Area Cerchio)")
                del figure[1]
                print(lista())
                input_figura()
                sceltaCerchio()
            elif figura == 3:
                input_altezza()
                perimetro_rettangolo = 2 * (float(numero) + float(altezza))
                area_rettangolo = float(numero) * float(altezza)
                print("\n---------------------------------------------")
                print("Rettangolo:")
                print("-Base    = ", numero, "cm")
                print("-Altezza = ", altezza, "cm")
                print("    -> Area      = ", round(area_rettangolo), "cm (", round(numero), "*", round(altezza), ")", sep="")
                print("    -> Perimetro = ", round(perimetro_rettangolo), "cm 2*(", round(numero), "+", round(altezza), ")", sep="")
                print("---------------------------------------------")
                print("Il numero inserito", numero, ", viene sostituito da", area_rettangolo, "(Area Rettangolo)")
                del figure[2]
                print(lista())
                input_figura()
                sceltaRettangolo()
            elif figura == 0:
                print("Grazie per essere passato. Alla prossima!")
                break
            else:
                print("Numero non valido!")
                print(lista())
                input_figura()


# funzione se premuto 1 in sceltaIniziale()
def sceltaQuadrato():
    while True:
            if figura == 2:
                print("\n---------------------------------------------")
                print("Cerchio:")
                print("-Raggio = ", area_quadrato, "cm")
                print("    -> Area          = ", round(area_quadrato ** 2 * math.pi, 2), "cm (", round(area_quadrato), "**2)*3.14", sep="")
                print("    -> Circonferenza = ", round(2 * math.pi * area_quadrato, 2), "cm (2*3.14*", round(area_quadrato), ")", sep="")
                print("---------------------------------------------")
                del figure[0]
                print(lista())
                input_figura()
                if figura == 3:
                    input_altezza()
                    #altezza = input("Inserisci un numero per l'Altezza del Rettangolo: ")
                    print("\n---------------------------------------------")
                    print("Rettangolo:")
                    print("-Base    = ", area_quadrato, "cm")
                    print("-Altezza = ", round(altezza), "cm")
                    print("    -> Area      = ", round(area_quadrato) * round(altezza), "cm (", round(area_quadrato), "*", round(altezza), ")", sep="")
                    print("    -> Perimetro = ", 2 * round(area_quadrato) + round(altezza), "cm 2*(", round(area_quadrato), "+", round(altezza), ")", sep="")
                    print("\n---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!\nPremi 3 per il Rettangolo oppure Premi 0 per Uscire.")
            elif figura == 3:
                input_altezza()
                #altezza = input("Inserisci un numero per l'Altezza del Rettangolo: ")
                print("\n---------------------------------------------")
                print("Rettangolo:")
                print("-Base    = ", round(area_quadrato), "cm")
                print("-Altezza = ", round(altezza), "cm")
                print("    -> Area      = ", round(area_quadrato) * round(altezza), "cm (", round(area_quadrato), "*", round(altezza), ")", sep="")
                print("    -> Perimetro = ", 2 * round(area_quadrato) + round(altezza), "cm 2*(", area_quadrato, "+", altezza, ")", sep="")
                print("---------------------------------------------")
                del figure[1]
                print(lista())
                input_figura()
                if figura == 2:
                    print("\n---------------------------------------------")
                    print("Cerchio:")
                    print("-Raggio = ", round(area_quadrato), "cm")
                    print("    -> Area          = ", round(area_quadrato ** 2 * math.pi, 2), "cm (", area_quadrato, "**2)*3.14", sep="")
                    print("    -> Circonferenza = ", 2 * math.pi * round(area_quadrato, 2), "cm (2*3.14*", round(area_quadrato, 2), ")", sep="")
                    print("\n---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!")
            elif figura == 0:
                print("Grazie per essere passato. Alla prossima!")
                break
            else:
                print("Numero non valido!")
                print(lista())
                input_figura()

# funzione se premuto 2 in sceltaIniziale()
def sceltaCerchio():
    while True:
            if figura == 1:
                print("\n---------------------------------------------")
                print("Quadrato:")
                print("-Lato = ", area_cerchio, "cm")
                print("    -> Area      = ", area_cerchio * area_cerchio, "cm (", round(area_cerchio), "*", round(area_cerchio), ")", sep="")
                print("    -> Perimetro = ", area_cerchio * 4, "cm (", round(area_cerchio), "*4)", sep="")
                print("---------------------------------------------")
                del figure[0]
                print(lista())
                input_figura()
                if figura == 3:
                    input_altezza()
                    #altezza = input("Inserisci un numero per l'Altezza del Rettangolo: ")
                    print("\n---------------------------------------------")
                    print("Rettangolo:")
                    print("-Base    = ", area_cerchio, "cm")
                    print("-Altezza = ", float(altezza), "cm")
                    print("    -> Area      = ", area_cerchio * altezza, "cm (", area_cerchio, "*", altezza, ")", sep="")
                    print("    -> Perimetro = ", area_cerchio * 2 + float(altezza), "cm 2*(", area_cerchio, "+", altezza, ")", sep="")
                    print("\n---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!")
            elif figura == 3:
                input_altezza()
                #altezza = input("Inserisci un numero per l'Altezza del Rettangolo: ")
                print("\n---------------------------------------------")
                print("Rettangolo:")
                print("-Base    = ", area_cerchio, "cm")
                print("-Altezza = ", float(altezza), "cm")
                print("    -> Area      = ", area_cerchio * float(altezza), "cm (", area_cerchio, "*", altezza, ")", sep="")
                print("    -> Perimetro = ", 2 * (round(area_cerchio) + round(altezza)), "cm 2*(", area_cerchio, "+", altezza, ")", sep="")
                print("---------------------------------------------")
                del figure[1]
                print(lista())
                input_figura()
                if figura == 1:
                    print("---------------------------------------------")
                    print("Quadrato:")
                    print("-Lato = ", area_cerchio, "cm")
                    print("    -> Area      = ", area_cerchio * area_cerchio, "cm (", round(area_cerchio), "*", round(area_cerchio), ")", sep="")
                    print("    -> Perimetro = ", area_cerchio * 4, "cm (", round(area_cerchio), "*4)", sep="")
                    print("\n---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!")
            elif figura == 0:
                print("Grazie per essere passato. Alla prossima!")
                break
            else:
                print("Numero non valido!")
                print(lista())
                input_figura()

# funzione se premuto 3 in sceltaIniziale()
def sceltaRettangolo():
    while True:
            if figura == 1:
                print("\n---------------------------------------------")
                print("Quadrato:")
                print("-Lato = ", area_rettangolo, "cm")
                print("    -> Area      = ", area_rettangolo * area_rettangolo, "cm (", round(area_rettangolo), "*", round(area_rettangolo), ")", sep="")
                print("    -> Perimetro = ", area_rettangolo * 4, "cm (", round(area_rettangolo), "*4)", sep="")
                print("---------------------------------------------")
                del figure[0]
                print(lista())
                input_figura()
                if figura == 2:
                    print("\n---------------------------------------------")
                    print("Cerchio:")
                    print("-Raggio = ", area_rettangolo, "cm")
                    print("    -> Area          = ", ((area_rettangolo ** 2) * 3.14), "cm (", area_rettangolo, "**2)*3.14", sep="")
                    print("    -> Circonferenza = ", 2 * 3.14 * area_rettangolo, "cm (2*3.14*", round(area_rettangolo), ")", sep="")
                    print("---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!")
            elif figura == 2:
                print("\n---------------------------------------------")
                print("Cerchio:")
                print("-Raggio = ", area_rettangolo, "cm")
                print("    -> Area          = ", ((area_rettangolo ** 2) * 3.14), "cm (", area_rettangolo, "**2)*3.14", sep="")
                print("    -> Circonferenza = ", 2 * 3.14 * area_rettangolo, "cm (2*3.14*", round(area_rettangolo), ")", sep="")
                print("---------------------------------------------")
                del figure[1]
                print(lista())
                input_figura()
                if figura == 1:
                    print("\n---------------------------------------------")
                    print("Quadrato:")
                    print("-Lato = ", area_rettangolo, "cm")
                    print("    -> Area      = ", area_rettangolo * area_rettangolo, "cm (", round(area_rettangolo), "*", round(area_rettangolo), ")", sep="")
                    print("    -> Perimetro = ", area_rettangolo * 4, "cm (", round(area_rettangolo), "*4)", sep="")
                    print("\n---------------------------------------------")
                    print("Bene, Ricominciamo!")
                    main()
                elif figura == 0:
                    print("Grazie per essere passato. Alla prossima!")
                    break
                else:
                    print("Numero non valido!")
            elif figura == 0:
                print("Grazie per essere passato. Alla prossima!")
                break
            else:
                print("Numero non valido!")
                print(lista())
                input_figura()

# logica di partenza
def main():
    global figure
    input_numero()
    figure = ["1 -> Quadrato", "2 -> Cerchio", "3 -> Rettangolo", "0 -> Chiudi Applicazione"]
    print(lista())
    input_figura()
    sceltaIniziale()

main()
