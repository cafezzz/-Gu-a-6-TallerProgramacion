import threading
import random
import queue
import time

# Crear una cola para almacenar los números
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

# Crear los hilos
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Iniciar los hilos
producer_thread.start()
consumer_thread.start()

# Esperar a que el productor termine
producer_thread.join()

# Esperar a que todos los elementos sean consumidos
num_queue.join()

print("Finished producing and consuming.")
