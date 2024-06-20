package gestiontienda;

import java.util.ArrayList;
import java.util.List;

public class Tienda {
    private List<Producto> productos;
    private List<Cliente> clientes;
    private List<Orden> ordenes;
    private List<Categoria> categorias;

    public Tienda() {
        productos = new ArrayList<>();
        clientes = new ArrayList<>();
        ordenes = new ArrayList<>();
        categorias = new ArrayList<>();
    }

    public void registrarProducto(Producto producto) {
        productos.add(producto);
    }

    public void registrarCliente(Cliente cliente) {
        clientes.add(cliente);
    }

    public Orden crearOrden(Cliente cliente) {
        Orden orden = new Orden(cliente);
        ordenes.add(orden);
        return orden;
    }

    public String mostrarProductos() {
        StringBuilder sb = new StringBuilder();
        for (Producto producto : productos) {
            sb.append(producto.mostrarInfo()).append("\n");
        }
        return sb.toString();
    }

    // Getters
    public List<Producto> getProductos() {
        return productos;
    }

    public List<Cliente> getClientes() {
        return clientes;
    }

    public List<Orden> getOrdenes() {
        return ordenes;
    }

    public List<Categoria> getCategorias() {
        return categorias;
    }
}

