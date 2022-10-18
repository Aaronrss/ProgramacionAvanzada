// Libreria de entrada y salida de datos
#include <stdio.h>
// Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de los elementos contenidos en la tabla hash
struct hash
{
	int valor;
	int llave;
};

// Variables globales

// Tabla contenedora de elementos
struct hash *tabla;
int capacidad = 10;
int longitud = 0;

// Funcion que obtiene un valor unico para la tabla hash
int codigoHash(int llave)
{
	return (llave % capacidad);
}

// Inicializacion de la tabla hash
void inicializarHash()
{
	int x;
	printf("Se inicializa la tabla hash con %d espacios disponibles\n", capacidad);
	tabla = malloc(capacidad * sizeof(struct hash));
	for (x = 0; x < capacidad; x++)
	{
		tabla[x].llave = 0;
		tabla[x].valor = 0;
	}
}

void insertar(int llave, int valor)
{
	// Se obtiene el codigo hash de la llave
	int indice = codigoHash(llave);

	// La llave no existe, por lo que se inserta en la tabla hash
	if (tabla[indice].valor == 0)
	{
		tabla[indice].llave = llave;
		tabla[indice].valor = valor;
		longitud++;
		printf("En la llave \'%d\' se inserta el valor \'%d\'\n", llave, valor);
	}
	// Se actualiza el valor de una llave existente
	else if (tabla[indice].llave == llave)
	{
		printf("La llave \'%d\' existe, por lo que se actualiza su valor a \'%d\'\n", llave, valor);
		tabla[indice].valor = valor;
	}
	else
		printf("El elemento no se puede insertar en la tabla hash\n");
}

/* Remueve una llave especifica de una tabla hash*/
void eliminar(int llave)
{
	// Se obtiene el codigo hash de la llave
	int indice = codigoHash(llave);
	// La llave no existe
	if (tabla[indice].valor == 0)
		printf("No se puede eliminar la llave \'%d\' ya que no existe en la tabla hash\n", llave);
	// La llave y el valor existen en la tabla hash
	else
	{
		printf("Se elimina la llave \'%d\' y el valor \'%d\' de la tabla hash\n", llave, tabla[indice].valor);
		tabla[indice].llave = 0;
		tabla[indice].valor = 0;
		longitud--;
	}
}

// Se muestran todos los elementos de la tabla hash
void mostrar()
{
	int x;
	printf("Elementos en la tabla hash\n");
	for (x = 0; x < capacidad; x++)
	{
		if (tabla[x].valor != 0)
			printf("Posicion[%d]: llave \'%d\', valor \'%d\' \n", x + 1, tabla[x].llave, tabla[x].valor);
	}
}

// Eliminar de memoria la tabla hash
void eliminarHash()
{
	free(tabla);
	return;
}

// Funcion principal
int main()
{
	inicializarHash();
	printf("Uso de una tabla hash\n\n");
	printf("Operaciones \"insercion\"\n");
	insertar(1, 100);
	insertar(3, 101);
	insertar(2, 200);
	insertar(114, 201);
	printf("\n");
	printf("Operacion \"mostrar elementos\"\n");
	mostrar();
	printf("\n");
	printf("Operaciones \"eliminacion\"\n");
	eliminar(100);
	eliminar(3);
	printf("\n");
	printf("Operacion \"mostrar elementos\"\n");
	mostrar();
	eliminarHash();
}
