package gestiontienda;

public class Producto {
    private String nombre;
    private double precio;
    private Categoria categoria;

    public Producto(String nombre, double precio, Categoria categoria) {
        this.nombre = nombre;
        this.precio = precio;
        this.categoria = categoria;
    }

    public String mostrarInfo() {
        return "Nombre del producto: " + nombre + ", Precio: " + precio + ", Categoria: " + categoria.getNombre();
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public Categoria getCategoria() {
        return categoria;
    }
}

