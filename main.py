import hashlib
import threading
import time
import binascii

# Configuración global
num_nodos = 5
dificultad = int("00000fffff000000000000000000000000000000000000000000000000000000", 16)
bloques_objetivo = 10
semaforo = threading.Semaphore(1)
cadena_de_bloques = []

class Bloque:
    def __init__(self, indice, marca_de_tiempo, hash_bloque, hash_anterior, minero):
        self.indice = indice
        self.marca_de_tiempo = marca_de_tiempo
        self.hash_bloque = hash_bloque
        self.hash_anterior = hash_anterior
        self.minero = minero

def prueba_de_trabajo(identificador_nodo):
    while True:
        nonce = 0
        marca_de_tiempo = int(time.time() * 1e9)
        datos_hash = (
            format(identificador_nodo, '08x') +
            format(nonce, '08x') +
            format(marca_de_tiempo, '016x')
        )

        while int(hashlib.sha256(binascii.unhexlify(datos_hash)).hexdigest(), 16) >= dificultad:
            nonce += 1
            datos_hash = (
                format(identificador_nodo, '08x') +
                format(nonce, '08x') +
                format(marca_de_tiempo, '016x')
            )

        return (
            hashlib.sha256(binascii.unhexlify(datos_hash)).hexdigest(),
            nonce,
            marca_de_tiempo / 1e9
        )

def seccion_critica(identificador_nodo, hash_bloque, semaforo):
    print(f"Nodo {identificador_nodo} está entrando en la sección crítica.")
    semaforo.acquire()

    bloque_anterior = None
    if cadena_de_bloques:
        bloque_anterior = cadena_de_bloques[-1]

    nuevo_bloque = Bloque(
        indice=len(cadena_de_bloques),
        marca_de_tiempo=int(time.time()),
        hash_bloque=hash_bloque,
        hash_anterior=bloque_anterior.hash_bloque if bloque_anterior else None,
        minero=identificador_nodo
    )

    cadena_de_bloques.append(nuevo_bloque)
    print(f"Nodo {identificador_nodo} creó un nuevo bloque: {nuevo_bloque.indice}")

    # Simula trabajo en el bloque
    time.sleep(2)

    semaforo.release()
    print(f"Nodo {identificador_nodo} liberó el semáforo.")

def ejecutar_nodo(identificador_nodo, semaforo):
    print(f"Nodo {identificador_nodo} está iniciando.")
    while len(cadena_de_bloques) < bloques_objetivo:
        resultado = prueba_de_trabajo(identificador_nodo)
        print(f"Nodo {identificador_nodo} completó la prueba de trabajo con hash {resultado[0]}")

        if int(resultado[0], 16) < dificultad:
            seccion_critica(identificador_nodo, resultado[0], semaforo)
        else:
            print(f"Nodo {identificador_nodo} falló la prueba de trabajo, intentando de nuevo.")

def main():
    hilos = []

    for i in range(num_nodos):
        hilo = threading.Thread(target=ejecutar_nodo, args=(i + 1, semaforo))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("RESULTADOS FINALES")
    
    # Imprime información de la cadena de bloques
    for bloque in cadena_de_bloques:
        print(f"Índice: {bloque.indice}, Marca de tiempo: {bloque.marca_de_tiempo}, Hash: {bloque.hash_bloque}, Minero: {bloque.minero}, Hash Anterior: {bloque.hash_anterior}")

if __name__ == "__main__":
    main()
