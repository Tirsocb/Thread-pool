# Multiplicación de matrices con Multiprocesamiento

## :arrows_clockwise: Los hilos en Python

El “Threading” es una técnica de programación que permite que una aplicación ejecute simultáneamente varias operaciones en el mismo espacio de proceso. A cada flujo de ejecución que se origina durante el procesamiento se le denomina hilo o subproceso, pudiendo realizar o no una misma tarea. En Python, el módulo “threading” hace posible la programación con hilos.

Ejecutar varios hilos o subprocesos es similar a ejecutar varios programas diferentes al mismo tiempo, pero con algunas ventajas añadidas:

- Los hilos en ejecución de un proceso comparten el mismo espacio de datos que el hilo principal y pueden, por tanto, tener acceso a la misma información o comunicarse entre sí más fácilmente que si estuvieran en procesos separados.
- Ejecutar un proceso de varios hilos suele requerir menos recursos de memoria que ejecutar lo equivalente en procesos separados. 

Permite simplificar el diseño de las aplicaciones que necesitan ejecutar varias operaciones de manera concurrente.

Para cada hilo de un proceso existe un puntero que realiza el seguimiento de las instrucciones que se ejecutan en cada momento. Además, la ejecución de un hilo se puede detener temporalmente o de manera indefinida. En general, un proceso sigue en ejecución cuando al menos uno de sus hilos permanece activo, es decir, cuando el último hilo concluye su cometido, termina el proceso, liberándose en ese momento todos los recursos utilizados.

## :beginner: Objetos Thread: los hilos

En Python un objeto “Thread” representa una determinada operación que se ejecuta como un subproceso independiente, es decir, es la representación de un hilo. Se pueden definir de dos formas los hilos:

- La primera consiste en pasar al método constructor un objeto invocable, como una función, que es llamada cuando se inicia la ejecución del hilo.
- La segunda sería creando una subclase de “Thread” en la que se reescribe el método `run()` y/o el constructor `__init__()`.

Los threads:

1. Utilizan el argumento `target` para establecer el nombre de la función a la que hay que llamar. 
2. Una vez que los hilos se hayan creado se iniciarán con el método `start()`. 
3. A todos los hilos se les asigna, automáticamente, un nombre en el momento de la creación que se puede conocer con el método `getName()`. 
4. un identificador único (en el momento que son iniciados) que se puede obtener accediendo al valor del atributo `ident`.
5. Los hilos se crean e inician implementando un bucle basado en `range()`.
6. Una posibilidad de asignar un nombre a un hilo con el método `hilo.setName(nombre)` y de acceder a su nombre mediante `hilo.name`.

### Ejemplo

```python
import threading

for num_hilo in range(NUM_HILOS):
hilo = threading.Thread(name='hilo%s' %num_hilo,
target=contar)
hilo.start()
```

## :round_pushpin: Hilos con argumentos

Tenemos la posibilidad de enviar valores a los hilos para que los puedan utilizar. Por este motivo existen los argumentos `args` y `kwargs` en el constructor.

### Ejemplo

```python
for num_hilo in range(3):
hilo = threading.Thread(target=contar, args=(num_hilo,)
,kwargs={'inicio':0, 'incremento':1,'limite':10})
hilo.start()
```

## :chart_with_downwards_trend: Multiplicación de Matrices

Multiplicar dos matrices es bastante simple. Se selecciona una fila de la primera matriz y una columna de la segunda matriz y se multiplican los elementos correspondientes y añadirlos a obtener el primer elemento, para luego pasar a la siguiente columna haga lo mismo para obtener el siguiente elemento y así sucesivamente.

Aquí, uno podría notar que dadas dos matrices **A(mXn)** y **B(nXr)** y su matriz de suma resultante **C(mXr)**, para obtener el elemento **C(i,j)** uno solo necesita considerar la i-ésima fila de la matriz A y j-ésima columna de la matriz B para obtener el elemento requerido de la matriz C. Por lo tanto, podemos hacerlo de forma aislada del resto de los elementos. Y por lo tanto, no importa si hemos calculado el elemento **C(1,1)** para calcular el elemento **C(1,2)**.

Por lo tanto, se puede dividir el programa en diferentes procesos y ejecutarlos en diferentes procesadores.

Ahora, aunque suene bastante simple, debemos tener cuidado con algunas cosas al implementar esto en el código. Una de las primeras cosas es decidir qué cálculos se ejecutarán en qué núcleo. Puede decidir dividir las matrices por filas o por columnas. Deberíamos hacerlo en fila. es decir, primero tomamos la primera matriz y tomamos un número definido de sus filas y lo multiplicamos con todas las columnas en la segunda matriz y hacemos esto simultáneamente para diferentes filas en diferentes núcleos.

Una forma de implementar esta función es comenzar la primera división de 0 a r, donde r se puede calcular por división de enteros

`(filas totales / número de procesadores)`

La siguiente división sería

`r a r + (filas totales / número de procesadores) `

Donde las filas totales ahora son **las 
filas totales antes menos el número de filas que ya se ejecutarán**, y tenemos un procesador menos y así sucesivamente.

### Ejemplo

- Número de procesadores, N = 4.

- Filas en total, R = 7.

- La primera división será de 0 a (7/4) es decir, 0 a 1.

- Ahora R = R - 1 = 6 y N = N - 1 = 3.

- La segunda división será de 1 a 1+ (6/3 ) es decir, 1 a 3. 

- Ahora R = R - 2 = 4, N = N - 1 = 2.

- La tercera división será de 3 a 3 + (4/2) es decir, 3 a 5.

- Ahora R = R - 2 = 2, N = N - 1 = 1.

- La cuarta división será de 5 a 5 + (2/1) es decir, de 5 a 7.

- La división en segmentos será de: (0 a 1), (1 a 3), (3 a 5) y (5 a 7).

En código de Python, sería.

```python
for i in range(0, size): # size es el número de cores, n es el tamaño de la matriz
    int limite_inferior = (n / size) * i 
    int limite_superior = (n / size) * (i + 1)
```

Dados cuatro núcleos debería aumentar el rendimiento del algoritmo en cuatro, sin embargo, hay gastos generales adicionales cuando intentamos ejecutar los procesos en paralelo. Por ejemplo, tenemos que generar múltiples procesos y hacer un procesamiento adicional, ya que en este caso dividimos las filas de la matriz para ejecutarlas en diferentes procesadores. Además, dado que escribiremos en otra matriz, puede haber conflictos al escribir los resultados, por lo que también puede provocar una desaceleración. Otra razón puede ser que los procesos tarden diferentes tiempos en ejecutarse, en el ejemplo anterior, no todas las filas tienen el mismo tamaño, por lo que la ejecución requiere un tiempo diferente.

Ejecutar el cálculo paralelo da como resultado el uso de los cuatro núcleos. Puedes verlo en la captura de pantalla a continuación.

![Screenshot](https://github.com/Tirsocb/Thread-pool/blob/main/img/Screenshot%20from%202021-04-16%2011-23-45.png)

Hemos ejecutado el programa para multiplicar matrices y también nos aseguramos de que realmente se ejecute en múltiples procesadores.

## :bulb: How to use

Para usar este programa, es necesario hacer `git clone` y luego `cd ` al folder que contiene el repo.

```git
git clone https://github.com/Tirsocb/Thread-pool.git
cd Thread-pool 
```
Luego ejecutar

```git
python3 matmul.py matA.csv matB.csv 4 output.csv
```

Estos corresponden a

```git
python3 matmul.py <Matrix_A.csv> <Matrix_B.csv> <Pool size o cores> <Output_File.csv>
```
1. Los archivos de entrada
2. El pool size: tamaño del pool a utilizar
3. El nombre del archivo de salida

## :white_check_mark: Resultado

El programa muestra los resultados de la multiplicación de matrices de forma paralela. También muestra el tiempo que se tarda (en s) en ejecutar las multiplicaciones y el número de cores utilizados en un archivo `.csv`.

## :man_technologist: Developers 

[Tirso Córdova](https://github.com/Tirsocb) :robot:

[Abner Xocop Chacach](https://github.com/abnerxch) :ghost:

# REPL
[Open project on Repl](https://replit.com/join/ddtyhmcp-tirsocb)

# :shipit: Referencias

[Javier Ceballos Fernández](https://www.redeszone.net/2017/07/13/curso-python-volumen-xx-hilos-parte-i/)

[khalidgt95](https://github.com/khalidgt95/Python-MultiThreading/blob/master/Matrix%20Multiplication.py)

# :open_file_folder: License
[MIT](https://choosealicense.com/licenses/mit/)
