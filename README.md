# TP1 Lado B: Algoritmos Genéticos

## Integrantes:
* Cupitó, Felipe
* De Luca, Juan Manuel
* Finucci Roca, Hernán
* Kim, Azul
* Konfederak, Sol

## Consgina:
Queremos ayudar a los artistas a lograr ése color que tiene en mente con una paleta limitada. Para ello, contaremos como input del usuario (el artista!) su paleta de colores y el color deseado; y buscamos implementar un sistema que, mediante una implementación de Algoritmos Genéticos, logre encontrar la forma de mezclar proporciones de los diferentes colores de su paleta para lograr el color que más se le acerque al color deseado

## Guía de instalación
Para poder correr el proyecto es necesario tener instalado:
* Python 3
* NumPy
* Matplotlib

Para instalar las librerías:
```
pip install numpy
pip install matplotlib
```

## Configuración
Se encuentra provisto un archivo de configuración config.json. En este, se puede alterar los parámetros que se encuentren allí. Se debe tener en cuenta:
* file: archivo del cual se extraen los colores. La primera línea es para el color objetivo y las demás corresponden a la paleta de colores
* selection: método de selección. Los tipos de selección disponibles son "elite", "roulette" y "rank". Si se introduce otro parámetro que no sean los mencionados, se utilizará por default el rank.
* max_generations: cantidad máxima de generaciones que se pueden generar.
* expected_fitness: valor para determinar a partir de qué valor se puede satisfacer al usuario con respecto al fitness. Es un valor entre el 0 y el 1. El valor default es 0.95. Si es que quiere que el algoritmo intente de llegar exactamente al color objetivo, setee el valor en 1.
Los últimos dos parámetros son condiciones de corte para el algoritmo.

## Ejecución
Para ejecutar el algoritmo:
```
python3 main.py
```
o
```
python main.py
```