#include <stdio.h>
struct operacion
{
	int valor1,valor2;
	float valor3;
};
void visualizar(struct operacion); //esto es un constructor?
void main(){
	struct operacion numerica;
	printf("Valor1: \n");
	scanf("%d",&numerica.valor1);
	printf("Valor2: \n");
	scanf("%d",&numerica.valor2);
	printf("Valor3: \n");
	scanf("%f",&numerica.valor3);
	visualizar(numerica);
}
void visualizar(struct operacion numerica){
	printf("Resultado: %f",((numerica.valor1*numerica.valor2)/numerica.valor3));
}

