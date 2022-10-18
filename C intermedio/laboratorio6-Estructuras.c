#include <stdio.h>
#include <string.h>
 
struct libros {
   char  titulo[50];
   char  autor[50];
   char  resumen[100];
   int   libro_id;
};
 
int main( ) {

   struct libros libro1;     
   struct libros libro2;        
   // strcpy() is defined in the <string.h> header file
   // Copies the string pointed by source (including the null character) to the destination.
   // Also returns the copied string
   strcpy( libro1.titulo, "C Programming");
   strcpy( libro1.autor, "Nuha Ali"); 
   strcpy( libro1.resumen, "C Programming Tutorial");
   libro1.libro_id = 6495407;

   strcpy( libro2.titulo, "Telecom Billing");
   strcpy( libro2.autor, "Zara Ali");
   strcpy( libro2.resumen, "Telecom Billing Tutorial");
   libro2.libro_id = 6495700;
 
   printf( "Libro 1 titulo : %s\n", libro1.titulo);
   printf( "Libro 1 autor : %s\n", libro1.autor);
   printf( "Libro 1 resumen : %s\n", libro1.resumen);
   printf( "Libro 1 libro_id : %d\n", libro1.libro_id);


   printf( "Libro 2 titulo : %s\n", libro2.titulo);
   printf( "Libro 2 autor : %s\n", libro2.autor);
   printf( "Libro 2 resumen : %s\n", libro2.resumen);
   printf( "Libro 2 libro_id : %d\n", libro2.libro_id);

   return 0;
}
