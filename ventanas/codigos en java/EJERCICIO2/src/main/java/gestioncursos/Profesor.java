package gestioncursos;

import java.util.ArrayList;
import java.util.List;

public class Profesor {
    private String nombre;
    private String apellido;
    private List<Asignatura> asignaturas;

    public Profesor(String nombre, String apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.asignaturas = new ArrayList<>();
    }

    public String mostrarInfo() {
        StringBuilder info = new StringBuilder("Nombre del maestro: " + nombre + " " + apellido + "\n");
        for (Asignatura a : asignaturas) {
            info.append("Asignatura: ").append(a.getNombre()).append("\n");
        }
        return info.toString();
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public List<Asignatura> getAsignaturas() {
        return asignaturas;
    }
}

