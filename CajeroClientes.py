class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)

class Cajera:
    def __init__(self, nombre):
        self.nombre = nombre

    def procesar_compra(self, cliente):
        print(f"\nCajera {self.nombre} procesando la compra de {cliente.nombre}")
        total = 0
        for producto in cliente.carrito:
            print(f"Escaneando producto: {producto.nombre} - Precio: {producto.precio}")
            total += producto.precio
        print(f"Total a pagar: {total}")
        
        pago = float(input("Ingrese la cantidad de dinero: "))
        while pago < total:
            print(f"Falta dinero. Total a pagar: {total}, pagado: {pago}")
            pago += float(input("Ingrese más dinero: "))
        cambio = pago - total
        print(f"Pago recibido: {pago}, Cambio: {cambio:.2f}\n")

def mostrar_menu():
    print("\n--- Menú de productos ---")
    print("1. Cuaderno - $3.50")
    print("2. Lápiz - $0.75")
    print("3. Borrador - $0.50")
    print("4. Tijeras - $2.00")
    print("5. Finalizar compra")

def seleccionar_producto(opcion):
    if opcion == 1:
        return Producto("Cuaderno", 3.50)
    elif opcion == 2:
        return Producto("Lápiz", 0.75)
    elif opcion == 3:
        return Producto("Borrador", 0.50)
    elif opcion == 4:
        return Producto("Tijeras", 2.00)
    else:
        return None

# Simulación
cajera = Cajera("María")
cliente = Cliente("Luis")

while True:
    mostrar_menu()
    opcion = int(input("Seleccione un producto (número): "))
    
    if opcion == 5:
        break
    producto_seleccionado = seleccionar_producto(opcion)
    if producto_seleccionado:
        cliente.agregar_producto(producto_seleccionado)
        print(f"Producto {producto_seleccionado.nombre} agregado al carrito.")
    else:
        print("Opción inválida, intente nuevamente.")

cajera.procesar_compra(cliente)
