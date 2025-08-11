#include <stdio.h>
	int main() {
		int numero1, numero2;

		// Solicitar al usuario que ingrese dos números
		printf("Ingrese el primer número: ");
		scanf("%d", &numero1);
		printf("Ingrese el segundo número: ");
		scanf("%d", &numero2);

		// Comparar los números e imprimir el resultado
		if (numero1 > numero2) {
				printf("El número mayor es: %d\n", numero1);
		} else if (numero2 > numero1) {
			printf("El número mayor es: %d\n", numero2);
		} else {
			printf("Ambos números son iguales.\n");
		}

	return 0;
	}
