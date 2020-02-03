#include <stdio.h> /*Autorise l'emploi de printf et de scanf.*/


int main(void)
{
    long double x, y;
    printf("Calcul de moyenne\n");   /* Affiche le titre. */
    printf("Entrez le premier nombre : ");
    scanf("%Lf", &x);            /* Entre le premier nombre. */
    printf("\nEntrez le deuxième nombre : ");
    scanf("%Lf", &y);            /* Entre le deuxième nombre. */
    printf("\nLa valeur moyenne de %Lf et de %Lf est %Lf.\n",
        x, y, (x+y)/2);
    return 0;
}
