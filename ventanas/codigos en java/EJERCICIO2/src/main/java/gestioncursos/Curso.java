package gestioncursos;

import java.util.ArrayList;
import java.util.List;

public class Curso {
    private String nombre;
    private Profesor profesor;
    private List<Estudiante> estudiantes;
    private Horario horario;

    public Curso(String nombre, Profesor profesor, Horario horario) {
        this.nombre = nombre;
        this.profesor = profesor;
        this.estudiantes = new ArrayList<>();
        this.horario = horario;
    }

    public String mostrarInfo() {
        StringBuilder info = new StringBuilder("Nombre del curso: " + nombre + "\n" +
                profesor.mostrarInfo() + "\n" +
                horario.mostrarInfo() + "\n" +
                "Estudiantes inscritos: ");
        for (Estudiante e : estudiantes) {
            info.append(e.getNombre()).append(" ").append(e.getApellido()).append(", ");
        }
        return info.toString();
    }

    public void agregarEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
        estudiante.getCursos().add(this);
    }

    // Getters
    public String getNombre() {
        return nombre;
    }
}

