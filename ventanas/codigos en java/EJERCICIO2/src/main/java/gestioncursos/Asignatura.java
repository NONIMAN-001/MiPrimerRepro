package gestioncursos;

public class Asignatura {
    private String nombre;
    private Profesor profesor;

    public Asignatura(String nombre, Profesor profesor) {
        this.nombre = nombre;
        this.profesor = profesor;
        profesor.getAsignaturas().add(this);
    }

    public String mostrarInfo() {
        return "Nombre: " + nombre + ", Profesor: " + profesor.getNombre() + " " + profesor.getApellido();
    }

    // Getters
    public String getNombre() {
        return nombre;
    }
}

