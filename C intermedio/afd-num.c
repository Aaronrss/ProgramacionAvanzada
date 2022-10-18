#include <stdio.h>
#include <string.h>

char cadena[80]={"< > ; <= a == x >= ) !="}

int main(void){
	int ind=0;
	int n, edo=0;
	n = strlen(cadena);
	while(ind < n){
		switch(edo){
			case 0:
				if(cadena[ind]=='<'){
					edo=1;
				}
				else {
					if(cadena[ind]=='='){
						edo=2;
					}
					else{
						if(cadena[ind]=='!'){
							edo=3;
						}
						else{
							printf("No se reconoce%c\n", );
						}
					}
				}
		}
	}
	return 0;
}