import threading
import numpy as np
import time

# Inicializar matrices grandes
A = np.random.randint(1, 10, (500, 500))
B = np.random.randint(1, 10, (500, 500))
result = np.zeros((len(A), len(B[0])))

def matrix_multiply_part(start_row, end_row):
    global A, B, result
    for i in range(start_row, end_row):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

# Medir el tiempo de la multiplicación paralela
start_time = time.time()

# Crear hilos para cada cuarto de la matriz
threads = []
num_threads = 4
rows_per_thread = len(A) // num_threads

for i in range(num_threads):
    start_row = i * rows_per_thread
    end_row = (i + 1) * rows_per_thread if i != num_threads - 1 else len(A)
    thread = threading.Thread(target=matrix_multiply_part, args=(start_row, end_row))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

end_time = time.time()
print(f"Time taken for parallel multiplication: {end_time - start_time:.4f} seconds")
