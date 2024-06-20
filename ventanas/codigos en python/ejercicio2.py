import tkinter as tk
from tkinter import ttk, messagebox

# Clases del sistema de gestión de cursos
class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario

    def mostrar_info(self):
        return (f"Nombre del curso: {self.nombre}\n"
                f"{self.profesor.mostrar_info()}\n"
                f"{self.horario.mostrar_info()}\n"
                f"Estudiantes inscritos: {[f'{e.nombre} {e.apellido}' for e in self.estudiantes]}")

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)

class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        return f"Nombre del maestro: {self.nombre} {self.apellido}\n" + "\n".join(f"Asignatura: {a.nombre}" for a in self.asignaturas)

class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        return (f"Nombre: {self.nombre} {self.apellido}, Id del estudiante: {self.id_estudiante}\n" +
                "\n".join(f"Curso: {c.nombre}" for c in self.cursos))

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        profesor.asignaturas.append(self)

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}"

class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota

    def mostrar_info(self):
        return (f"Evaluación del curso: {self.curso.nombre}\n"
                f"Estudiante: {self.estudiante.nombre} {self.estudiante.apellido}, {self.estudiante.id_estudiante}\n"
                f"Nota: {self.nota}")

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia}, De {self.hora_inicio} a {self.hora_fin}"

# Funciones de la GUI
def registrar_profesor():
    profesor = Profesor(entry_profesor_nombre.get(), entry_profesor_apellido.get())
    profesores.append(profesor)
    messagebox.showinfo("Registro", "Profesor registrado con éxito")

def registrar_asignatura():
    profesor = next((p for p in profesores if f"{p.nombre} {p.apellido}" == combobox_profesor.get()), None)
    if profesor:
        asignatura = Asignatura(entry_asignatura_nombre.get(), profesor)
        asignaturas.append(asignatura)
        messagebox.showinfo("Registro", "Asignatura registrada con éxito")
    else:
        messagebox.showerror("Error", "Profesor no encontrado")

def registrar_curso():
    profesor = next((p for p in profesores if f"{p.nombre} {p.apellido}" == combobox_profesor_curso.get()), None)
    if profesor:
        horario = Horario(entry_horario_dia.get(), entry_horario_inicio.get(), entry_horario_fin.get())
        curso = Curso(entry_curso_nombre.get(), profesor, horario)
        cursos.append(curso)
        messagebox.showinfo("Registro", "Curso registrado con éxito")
    else:
        messagebox.showerror("Error", "Profesor no encontrado")

def registrar_estudiante():
    estudiante = Estudiante(entry_estudiante_nombre.get(), entry_estudiante_apellido.get(), entry_id_estudiante.get())
    estudiantes.append(estudiante)
    messagebox.showinfo("Registro", "Estudiante registrado con éxito")

def agregar_estudiante_a_curso():
    curso = next((c for c in cursos if c.nombre == combobox_curso.get()), None)
    estudiante = next((e for e in estudiantes if e.id_estudiante == entry_id_estudiante_curso.get()), None)
    if curso and estudiante:
        curso.agregar_estudiante(estudiante)
        messagebox.showinfo("Registro", "Estudiante agregado al curso con éxito")
    else:
        messagebox.showerror("Error", "Curso o estudiante no encontrado")

def realizar_evaluacion():
    curso = next((c for c in cursos if c.nombre == combobox_curso_eval.get()), None)
    estudiante = next((e for e in estudiantes if e.id_estudiante == entry_id_estudiante_eval.get()), None)
    if curso and estudiante:
        evaluacion = Evaluacion(curso, estudiante, entry_nota.get())
        evaluaciones.append(evaluacion)
        messagebox.showinfo("Registro", "Evaluación registrada con éxito")
    else:
        messagebox.showerror("Error", "Curso o estudiante no encontrado")

def mostrar_info_cursos():
    info_cursos = "\n\n".join(curso.mostrar_info() for curso in cursos)
    messagebox.showinfo("Cursos en el sistema", info_cursos if info_cursos else "No hay cursos registrados")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Cursos")
ventana.configure(bg="light goldenrod")

profesores = []
asignaturas = []
cursos = []
estudiantes = []
evaluaciones = []

# Widgets para registrar profesores
tk.Label(ventana, text="Registrar Profesor", bg="light goldenrod").grid(row=0, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=1, column=0)
entry_profesor_nombre = tk.Entry(ventana)
entry_profesor_nombre.grid(row=1, column=1)

tk.Label(ventana, text="Apellido:", bg="light goldenrod").grid(row=2, column=0)
entry_profesor_apellido = tk.Entry(ventana)
entry_profesor_apellido.grid(row=2, column=1)

btn_registrar_profesor = tk.Button(ventana, text="Registrar Profesor", command=registrar_profesor)
btn_registrar_profesor.grid(row=3, column=0, columnspan=2)

# Widgets para registrar asignaturas
tk.Label(ventana, text="Registrar Asignatura", bg="light goldenrod").grid(row=4, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=5, column=0)
entry_asignatura_nombre = tk.Entry(ventana)
entry_asignatura_nombre.grid(row=5, column=1)

tk.Label(ventana, text="Profesor:", bg="light goldenrod").grid(row=6, column=0)
combobox_profesor = ttk.Combobox(ventana, values=[f"{p.nombre} {p.apellido}" for p in profesores])
combobox_profesor.grid(row=6, column=1)

btn_registrar_asignatura = tk.Button(ventana, text="Registrar Asignatura", command=registrar_asignatura)
btn_registrar_asignatura.grid(row=7, column=0, columnspan=2)

# Widgets para registrar cursos
tk.Label(ventana, text="Registrar Curso", bg="light goldenrod").grid(row=8, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=9, column=0)
entry_curso_nombre = tk.Entry(ventana)
entry_curso_nombre.grid(row=9, column=1)

tk.Label(ventana, text="Profesor:", bg="light goldenrod").grid(row=10, column=0)
combobox_profesor_curso = ttk.Combobox(ventana, values=[f"{p.nombre} {p.apellido}" for p in profesores])
combobox_profesor_curso.grid(row=10, column=1)

tk.Label(ventana, text="Día:", bg="light goldenrod").grid(row=11, column=0)
entry_horario_dia = tk.Entry(ventana)
entry_horario_dia.grid(row=11, column=1)

tk.Label(ventana, text="Hora inicio:", bg="light goldenrod").grid(row=12, column=0)
entry_horario_inicio = tk.Entry(ventana)
entry_horario_inicio.grid(row=12, column=1)

tk.Label(ventana, text="Hora fin:", bg="light goldenrod").grid(row=13, column=0)
entry_horario_fin = tk.Entry(ventana)
entry_horario_fin.grid(row=13, column=1)

btn_registrar_curso = tk.Button(ventana, text="Registrar Curso", command=registrar_curso)
btn_registrar_curso.grid(row=14, column=0, columnspan=2)

# Widgets para registrar estudiantes
tk.Label(ventana, text="Registrar Estudiante", bg="light goldenrod").grid(row=15, column=0, columnspan=2)
tk.Label(ventana, text="Nombre:", bg="light goldenrod").grid(row=16, column=0)
entry_estudiante_nombre = tk.Entry(ventana)
entry_estudiante_nombre.grid(row=16, column=1)

tk.Label(ventana, text="Apellido:", bg="light goldenrod").grid(row=17, column=0)
entry_estudiante_apellido = tk.Entry(ventana)
entry_estudiante_apellido.grid(row=17, column=1)

tk.Label(ventana, text="ID Estudiante:", bg="light goldenrod").grid(row=18, column=0)
entry_id_estudiante = tk.Entry(ventana)
entry_id_estudiante.grid(row=18, column=1)

btn_registrar_estudiante = tk.Button(ventana, text="Registrar Estudiante", command=registrar_estudiante)
btn_registrar_estudiante.grid(row=19, column=0, columnspan=2)

# Widgets para agregar estudiantes a cursos
tk.Label(ventana, text="Agregar Estudiante a Curso", bg="light goldenrod").grid(row=20, column=0, columnspan=2)
tk.Label(ventana, text="Curso:", bg="light goldenrod").grid(row=21, column=0)
combobox_curso = ttk.Combobox(ventana, values=[c.nombre for c in cursos])
combobox_curso.grid(row=21, column=1)

tk.Label(ventana, text="ID Estudiante:", bg="light goldenrod").grid(row=22, column=0)
entry_id_estudiante_curso = tk.Entry(ventana)
entry_id_estudiante_curso.grid(row=22, column=1)

btn_agregar_estudiante_curso = tk.Button(ventana, text="Agregar Estudiante", command=agregar_estudiante_a_curso)
btn_agregar_estudiante_curso.grid(row=23, column=0, columnspan=2)

# Widgets para realizar evaluaciones
tk.Label(ventana, text="Realizar Evaluación", bg="light goldenrod").grid(row=24, column=0, columnspan=2)
tk.Label(ventana, text="Curso:", bg="light goldenrod").grid(row=25, column=0)
combobox_curso_eval = ttk.Combobox(ventana, values=[c.nombre for c in cursos])
combobox_curso_eval.grid(row=25, column=1)

tk.Label(ventana, text="ID Estudiante:", bg="light goldenrod").grid(row=26, column=0)
entry_id_estudiante_eval = tk.Entry(ventana)
entry_id_estudiante_eval.grid(row=26, column=1)

tk.Label(ventana, text="Nota:", bg="light goldenrod").grid(row=27, column=0)
entry_nota = tk.Entry(ventana)
entry_nota.grid(row=27, column=1)

btn_realizar_evaluacion = tk.Button(ventana, text="Realizar Evaluación", command=realizar_evaluacion)
btn_realizar_evaluacion.grid(row=28, column=0, columnspan=2)

# Botón para mostrar información de los cursos
btn_mostrar_info_cursos = tk.Button(ventana, text="Mostrar Información de Cursos", command=mostrar_info_cursos)
btn_mostrar_info_cursos.grid(row=29, column=0, columnspan=2)

ventana.mainloop()
