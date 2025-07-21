#include <stdio.h>

int main(){
	int numero1, numero2, suma;

	// Solicitar al usuario que ingrese dos números
	printf("Ingrese el primer número: ");
	scanf("%d", &numero1);
	printf("Ingrese el segundo número: ");
	scanf("%d", &numero2);

	// Calcular la suma de los números
	suma = numero1 + numero2;

	// Mostrar el resultado
	printf("La suma de %d y %d es %d\n", numero1, numero2, suma);

	return 0;
}
