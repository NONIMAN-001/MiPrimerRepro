package gestiontienda;

public class ItemOrden {
    private Producto producto;
    private int cantidad;

    public ItemOrden(Producto producto, int cantidad) {
        this.producto = producto;
        this.cantidad = cantidad;
    }

    public double calcularSubtotal() {
        return producto.getPrecio() * cantidad;
    }

    public String mostrarInfo() {
        return "Item: " + producto.getNombre() + ", Cantidad: " + cantidad + ", Subtotal: " + calcularSubtotal();
    }
}

