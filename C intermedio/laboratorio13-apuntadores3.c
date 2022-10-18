//Programa de ejemplo del uso de apuntadores
#include <stdio.h>

void main(void) 
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
    printf("%s", *(cityPtr+r));
    printf("\n");
  }
}
