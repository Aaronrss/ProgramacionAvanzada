//Libreria de entrada y salida de datos
#include<stdio.h>
//Libreria para el manejo de memoria
#include <stdlib.h>

// Definicion de la estructura de un nodo en un arbol binario
struct nodo {
    int valor;
    struct nodo *izquierda;
    struct nodo *derecha;
};

//Elemento que apunta a la parte inicial del arbol binario
struct nodo *raiz=NULL;



//Insertar nuevo nodo en el arbol binario
void insertarNodo(int numero)
{
    struct nodo *nuevo= malloc(sizeof(struct nodo));
    nuevo->valor = numero;
    nuevo->izquierda = NULL;
    nuevo->derecha = NULL;
    printf("Se inserta el nodo con el valor de %d en el arbol binario\n", numero);
    //No existe ningun elemento en el arbol binario
    if (raiz == NULL)
        raiz = nuevo;
    //Existe uno o mas elementos en el arbol binario   
    else
    {
    	//Indices para el recorrido del arbol binario
        struct nodo *anterior;
		struct nodo *actual;
        anterior = NULL;
        actual = raiz;
        //Recorrido sobre la jerarquia del arbol
        while (actual != NULL)
        {
            anterior = actual;
            /*si el valor es menor optamos 
			por el lado izquierdo del arbol*/
            if (numero < actual->valor)
                actual = actual->izquierda;
            //Obtamos por el lado derecho del arbol    
            else
                actual = actual->derecha;
        }
        //Al llegar al final del arbol insertamos elementos
        if (numero < anterior->valor)
            anterior->izquierda = nuevo;
        else
            anterior->derecha = nuevo;
    }
}

//Se elimina recursivamente todos los subnodos asociados al nodo enviado
void borrarArbol(struct nodo *elemento)
{
    if (elemento != NULL)
    {
    	printf("Eliminar nodo con el valor %d\n", elemento->valor);
        borrarArbol(elemento->izquierda);
        borrarArbol(elemento->derecha);
        free(elemento);
    }
}

//Mostrar los elementos del arbol binario en preorder
void recorridoPreOrder(struct nodo *inicial)
{
	//Se recorre desde el nodo raiz
    if (inicial != NULL)
    {
      /*
      Visitamos primero el nodo raíz, luego recursivamente 
	  realizamos un recorrido en preorden del subárbol izquierdo, 
	  seguido de un recorrido recursivo en preorden del subárbol 
	  derecho
	  */	
      printf(" %d ",inicial->valor);
      recorridoPreOrder(inicial->izquierda);
      recorridoPreOrder(inicial->derecha);
    }
}

//Mostrar los elementos del arbol binario en inorder
void recorridoInOrder(struct nodo *inicial)
{
	//Se recorre desde el nodo raiz
    if (inicial != NULL)
    {
      /*Realizamos recursivamente un recorrido en inorden 
	  en el subárbol izquierdo, visitamos el nodo raíz, 
	  y finalmente hacemos un recorrido recursivo en 
	  inorden del subárbol derecho.*/
      recorridoInOrder(inicial->izquierda);
      printf(" %d ",inicial->valor);
      recorridoInOrder(inicial->derecha);
    }
}


//Mostrar los elementos del arbol binario en postorder
void recorridoPostOrder(struct nodo *inicial)
{
	//Se recorre desde el nodo raiz
    if (inicial != NULL)
    {
      /* Realizamos recursivamente recorridos en postorden 
	  del subárbol izquierdo y del subárbol derecho seguidos 
	  de una visita al nodo raíz.*/	
      recorridoPostOrder(inicial->izquierda);
      recorridoPostOrder(inicial->derecha);
      printf(" %d ",inicial->valor);
    }
}

//Programa principal 
void main() {
   printf("Uso de un arbol binario\n\n");
   printf("Operaciones \"insercion\"\n");
   insertarNodo(10);
   insertarNodo(5);
   insertarNodo(14);
   insertarNodo(7);
   insertarNodo(12);
   printf("\n");
   printf("Operacion \"recorrido preorden\"\n");
   recorridoPreOrder(raiz);
   printf("\n\n");
   printf("Operacion \"recorrido inorder\"\n");
   recorridoInOrder(raiz);
   printf("\n\n");
   printf("Operacion \"recorrido postorder\"\n");
   recorridoPostOrder(raiz);
   printf("\n\n");
   printf("Operaciones \"eliminar\"\n");
   borrarArbol(raiz); 
}







