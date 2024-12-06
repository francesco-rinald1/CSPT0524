//includi libreria input/output
#include <stdio.h>

//inizio compilazione della main
int main() {
    
    //variabili
    int D;
//  float area_cerchio = ((D * D) * 3.14);
    
    //stampa frase per richiedere un numero
    printf("Dammi un numero per dare un valore alla lettera D: \n");
    
    //assegna numero a variabile D
    scanf("%i", &D);
    
    //stampa + calcolo area quadrato
    printf("Considerando che il lato del quadrato è di %icm, l'area è pari a %icm quadrati\n\n", D, D*D);
    
    //stampa + calcolo area cerchio
    printf("Considerando che il raggio del cerchio è di %icm, l'area è pari a %.1fcm quadrati\n\n", D, D * D * 3.14);

    //stampa + calcolo area triangolo equilatero
    printf("Considerando che un raggio del triangolo è di %icm, e che la radice quadrata di 3 equivale a 1.732, l'area è pari a %.3fcm quadrati\n\n", D, ((1.732 / 4) * D * D));


    return 0;
}