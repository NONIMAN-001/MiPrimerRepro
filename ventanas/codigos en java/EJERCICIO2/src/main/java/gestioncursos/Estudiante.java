package gestioncursos;

import java.util.ArrayList;
import java.util.List;

public class Estudiante {
    private String nombre;
    private String apellido;
    private String idEstudiante;
    private List<Curso> cursos;

    public Estudiante(String nombre, String apellido, String idEstudiante) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.idEstudiante = idEstudiante;
        this.cursos = new ArrayList<>();
    }

    public String mostrarInfo() {
        StringBuilder info = new StringBuilder("Nombre: " + nombre + " " + apellido + ", Id del estudiante: " + idEstudiante + "\n");
        for (Curso c : cursos) {
            info.append("Curso: ").append(c.getNombre()).append("\n");
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

    public String getIdEstudiante() {
        return idEstudiante;
    }

    public List<Curso> getCursos() {
        return cursos;
    }
}

