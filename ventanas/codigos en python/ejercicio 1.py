import tkinter as tk
from tkinter import ttk, messagebox

# Clases de Biblioteca
class Libro:
    def __init__(self, titulo, id, autor, categoria):
        self.titulo = titulo
        self.id = id
        self.autor = autor
        self.categoria = categoria

    def mostrar_info(self):
        return f"Titulo: {self.titulo}\nId: {self.id}\nAutor: {self.autor.nombre} {self.autor.apellido}\nCategoria: {self.categoria.nombre}"

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Usuario:
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario

    def mostrar_info(self):
        return f"Usuario: {self.nombre} {self.apellido}, Id: {self.id_usuario}"

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        return (f"Prestamo\n{self.libro.mostrar_info()}\n{self.usuario.mostrar_info()}\n"
                f"Fecha prestamo: {self.fecha_prestamo}\nFecha devolucion: {self.fecha_devolucion}")

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def realizar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)

    def mostrar_libros(self):
        return "\n".join(libro.mostrar_info() for libro in self.libros)

# Funciones de la GUI
def registrar_libro():
    autor = Autor(entry_autor_nombre.get(), entry_autor_apellido.get())
    categoria = Categoria(entry_categoria.get())
    libro = Libro(entry_titulo.get(), entry_id_libro.get(), autor, categoria)
    biblioteca.registrar_libro(libro)
    messagebox.showinfo("Registro", "Libro registrado con éxito")

def registrar_usuario():
    usuario = Usuario(entry_usuario_nombre.get(), entry_usuario_apellido.get(), entry_id_usuario.get())
    biblioteca.registrar_usuario(usuario)
    messagebox.showinfo("Registro", "Usuario registrado con éxito")

def realizar_prestamo():
    try:
        libro = next(libro for libro in biblioteca.libros if libro.id == entry_id_prestamo_libro.get())
        usuario = next(usuario for usuario in biblioteca.usuarios if usuario.id_usuario == entry_id_prestamo_usuario.get())
        prestamo = Prestamo(libro, usuario, entry_fecha_prestamo.get(), entry_fecha_devolucion.get())
        biblioteca.realizar_prestamo(prestamo)
        messagebox.showinfo("Préstamo", "Préstamo realizado con éxito")
    except StopIteration:
        messagebox.showerror("Error", "Libro o Usuario no encontrado")

def mostrar_libros():
    info_libros = biblioteca.mostrar_libros()
    messagebox.showinfo("Libros en Biblioteca", info_libros if info_libros else "No hay libros registrados")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca")
ventana.configure(bg="light goldenrod")

biblioteca = Biblioteca()

# Widgets para registrar libros
tk.Label(ventana, text="Registrar Libro", bg="light goldenrod").grid(row=0, column=0, columnspan=2)
tk.Label(ventana, text="Título:", bg="light goldenrod").grid(row=1, column=0)
entry_titulo = tk.Entry(ventana)
entry_titulo.grid(row=1, column=1)

tk.Label(ventana, text="ID:", bg="light goldenrod").grid(row=2, column=0)
entry_id_libro = tk.Entry(ventana)
entry_id_libro.grid(row=2, column=1)

tk.Label(ventana, text="Autor Nombre:", bg="light goldenrod").grid(row=3, column=0)
entry_autor_nombre = tk.Entry(ventana)
entry_autor_nombre.grid(row=3, column=1)

tk.Label(ventana, text="Autor Apellido:", bg="light goldenrod").grid(row=4, column=0)
entry_autor_apellido = tk.Entry(ventana)
entry_autor_apellido.grid(row=4, column=1)

tk.Label(ventana, text="Categoría:", bg="light goldenrod").grid(row=5, column=0)
entry_categoria = tk.Entry(ventana)
entry_categoria.grid(row=5, column=1)

btn_registrar_libro = tk.Button(ventana, text="Registrar Libro", command=registrar_libro)
btn_registrar_libro.grid(row=6, column=0, columnspan=2)

# Widgets para registrar usuarios
tk.Label(ventana, text="Registrar Usuario", bg="light goldenrod").grid(row=7, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=8, column=0)
entry_usuario_nombre = tk.Entry(ventana)
entry_usuario_nombre.grid(row=8, column=1)

tk.Label(ventana, text="Apellido:", bg="light goldenrod").grid(row=9, column=0)
entry_usuario_apellido = tk.Entry(ventana)
entry_usuario_apellido.grid(row=9, column=1)

tk.Label(ventana, text="ID Usuario:", bg="light goldenrod").grid(row=10, column=0)
entry_id_usuario = tk.Entry(ventana)
entry_id_usuario.grid(row=10, column=1)

btn_registrar_usuario = tk.Button(ventana, text="Registrar Usuario", command=registrar_usuario)
btn_registrar_usuario.grid(row=11, column=0, columnspan=2)

# Widgets para realizar préstamo
tk.Label(ventana, text="Realizar Préstamo", bg="light goldenrod").grid(row=12, column=0, columnspan=2)
tk.Label(ventana, text="ID Libro:", bg="light goldenrod").grid(row=13, column=0)
entry_id_prestamo_libro = tk.Entry(ventana)
entry_id_prestamo_libro.grid(row=13, column=1)

tk.Label(ventana, text="ID Usuario:", bg="light goldenrod").grid(row=14, column=0)
entry_id_prestamo_usuario = tk.Entry(ventana)
entry_id_prestamo_usuario.grid(row=14, column=1)

tk.Label(ventana, text="Fecha Préstamo:", bg="light goldenrod").grid(row=15, column=0)
entry_fecha_prestamo = tk.Entry(ventana)
entry_fecha_prestamo.grid(row=15, column=1)

tk.Label(ventana, text="Fecha Devolución:", bg="light goldenrod").grid(row=16, column=0)
entry_fecha_devolucion = tk.Entry(ventana)
entry_fecha_devolucion.grid(row=16, column=1)

btn_realizar_prestamo = tk.Button(ventana, text="Realizar Préstamo", command=realizar_prestamo)
btn_realizar_prestamo.grid(row=17, column=0, columnspan=2)

# Botón para mostrar libros
btn_mostrar_libros = tk.Button(ventana, text="Mostrar Libros", command=mostrar_libros)
btn_mostrar_libros.grid(row=18, column=0, columnspan=2)

ventana.mainloop()
