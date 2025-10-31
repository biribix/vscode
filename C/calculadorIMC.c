#include <stdio.h>
#include <math.h>

int main() {
    float peso, altura, IMC;

    printf("Introduce tu peso en kg: ");
    scanf("%f", &peso);

    printf("Introduce tu altura en m: ");
    scanf("%f", &altura);

    altura = altura * altura;
    IMC = roundf((peso / altura) * 100) / 100;  // redondea a 2 decimales

    printf("Tu IMC es: %.2f\n", IMC);

    if (IMC <= 18.5) {
        printf("Bajo peso\n");
    } else if (IMC <= 24.9) {
        printf("Peso saludable\n");
    } else if (IMC <= 29.9) {
        printf("Sobrepeso\n");
    } else if (IMC >= 30) {
        printf("Obesidad\n");
    }

    return 0;
}
