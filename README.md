# BlockChain-Simulation
Proyecto que presenta una simulación básica de una red blockchain con múltiples nodos que compiten por la minería de bloques mediante un mecanismo de prueba de trabajo. Cada nodo ejecuta hilos para demostrar el proceso de minería y cómo los bloques son agregados a la cadena de bloques de manera segura mediante un semáforo. 

Descripción
Blockchain Simulation es un proyecto que simula de manera básica el funcionamiento de una red blockchain con múltiples nodos. Cada nodo compite por la minería de bloques utilizando un mecanismo de prueba de trabajo. La simulación incluye la implementación de hilos para demostrar el proceso de minería y cómo los bloques son agregados de manera segura a la cadena de bloques mediante un mecanismo de sección crítica.

Funcionalidades
Minería de Bloques: Cada nodo realiza la minería de bloques mediante un proceso de prueba de trabajo, buscando un hash que cumpla con la dificultad establecida.
Sección Crítica: Se implementa una sección crítica utilizando semáforos para garantizar la exclusividad en la adición de bloques a la cadena de bloques, evitando posibles conflictos.
Hilos Concurrentes: La simulación utiliza hilos (threads) para representar los diferentes nodos de la red blockchain, demostrando la concurrencia en la minería de bloques.

Requisitos
Python 3.x
Bibliotecas estándar de Python (no se requieren instalaciones adicionales)

Instrucciones de Uso
-Clonar el Repositorio
-Ejecutar el Proyecto
-Observar la Simulación (Cada nodo intentará realizar la minería de bloques. La sección crítica garantiza la adición segura de bloques a la cadena de bloques.)

Resultados Finales:
Después de que se alcanza el número objetivo de bloques, se imprimirá la información completa de la cadena de bloques.
