import tkinter as tk
from tkinter import ttk, messagebox

# Clases del sistema de gestión de productos y órdenes
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"Nombre del producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria.nombre}"

class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Nombre: {self.nombre} {self.apellido}, ID: {self.id_cliente}"

class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0.0

    def agregar_item(self, item):
        self.items.append(item)
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(item.calcular_subtotal() for item in self.items)

    def mostrar_info(self):
        items_info = "\n".join(item.mostrar_info() for item in self.items)
        return (f"Orden de {self.cliente.nombre} {self.cliente.apellido}\n{items_info}\nTotal: {self.total}")

class ItemOrden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.producto.precio * self.cantidad

    def mostrar_info(self):
        return f"Item: {self.producto.nombre}, Cantidad: {self.cantidad}, Subtotal: {self.calcular_subtotal()}"

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Categoria: {self.nombre}"

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []
        self.categorias = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def crear_orden(self, cliente):
        orden = Orden(cliente)
        self.ordenes.append(orden)
        return orden

    def mostrar_productos(self):
        return "\n".join(producto.mostrar_info() for producto in self.productos)

# Funciones de la GUI
def registrar_producto():
    categoria = next((c for c in tienda.categorias if c.nombre == combobox_categoria.get()), None)
    if categoria:
        producto = Producto(entry_producto_nombre.get(), float(entry_producto_precio.get()), categoria)
        tienda.registrar_producto(producto)
        messagebox.showinfo("Registro", "Producto registrado con éxito")
    else:
        messagebox.showerror("Error", "Categoría no encontrada")

def registrar_cliente():
    cliente = Cliente(entry_cliente_nombre.get(), entry_cliente_apellido.get(), entry_id_cliente.get())
    tienda.registrar_cliente(cliente)
    messagebox.showinfo("Registro", "Cliente registrado con éxito")

def agregar_item_a_orden():
    cliente = next((c for c in tienda.clientes if f"{c.nombre} {c.apellido}" == combobox_cliente.get()), None)
    producto = next((p for p in tienda.productos if p.nombre == combobox_producto.get()), None)
    if cliente and producto:
        cantidad = int(entry_cantidad.get())
        item = ItemOrden(producto, cantidad)
        orden = next((o for o in tienda.ordenes if o.cliente == cliente), None)
        if not orden:
            orden = tienda.crear_orden(cliente)
        orden.agregar_item(item)
        messagebox.showinfo("Registro", "Item agregado a la orden con éxito")
    else:
        messagebox.showerror("Error", "Cliente o producto no encontrado")

def mostrar_info_productos():
    info_productos = tienda.mostrar_productos()
    messagebox.showinfo("Productos en la tienda", info_productos if info_productos else "No hay productos registrados")

def mostrar_info_ordenes():
    info_ordenes = "\n\n".join(orden.mostrar_info() for orden in tienda.ordenes)
    messagebox.showinfo("Ordenes en la tienda", info_ordenes if info_ordenes else "No hay órdenes registradas")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Tienda")
ventana.configure(bg="light goldenrod")

tienda = Tienda()

# Categorías predefinidas
categoria1 = Categoria("Periféricos")
categoria2 = Categoria("Tarjetas de video")
tienda.categorias.append(categoria1)
tienda.categorias.append(categoria2)

# Widgets para registrar productos
tk.Label(ventana, text="Registrar Producto", bg="light goldenrod").grid(row=0, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=1, column=0)
entry_producto_nombre = tk.Entry(ventana)
entry_producto_nombre.grid(row=1, column=1)

tk.Label(ventana, text="Precio:", bg="light goldenrod").grid(row=2, column=0)
entry_producto_precio = tk.Entry(ventana)
entry_producto_precio.grid(row=2, column=1)

tk.Label(ventana, text="Categoría:", bg="light goldenrod").grid(row=3, column=0)
combobox_categoria = ttk.Combobox(ventana, values=[c.nombre for c in tienda.categorias])
combobox_categoria.grid(row=3, column=1)

btn_registrar_producto = tk.Button(ventana, text="Registrar Producto", command=registrar_producto)
btn_registrar_producto.grid(row=4, column=0, columnspan=2)

# Widgets para registrar clientes
tk.Label(ventana, text="Registrar Cliente", bg="light goldenrod").grid(row=5, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=6, column=0)
entry_cliente_nombre = tk.Entry(ventana)
entry_cliente_nombre.grid(row=6, column=1)

tk.Label(ventana, text="Apellido:", bg="light goldenrod").grid(row=7, column=0)
entry_cliente_apellido = tk.Entry(ventana)
entry_cliente_apellido.grid(row=7, column=1)

tk.Label(ventana, text="ID Cliente:", bg="light goldenrod").grid(row=8, column=0)
entry_id_cliente = tk.Entry(ventana)
entry_id_cliente.grid(row=8, column=1)

btn_registrar_cliente = tk.Button(ventana, text="Registrar Cliente", command=registrar_cliente)
btn_registrar_cliente.grid(row=9, column=0, columnspan=2)

# Widgets para agregar items a orden
tk.Label(ventana, text="Agregar Item a Orden", bg="light goldenrod").grid(row=10, column=0, columnspan=2)
tk.Label(ventana, text="Cliente:", bg="light goldenrod").grid(row=11, column=0)
combobox_cliente = ttk.Combobox(ventana, values=[f"{c.nombre} {c.apellido}" for c in tienda.clientes])
combobox_cliente.grid(row=11, column=1)

tk.Label(ventana, text="Producto:", bg="light goldenrod").grid(row=12, column=0)
combobox_producto = ttk.Combobox(ventana, values=[p.nombre for p in tienda.productos])
combobox_producto.grid(row=12, column=1)

tk.Label(ventana, text="Cantidad:", bg="light goldenrod").grid(row=13, column=0)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=13, column=1)

btn_agregar_item = tk.Button(ventana, text="Agregar Item", command=agregar_item_a_orden)
btn_agregar_item.grid(row=14, column=0, columnspan=2)

# Botones para mostrar información
btn_mostrar_productos = tk.Button(ventana, text="Mostrar Productos", command=mostrar_info_productos)
btn_mostrar_productos.grid(row=15, column=0, columnspan=2)

btn_mostrar_ordenes = tk.Button(ventana, text="Mostrar Órdenes", command=mostrar_info_ordenes)
btn_mostrar_ordenes.grid(row=16, column=0, columnspan=2)

ventana.mainloop()

