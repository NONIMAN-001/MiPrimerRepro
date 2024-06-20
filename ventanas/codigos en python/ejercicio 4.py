import tkinter as tk
from tkinter import ttk, messagebox

class Jugador:
    def __init__(self, nombre, edad, posicion):
        self._nombre = nombre
        self._edad = edad
        self._posicion = posicion

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad
    def set_edad(self, edad):
        self._edad = edad

    def get_posicion(self):
        return self._posicion
    def set_posicion(self, posicion):
        self._posicion = posicion

    def mostrar_info(self):
        return f"Jugador: {self._nombre}, Edad: {self._edad}, Posición: {self._posicion}"

class Equipo:
    def __init__(self, nombre, entrenador):
        self._nombre = nombre
        self._entrenador = entrenador
        self._jugadores = []

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_entrenador(self):
        return self._entrenador
    def set_entrenador(self, entrenador):
        self._entrenador = entrenador

    def get_jugadores(self):
        return self._jugadores
    def agregar_jugador(self, jugador):
        self._jugadores.append(jugador)

    def mostrar_info(self):
        jugadores_info = "\n".join(jugador.mostrar_info() for jugador in self._jugadores)
        return f"Equipo: {self._nombre}, Entrenador: {self._entrenador}\nJugadores:\n{jugadores_info}"

class Partido:
    def __init__(self, equipo_local, equipo_visitante, estadio):
        self._equipo_local = equipo_local
        self._equipo_visitante = equipo_visitante
        self._estadio = estadio
        self._resultado = None

    def get_equipo_local(self):
        return self._equipo_local
    def set_equipo_local(self, equipo_local):
        self._equipo_local = equipo_local

    def get_equipo_visitante(self):
        return self._equipo_visitante
    def set_equipo_visitante(self, equipo_visitante):
        self._equipo_visitante = equipo_visitante

    def get_estadio(self):
        return self._estadio
    def set_estadio(self, estadio):
        self._estadio = estadio

    def get_resultado(self):
        return self._resultado
    def set_resultado(self, resultado):
        self._resultado = resultado

    def jugar_partido(self, resultado):
        self._resultado = resultado

    def mostrar_resultado(self):
        return f"Partido: {self._equipo_local.get_nombre()} vs {self._equipo_visitante.get_nombre()}, Resultado: {self._resultado}"

class Grupo:
    def __init__(self, nombre):
        self._nombre = nombre
        self._equipos = []

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_equipos(self):
        return self._equipos
    def agregar_equipo(self, equipo):
        self._equipos.append(equipo)

    def mostrar_info(self):
        equipos_info = "\n".join(equipo.mostrar_info() for equipo in self._equipos)
        return f"Grupo: {self._nombre}\nEquipos:\n{equipos_info}"

class Estadio:
    def __init__(self, nombre, ciudad, capacidad):
        self._nombre = nombre
        self._ciudad = ciudad
        self._capacidad = capacidad

    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_ciudad(self):
        return self._ciudad
    def set_ciudad(self, ciudad):
        self._ciudad = ciudad

    def get_capacidad(self):
        return self._capacidad
    def set_capacidad(self, capacidad):
        self._capacidad = capacidad

    def mostrar_info(self):
        return f"Estadio: {self._nombre}, Ciudad: {self._ciudad}, Capacidad: {self._capacidad}"

class Mundial:
    def __init__(self):
        self._grupos = []
        self._estadios = []

    def get_grupos(self):
        return self._grupos
    def get_estadios(self):
        return self._estadios

    def registrar_grupo(self, grupo):
        self._grupos.append(grupo)
    def registrar_estadio(self, estadio):
        self._estadios.append(estadio)

    def generar_fixture(self):
        fixture = []
        for grupo in self._grupos:
            equipos = grupo.get_equipos()
            for i in range(len(equipos)):
                for j in range(i + 1, len(equipos)):
                    partido = Partido(equipos[i], equipos[j], self._estadios[0])  # simplificado para usar el primer estadio
                    fixture.append(partido)
        return fixture

# Funciones de la GUI
def registrar_jugador():
    nombre = entry_jugador_nombre.get()
    edad = entry_jugador_edad.get()
    posicion = entry_jugador_posicion.get()
    jugador = Jugador(nombre, edad, posicion)
    jugadores.append(jugador)
    messagebox.showinfo("Registro", "Jugador registrado con éxito")

def registrar_equipo():
    nombre = entry_equipo_nombre.get()
    entrenador = entry_equipo_entrenador.get()
    equipo = Equipo(nombre, entrenador)
    equipos.append(equipo)
    messagebox.showinfo("Registro", "Equipo registrado con éxito")

def agregar_jugador_a_equipo():
    equipo_nombre = combobox_equipo.get()
    jugador_nombre = combobox_jugador.get()
    equipo = next((e for e in equipos if e.get_nombre() == equipo_nombre), None)
    jugador = next((j for j in jugadores if j.get_nombre() == jugador_nombre), None)
    if equipo and jugador:
        equipo.agregar_jugador(jugador)
        messagebox.showinfo("Registro", "Jugador agregado al equipo con éxito")
    else:
        messagebox.showerror("Error", "Equipo o jugador no encontrado")

def registrar_estadio():
    nombre = entry_estadio_nombre.get()
    ciudad = entry_estadio_ciudad.get()
    capacidad = entry_estadio_capacidad.get()
    estadio = Estadio(nombre, ciudad, capacidad)
    estadios.append(estadio)
    messagebox.showinfo("Registro", "Estadio registrado con éxito")

def registrar_grupo():
    nombre = entry_grupo_nombre.get()
    grupo = Grupo(nombre)
    grupos.append(grupo)
    messagebox.showinfo("Registro", "Grupo registrado con éxito")

def agregar_equipo_a_grupo():
    grupo_nombre = combobox_grupo.get()
    equipo_nombre = combobox_equipo_grupo.get()
    grupo = next((g for g in grupos if g.get_nombre() == grupo_nombre), None)
    equipo = next((e for e in equipos if e.get_nombre() == equipo_nombre), None)
    if grupo and equipo:
        grupo.agregar_equipo(equipo)
        messagebox.showinfo("Registro", "Equipo agregado al grupo con éxito")
    else:
        messagebox.showerror("Error", "Grupo o equipo no encontrado")

def generar_fixture():
    mundial = Mundial()
    for grupo in grupos:
        mundial.registrar_grupo(grupo)
    for estadio in estadios:
        mundial.registrar_estadio(estadio)
    fixture = mundial.generar_fixture()
    fixture_info = "\n\n".join(partido.mostrar_resultado() for partido in fixture)
    messagebox.showinfo("Fixture Generado", fixture_info if fixture_info else "No hay partidos para mostrar")

def mostrar_info_equipos():
    info_equipos = "\n\n".join(equipo.mostrar_info() for equipo in equipos)
    messagebox.showinfo("Equipos en el sistema", info_equipos if info_equipos else "No hay equipos registrados")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Mundial")
ventana.configure(bg="light goldenrod")

jugadores = []
equipos = []
estadios = []
grupos = []

# Widgets para registrar jugadores
tk.Label(ventana, text="Registrar Jugador", bg="light goldenrod").grid(row=0, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=1, column=0)
entry_jugador_nombre = tk.Entry(ventana)
entry_jugador_nombre.grid(row=1, column=1)

tk.Label(ventana, text="Edad:", bg="light goldenrod").grid(row=2, column=0)
entry_jugador_edad = tk.Entry(ventana)
entry_jugador_edad.grid(row=2, column=1)

tk.Label(ventana, text="Posición:", bg="light goldenrod").grid(row=3, column=0)
entry_jugador_posicion = tk.Entry(ventana)
entry_jugador_posicion.grid(row=3, column=1)

btn_registrar_jugador = tk.Button(ventana, text="Registrar Jugador", command=registrar_jugador)
btn_registrar_jugador.grid(row=4, column=0, columnspan=2)

# Widgets para registrar equipos
tk.Label(ventana, text="Registrar Equipo", bg="light goldenrod").grid(row=5, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=6, column=0)
entry_equipo_nombre = tk.Entry(ventana)
entry_equipo_nombre.grid(row=6, column=1)

tk.Label(ventana, text="Entrenador:", bg="light goldenrod").grid(row=7, column=0)
entry_equipo_entrenador = tk.Entry(ventana)
entry_equipo_entrenador.grid(row=7, column=1)

btn_registrar_equipo = tk.Button(ventana, text="Registrar Equipo", command=registrar_equipo)
btn_registrar_equipo.grid(row=8, column=0, columnspan=2)

# Widgets para agregar jugadores a equipos
tk.Label(ventana, text="Agregar Jugador a Equipo", bg="light goldenrod").grid(row=9, column=0, columnspan=2)
tk.Label(ventana, text="Equipo:", bg="light goldenrod").grid(row=10, column=0)
combobox_equipo = ttk.Combobox(ventana, values=[e.get_nombre() for e in equipos])
combobox_equipo.grid(row=10, column=1)

tk.Label(ventana, text="Jugador:", bg="light goldenrod").grid(row=11, column=0)
combobox_jugador = ttk.Combobox(ventana, values=[j.get_nombre() for j in jugadores])
combobox_jugador.grid(row=11, column=1)

btn_agregar_jugador = tk.Button(ventana, text="Agregar Jugador", command=agregar_jugador_a_equipo)
btn_agregar_jugador.grid(row=12, column=0, columnspan=2)

# Widgets para registrar estadios
tk.Label(ventana, text="Registrar Estadio", bg="light goldenrod").grid(row=13, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=14, column=0)
entry_estadio_nombre = tk.Entry(ventana)
entry_estadio_nombre.grid(row=14, column=1)

tk.Label(ventana, text="Ciudad:", bg="light goldenrod").grid(row=15, column=0)
entry_estadio_ciudad = tk.Entry(ventana)
entry_estadio_ciudad.grid(row=15, column=1)

tk.Label(ventana, text="Capacidad:", bg="light goldenrod").grid(row=16, column=0)
entry_estadio_capacidad = tk.Entry(ventana)
entry_estadio_capacidad.grid(row=16, column=1)

btn_registrar_estadio = tk.Button(ventana, text="Registrar Estadio", command=registrar_estadio)
btn_registrar_estadio.grid(row=17, column=0, columnspan=2)

# Widgets para registrar grupos
tk.Label(ventana, text="Registrar Grupo", bg="light goldenrod").grid(row=18, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=19, column=0)
entry_grupo_nombre = tk.Entry(ventana)
entry_grupo_nombre.grid(row=19, column=1)

btn_registrar_grupo = tk.Button(ventana, text="Registrar Grupo", command=registrar_grupo)
btn_registrar_grupo.grid(row=20, column=0, columnspan=2)

# Widgets para agregar equipos a grupos
tk.Label(ventana, text="Agregar Equipo a Grupo", bg="light goldenrod").grid(row=21, column=0, columnspan=2)
tk.Label(ventana, text="Grupo:", bg="light goldenrod").grid(row=22, column=0)
combobox_grupo = ttk.Combobox(ventana, values=[g.get_nombre() for g in grupos])
combobox_grupo.grid(row=22, column=1)

tk.Label(ventana, text="Equipo:", bg="light goldenrod").grid(row=23, column=0)
combobox_equipo_grupo = ttk.Combobox(ventana, values=[e.get_nombre() for e in equipos])
combobox_equipo_grupo.grid(row=23, column=1)

btn_agregar_equipo = tk.Button(ventana, text="Agregar Equipo", command=agregar_equipo_a_grupo)
btn_agregar_equipo.grid(row=24, column=0, columnspan=2)

# Widgets para generar fixture
btn_generar_fixture = tk.Button(ventana, text="Generar Fixture", command=generar_fixture)
btn_generar_fixture.grid(row=25, column=0, columnspan=2)

# Botón para mostrar información de los equipos
btn_mostrar_info_equipos = tk.Button(ventana, text="Mostrar Información de Equipos", command=mostrar_info_equipos)
btn_mostrar_info_equipos.grid(row=26, column=0, columnspan=2)

ventana.mainloop()
