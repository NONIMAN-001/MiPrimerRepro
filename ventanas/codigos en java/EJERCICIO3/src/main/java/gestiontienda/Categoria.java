package gestiontienda;

public class Categoria {
    private String nombre;

    public Categoria(String nombre) {
        this.nombre = nombre;
    }

    public String mostrarInfo() {
        return "Categoria: " + nombre;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }
}

