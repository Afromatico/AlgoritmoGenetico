Para ejecutar el código se requiere:

	-Python3.6
	-matplotlib
	(opcional Pandas no Testeado)

Para ejecutar el código basta en un shell:

	- ubicar la consola dentro de la carpeta de la Tarea

 	- ejecutar: python -m geneticAlgorithm.main 10 0.1   

El primer parámetro corresponde al tamaño del tablero
Segundo parámetro corresponde a la probabilidad de mutación

El código devuelve un gráfico de matplotlib mostrando numero de reinas que se lograron colocar vs generación, luego imprime en consola la solución como un arreglo de arreglos de casillas y el tiempo que tardo en encontrar la solución.

En esta tarea escogí solucionar el problema de encontrar la configuración tal que se pueda  colocar la maxima cantidad de reinas posibles en un tablero de ajedrez de n dimensiones.
Este problema puede o no tener solución dependiendo la las dimensiones del tablero, y se soluciona mediante un algoritmo de programación genética.

Este algoritmo esta enfocado a ser lo mas genérico posible así que puede no ser muy eficiente a la hora de resolver este problema en especifico.

De los test realizados por lo general demora aproximadamente 14-30 generaciones en encontrar una solución al problema, aun así ocurre menudo que se cae en un mínimo local difícil de salir que toma mas generaciones (50- 130), pasado ese limite opte por iniciar una nueva configuración desde zero.

Por lo mismo explicado anteriormente el tiempo de solución es variable, tomando en torno a 3 segundos si se encuentra dentro de las primeras 30 generaciones, y sumando 20 si esa configuración llego a un mínimo local. 



