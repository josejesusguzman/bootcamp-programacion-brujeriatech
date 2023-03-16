# Ejercicios de algoritmos de lógica de programación

### Psudocódugo. Son las instrucciones quie va a seguir el programa pero son hacerlo

Estos son unos ejemplos y ejercicios de pseudocódigo para mejorar la lógica de programación

1. Encuentra el número más grande
```
Inicializar max = primer elemento de la lista
Para cada número de la lista:
    Si número_actual es mayor a max:
        max = número_actual
Fin del bucle
Imprimimos max
```

2. Promedio de calificaciones
```
Incializar suma = 0
Para cada calificación en la lista de calificaciones:
    suma = suma + calificación
Fin del bucle
promedio = suma / cantidad de calificaciones
Imprimimos promedio

```

3. Detector de palindromos
```
Eliminar espacios de la palabra
Eliminar signos de puntuación
Convertir la frase a solo minúsculas

- Esto es lo de invertir la palabra -
Para cada letra desde la última posición hasta la primera:
    Agrega la letra a palabra_invertida

Inicializar palabra_invertida = Resultad|o de invertir la palabra
Si palabra == palabra_invertida:
    Imprimir "Es palíndromo"
Sino:
    Imprimimos "No es palíndromo"
```

4. Números primos
Un número primo es un número mayor a 1 que tiene únicamente dos divisores positivos: el mismo y 1
El 7 es un número primo porque los únicos dos números enteros que al dividir al 7 nos da un resultado entero y sion residuo son el 7 (el mismo número) y el 1

5. Serie fibonacci
Es una secuencia de números en la que cada número es la suma de los dos anteriores comenzando con un 0 y un 1. Ejemplo:

0, 1, (0 + 1) = 1, (1 + 1)= 2, 

6. Contador de palabras

7. Imprimir todas las tablas de multiplicar del 1 al 10 con un bucle

8. Conversión de temperatura de Celcius a Fahrenheit y viceversa dependiendo de lo que el usuario quiera. Formulas:
   ºF = (ºC · 1.8) + 32
   ºC = (ºF - 32) / 1.8
