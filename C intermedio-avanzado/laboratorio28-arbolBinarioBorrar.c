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

/* Dado un arbol binario (que no esta vacio), se regresa el nodo 
   con el minimo valor en el arbol. No es necesario recorrer
   todo la estructura*/
struct nodo *NodoMenor(struct nodo* elemento) 
{ 
    struct nodo *actual = elemento; 
    /* Recorrer el arbol hasta encontrar el nodo mas 
	profundo del lado izquierdo.
	
	En el arbol binario, los elemento menores siempre
	estan del lado izquierdo */
    while (actual && actual->izquierda != NULL) 
        actual = actual->izquierda; 
    return actual; 
} 

//Se elimina recursivamente todos los subnodos asociados al nodo enviado
struct nodo* borrarNodo(struct nodo* inicio, int valor)
{
    //Caso base
     if (inicio == NULL) 
	 	return inicio;
	
	/* Si el valor a eliminar es menor que el nodo inicio
	entonces este esta del lado izquierdo del arbol binario*/
    if (valor < inicio->valor) 
        inicio->izquierda = borrarNodo(inicio->izquierda, valor);
		
	/* Si el valor a eliminar es mayor que el nodo inicio 
	entonces este esta del lado derecho del arbol binario*/  
    else if (valor > inicio->valor) 
        inicio->derecha = borrarNodo(inicio->derecha, valor);
	
    /*Si el valor es igual al nodo inicio entonces este es 
	el nodo a eliminar*/
    else
    { 
       printf("Se borra el nodo con el valor de %d en el arbol binario\n", valor);
       //Nodo con solo un hijo o sin hijos 
        if (inicio->izquierda == NULL) 
        { 
            struct nodo *temporal = inicio->derecha; 
            free(inicio); 
            return temporal; 
        } 
        else if (inicio->derecha == NULL) 
        { 
            struct nodo *temporal = inicio->izquierda; 
            free(inicio); 
            return temporal; 
        } 
        
        /* Nodo con dos hijos: se obtiene el nodo sucesor en modo inorder 
		(el menor en el lado derecho del arbol)*/ 
        struct nodo* temporal = NodoMenor(inicio->derecha); 
  
        // Se copia el valor (contenido) del nodo sucesor
        inicio->valor = temporal->valor; 
  
        // Delete the inorder successor 
        //Se borra el nodo sucesor
        inicio->derecha=borrarNodo(inicio->derecha, temporal->valor);
    }
    return inicio; 
}

//Mostrar los elementos del arbol binario en preorder
void recorridoPreOrder(struct nodo *inicial)
{
	//Se recorre desde el nodo raiz
    if (inicial != NULL)
    {
      /*
      Visitamos primero el nodo ra�z, luego recursivamente 
	  realizamos un recorrido en preorden del sub�rbol izquierdo, 
	  seguido de un recorrido recursivo en preorden del sub�rbol 
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
	  en el sub�rbol izquierdo, visitamos el nodo ra�z, 
	  y finalmente hacemos un recorrido recursivo en 
	  inorden del sub�rbol derecho.*/
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
	  del sub�rbol izquierdo y del sub�rbol derecho seguidos 
	  de una visita al nodo ra�z.*/	
      recorridoPostOrder(inicial->izquierda);
      recorridoPostOrder(inicial->derecha);
      printf(" %d ",inicial->valor);
    }
}

//Programa principal 
void main() {
   printf("Uso de un arbol binario\n\n");
   printf("Operaciones \"insercion\"\n");
   insertarNodo(50);
   insertarNodo(30);
   insertarNodo(20);
   insertarNodo(40);
   insertarNodo(70);
   insertarNodo(60);
   insertarNodo(80);
   printf("Operacion \"recorrido preorden\"\n");
   recorridoPreOrder(raiz);
   printf("\n");
   printf("Operacion \"recorrido inorder\"\n");
   recorridoInOrder(raiz);
   printf("\n");
   printf("Operacion \"recorrido postorder\"\n");
   recorridoPostOrder(raiz);
   printf("\n");
   printf("Operacion \"eliminar\"\n");
   borrarNodo(raiz, 20);
   printf("Operacion \"recorrido inorder\"\n");
   recorridoInOrder(raiz);
   printf("\n");
   printf("Operacion \"eliminar\"\n");
   borrarNodo(raiz, 30);
   printf("Operacion \"recorrido inorder\"\n");
   recorridoInOrder(raiz);
   printf("\n");
   printf("Operacion \"eliminar\"\n");
   borrarNodo(raiz, 50);
   printf("Operacion \"recorrido inorder\"\n");
   recorridoInOrder(raiz);
}