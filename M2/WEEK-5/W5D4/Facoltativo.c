#include <stdio.h>

int main() {
float num1, num2, num3, media3 = ((num1 + num2 + num3)/3);

printf("In questa sessione andremo a calcolare la media di tre numeri inseriti da te e successivamente ti mostrerò il risultato dell'area di un quadrato, di un cerchio e di un triangolo in base alla media dei tuoi numeri, e mostreremo un risultato in decimali e uno arrotondato senza dicomali.\n\n");

    printf("Inserisci il primo numero: \n");
    scanf("%f", &num1);

    printf("Bene! Adesso inserisci il secondo numero: \n");
    scanf("%f", &num2);

    printf("Molto Bene!! Non ti resta che inserire il terzo numero: \n");
    scanf("%f", &num3);


float media1 = ((num1 + num2 + num3)/3);
int media2 = ((num1 + num2 + num3)/3);
    
    printf("Perfetto!!! I Tuoi numeri sono %.2f, %.2f e %.2f\n", num1, num2, num3);
    
    printf("La media aritmetica è di %.2f\n", media1);
    
    printf("La media aritmetica arrotondata è di %i\n\n\n", media2);
    
float area_quadrato = (media1 * media1);
float area_cerchio = (media1 * media1) * 3.14;
float area_triangolo = (media1 * media1) * (1.732 / 4);

int area_quadrato1 = (media1 * media1);
int area_cerchio1 = (media1 * media1) * 3.14;
int area_triangolo1 = (media1 * media1) * (1.732 / 4);
    printf("MEDIA DECIMALE\n");
    printf("L'area di un quadrato avendo il lato di %.2fcm, è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm.\n\n", media1, area_quadrato, area_quadrato1);

    printf("L'area di un cerchio con raggio di %.2fcm, è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm.\n\n", media1, area_cerchio, area_cerchio1);

    printf("L'area di un triangolo con lato di %.2fcm è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm\n\n", media1, area_triangolo, area_triangolo1);
    
    printf("MEDIA ARROTONDATA\n");
    printf("L'area di un quadrato avendo il lato di %icm, è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm.\n\n", media2, area_quadrato, area_quadrato1);
    
    printf("L'area di un cerchio con raggio di %icm, è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm.\n\n", media2, area_cerchio, area_cerchio1);
    
    printf("L'area di un triangolo con lato di %icm è pari a %.2fcm,\ninvece con un risultato arrotondato sarebbe pari a %icm\n\n", media2, area_triangolo, area_triangolo1);

    return 0;
}