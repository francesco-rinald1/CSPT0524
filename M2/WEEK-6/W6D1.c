/* sono stato aiutato dalla AI, un buon 50% sono riuscito a farlo da solo, 
poi per logica ho dovuto chiedere spiegazioni a GPT*/

#include <stdio.h>
#include <string.h>

//definisci il numro di domande
#define NUM_DOMANDE 5

//funzione di benvenuto
void benvenuto() {
    printf("Benvenuto nel Gioco dei Quiz del W6D1");
    printf("\n\nIn questo Gioco affronterai cinque domande e avrai tre risposte di cui solo una è corretta.");
}

// Funzione per gestire il quiz
void domande() {
    // Array delle domande
    char *domande[] = {
        "Qual è la capitale d'Italia?",
        "Qual è il risultato di 5 * 6?",
        "Chi ha scritto 'La Divina Commedia'?",
        "Qual è il pianeta più vicino al sole?",
        "Qual è il colore della bandiera italiana?"
    };

    // Array delle risposte
    char *risposte[][3] = {
        {"Roma", "Milano", "Napoli"},
        {"11", "30", "50"},
        {"Dante", "Petrarca", "Boccaccio"},
        {"Venere", "Terra", "Mercurio"},
        {"Rosso, bianco, verde", "Rosso, blu, bianco", "Verde, bianco, nero"}
    };

    // Indici delle risposte corrette
    int risposteCorrette[] = {0, 1, 0, 2, 0};

    int vite = 3;      // Numero di vite
    int punteggio = 0; // Punteggio iniziale

    // Ciclo domande
    for (int i = 0; i < NUM_DOMANDE; i++) {
        printf("\nDomanda %d: %s\n", i + 1, domande[i]);
        printf("1) %s\n", risposte[i][0]);
        printf("2) %s\n", risposte[i][1]);
        printf("3) %s\n", risposte[i][2]);
        printf("Inserisci il numero della tua risposta (1-3): ");

        int risposta;
        scanf("%d", &risposta);

        // Verifica della risposta
        if (risposta - 1 == risposteCorrette[i]) {
            printf("Risposta corretta!\n");
            punteggio += 10;
        } else {
            printf("Risposta sbagliata!\n");
            vite--;
            if (vite == 0) {
                printf("\nMi dispiace, hai esaurito le vite. Hai perso!\n");
                printf("Punteggio totale: %d punti\n", punteggio);
                return;
            }
        }

        printf("Vite rimanenti: %d | Punteggio: %d\n", vite, punteggio);
    }

    printf("\nComplimenti! Hai completato il quiz.\n");
    printf("Punteggio totale: %d punti\n", punteggio);
}

// Funzione per chiedere il nome
void nome() {
    char nome[20];
    printf("\n\nQual è il tuo Nome?\n");
    scanf("%s", nome);
    printf("Ciao %s, iniziamo a giocare!!\n\n", nome);
    domande(); // Chiama la funzione domande
}

// Funzione per gestire la scelta del giocatore
void partita() {
    printf("\n\nVuoi iniziare una partita?");
    printf("\nPremi A per iniziare, oppure premi B per chiudere il gioco: \n");

    char scelta;
    scanf(" %c", &scelta);

    if (scelta == 'A' || scelta == 'a') {
        printf("\n\nBENE!! Iniziamo una partita!");
        nome();
    } else if (scelta == 'B' || scelta == 'b') {
        printf("\n\nVa bene, quando vuoi tornare a giocare ti aspetto qui!!!");
    } else {
        printf("\n\nOps!!! Comando non valido. Ricominciamo!");
        partita();
    }
}

int main() {
    benvenuto();
    partita();
    return 0;
}