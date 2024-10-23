import tkinter as tk
from tkinter import simpledialog, messagebox
import random

class CallCenterCassette:
    def __init__(self, root):
        self.root = root
        self.root.title("CallCenter Cassette")
        self.root.geometry("400x400")
        self.root.config(bg="purple")  # Fondo morado
        
        # Título
        self.title_label = tk.Label(root, text="CallCenter Cassette", font=("Arial", 20, "bold"), bg="purple", fg="white")
        self.title_label.pack(pady=10)

        # Etiqueta de estado
        self.status_label = tk.Label(root, text="Estado: Inactivo", font=("Arial", 14), bg="purple", fg="white")
        self.status_label.pack(pady=10)
        
        # Botones de control
        self.call_random_button = tk.Button(root, text="Llamar al azar", command=self.call_random, bg="darkorchid", fg="white")
        self.call_random_button.pack(pady=5)
        
        self.dial_button = tk.Button(root, text="Marcar", command=self.dial_number, bg="mediumpurple", fg="black")
        self.dial_button.pack(pady=5)
        
        self.end_call_button = tk.Button(root, text="Terminar llamada", command=self.end_call, bg="indigo", fg="white")
        self.end_call_button.pack(pady=5)

        self.save_sale_button = tk.Button(root, text="Anotar venta", command=self.save_sale, bg="darkviolet", fg="white")
        self.save_sale_button.pack(pady=5)

        self.view_customers_button = tk.Button(root, text="Ver clientes", command=self.view_customers, bg="blueviolet", fg="white")
        self.view_customers_button.pack(pady=5)
        
        # Botón de salir
        self.exit_button = tk.Button(root, text="Salir", command=self.root.quit, bg="grey", fg="white")
        self.exit_button.pack(pady=20)

    # Métodos para las acciones de los botones
    def call_random(self):
        number = random.randint(1000000000, 9999999999)  # Genera un número de teléfono al azar con 10 dígitos
        self.status_label.config(text=f"Llamando a {number}")
        with open("marcados.txt", "a") as file:
            file.write(f"Llamado al número: {number}\n")
        messagebox.showinfo("Llamada", f"Llamando al número {number}")

    def dial_number(self):
        number = simpledialog.askstring("Marcar", "Ingrese el número de teléfono:")
        if number and len(number) == 10 and number.isdigit():
            self.status_label.config(text=f"Marcando {number}")
            with open("marcados.txt", "a") as file:
                file.write(f"Marcado al número: {number}\n")
            messagebox.showinfo("Marcando", f"Marcando el número {number}")
        else:
            messagebox.showerror("Error", "El número debe tener 10 dígitos y ser numérico.")
        
    def end_call(self):
        self.status_label.config(text="Estado: Llamada terminada")
        messagebox.showinfo("Llamada", "Llamada terminada")
    
    def save_sale(self):
        name = simpledialog.askstring("Anotar venta", "Ingrese el nombre del cliente:")
        number = simpledialog.askstring("Anotar venta", "Ingrese el número del cliente:")
        if name and number and len(number) == 10 and number.isdigit():
            with open("clientes.txt", "a") as file:
                file.write(f"Cliente: {name}, Número: {number}\n")
            messagebox.showinfo("Venta anotada", f"Venta anotada para {name} con número {number}")
        else:
            messagebox.showerror("Error", "Debe ingresar un nombre y un número válido de 10 dígitos.")

    def view_customers(self):
        try:
            with open("clientes.txt", "r") as file:
                clientes = file.read()
            with open("marcados.txt", "r") as file:
                marcados = file.read()
            if clientes or marcados:
                messagebox.showinfo("Clientes y números marcados", f"Clientes actuales:\n{clientes}\n\nNúmeros marcados:\n{marcados}")
            else:
                messagebox.showinfo("Clientes y números marcados", "No hay clientes ni números marcados registrados.")
        except FileNotFoundError:
            messagebox.showinfo("Clientes y números marcados", "No hay datos disponibles.")

# Configuración de la ventana principal
root = tk.Tk()
app = CallCenterCassette(root)
root.mainloop()
