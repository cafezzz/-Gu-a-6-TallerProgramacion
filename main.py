import threading
import random
import queue
import numpy as np
import time

# Productor/Consumidor
num_queue = queue.Queue()

def producer():
    for _ in range(10):  # Generar 10 números aleatorios
        num = random.randint(1, 100)
        print(f"Producing: {num}")
        num_queue.put(num)
        time.sleep(0.5)  # Esperar un poco antes de producir el siguiente número

def consumer():
    for _ in range(10):
        num = num_queue.get()
        result = num * 2
        print(f"Consuming: {num} -> Result: {result}")
        num_queue.task_done()

# Multiplicación de Matrices Secuencial
def matrix_multiply_sequential(A, B):
    result = np.zeros((len(A), len(B[0])))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Multiplicación de Matrices Paralela
def matrix_multiply_part(start_row, end_row):
    global A, B, result
    for i in range(start_row, end_row):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

# Método main
def main():
    # Productor/Consumidor
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Iniciar hilos
    producer_thread.start()
    consumer_thread.start()

    # Esperar a que el productor termine
    producer_thread.join()
    num_queue.join()  # Esperar a que todos los elementos sean consumidos

    print("Finished producing and consuming.")

    # Multiplicación de Matrices Secuencial
    A = np.random.randint(1, 10, (500, 500))
    B = np.random.randint(1, 10, (500, 500))

    start_time = time.time()
    C_sequential = matrix_multiply_sequential(A, B)
    end_time = time.time()
    print(f"Time taken for sequential multiplication: {end_time - start_time:.4f} seconds")

    # Multiplicación de Matrices Paralela
    global result
    result = np.zeros((len(A), len(B[0])))

    start_time = time.time()
    threads = []
    num_threads = 4
    rows_per_thread = len(A) // num_threads

    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i != num_threads - 1 else len(A)
        thread = threading.Thread(target=matrix_multiply_part, args=(start_row, end_row))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken for parallel multiplication: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
