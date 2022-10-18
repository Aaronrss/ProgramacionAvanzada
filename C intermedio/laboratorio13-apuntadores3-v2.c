//Programa de ejemplo del uso de apuntadores
#include <stdio.h>
#include <string.h>

int main() 
{
  char *cityPtr[4] = {
    "puebla",
    "tlaxcala",
    "nayarit",
    "colima"
  };
  int r;
  for (r = 0; r < 4; r++) 
  {
    int len1, len2 = strlen(*(cityPtr+r));
    char *ptr=&((*(cityPtr+r))-1);
    printf("%s", *(cityPtr+r));
    printf("\n");
    for(len1 = len2; len1 >= 0 ; len1--)
      //por qué aquí %c, es por el puntero?
      printf("%c", *ptr--);
  }
}
