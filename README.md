# TP1 Lado B: Algoritmos Genéticos

## Integrantes:
* Cupitó, Felipe
* De Luca, Juan Manuel
* Finucci Roca, Hernán
* Kim, Azul
* Konfederak, Sol

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