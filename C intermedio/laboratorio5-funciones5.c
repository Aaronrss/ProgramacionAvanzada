/*Programa que muestra
el uso de funciones 3*/

#include <stdio.h>
#include <string.h>

void imprimir(int a, char texto[4]){
 int x,y;	
 for (x=0;x<a;x++){
   for(y=0;y<strlen(texto);y++){ 	
     printf(" %c ",texto[y]);
   } 
  printf("\n");  
 }  
 printf("\n");
}

int main() 
{
  char cadena[]="hola";
  char cadena2[]="mundo";
  imprimir(5,cadena);
  imprimir(4,cadena2);  
}
