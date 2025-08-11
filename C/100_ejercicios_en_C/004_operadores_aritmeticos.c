#include <stdio.h>

int main() {
	int numero1, numero2;
	int suma, resta, multiplicacion, division, modulo;

	// Solicitar al usuario que ingrese dos números
	printf("Ingrese el primer número: ");
	scanf("%d", &numero1);
	printf("Ingrese el segundo número: ");
	scanf("%d", &numero2);

	// Realizar operaciones aritméticas
	suma = numero1 + numero2;
	resta = numero1 - numero2;
	multiplicacion = numero1 * numero2;
	division = numero1 / numero2; // Nota: esto realizará una división entera
	modulo = numero1 % numero2; // Nota: esto es el residuo de la división entera

	// Mostrar resultados
	printf("Suma: %d + %d = %d\n", numero1, numero2, suma);
	printf("Resta: %d - %d = %d\n", numero1, numero2, resta);
	printf("Multiplicación: %d * %d = %d\n", numero1, numero2, multiplicacion);
	printf("División: %d / %d = %d\n", numero1, numero2, division);
	printf("Módulo: %d %% %d = %d\n", numero1, numero2, modulo);

	return 0;

}
