package gestioncursos;

public class Evaluacion {
    private Curso curso;
    private Estudiante estudiante;
    private String nota;

    public Evaluacion(Curso curso, Estudiante estudiante, String nota) {
        this.curso = curso;
        this.estudiante = estudiante;
        this.nota = nota;
    }

    public String mostrarInfo() {
        return "Evaluación del curso: " + curso.getNombre() + "\n" +
               "Estudiante: " + estudiante.getNombre() + " " + estudiante.getApellido() + ", " + estudiante.getIdEstudiante() + "\n" +
               "Nota: " + nota;
    }
}

