package biblioteca;

public class Prestamo {
    private Libro libro;
    private Usuario usuario;
    private String fechaPrestamo;
    private String fechaDevolucion;

    public Prestamo(Libro libro, Usuario usuario, String fechaPrestamo, String fechaDevolucion) {
        this.libro = libro;
        this.usuario = usuario;
        this.fechaPrestamo = fechaPrestamo;
        this.fechaDevolucion = fechaDevolucion;
    }

    public String mostrarInfo() {
        return "Prestamo\n" + libro.mostrarInfo() + "\n" + usuario.mostrarInfo() + "\nFecha prestamo: " + fechaPrestamo + "\nFecha devolucion: " + fechaDevolucion;
    }
}


