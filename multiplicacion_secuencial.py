import numpy as np
import time

# Función para multiplicar dos matrices de manera secuencial
def matrix_multiply_sequential(A, B):
    result = np.zeros((len(A), len(B[0])))
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Inicializar matrices grandes
A = np.random.randint(1, 10, (500, 500))
B = np.random.randint(1, 10, (500, 500))

# Medir el tiempo de la multiplicación secuencial
start_time = time.time()
C_sequential = matrix_multiply_sequential(A, B)
end_time = time.time()

print(f"Time taken for sequential multiplication: {end_time - start_time:.4f} seconds")
