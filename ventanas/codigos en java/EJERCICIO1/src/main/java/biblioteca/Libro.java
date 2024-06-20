package biblioteca;

public class Libro {
    private String titulo;
    private String id;
    private Autor autor;
    private Categoria categoria;

    public Libro(String titulo, String id, Autor autor, Categoria categoria) {
        this.titulo = titulo;
        this.id = id;
        this.autor = autor;
        this.categoria = categoria;
    }

    public String mostrarInfo() {
        return "Titulo: " + titulo + "\nId: " + id + "\nAutor: " + autor.getNombre() + " " + autor.getApellido() + "\nCategoria: " + categoria.getNombre();
    }

    public String getId() {
        return id;
    }
}


