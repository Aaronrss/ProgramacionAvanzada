/*Programa que muestra
 la funcionalidad basica
 de un ciclo do-while*/

// stdio.h, what elements this library brings
#include <stdio.h>
int main(){
 int x = 5,i = 0;
 do{
    i++;
    /* What does %d\n means and work*/
    printf("%d\n",i);
 }while(i < x);
 return 0;
}
