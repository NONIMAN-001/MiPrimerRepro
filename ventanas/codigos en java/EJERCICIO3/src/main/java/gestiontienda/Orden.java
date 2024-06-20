package gestiontienda;

import java.util.ArrayList;
import java.util.List;

public class Orden {
    private Cliente cliente;
    private List<ItemOrden> items;
    private double total;

    public Orden(Cliente cliente) {
        this.cliente = cliente;
        this.items = new ArrayList<>();
        this.total = 0.0;
    }

    public void agregarItem(ItemOrden item) {
        items.add(item);
        calcularTotal();
    }

    private void calcularTotal() {
        total = items.stream().mapToDouble(ItemOrden::calcularSubtotal).sum();
    }

    public String mostrarInfo() {
        StringBuilder itemsInfo = new StringBuilder();
        for (ItemOrden item : items) {
            itemsInfo.append(item.mostrarInfo()).append("\n");
        }
        return "Orden de " + cliente.getNombre() + " " + cliente.getApellido() + "\n" + itemsInfo + "Total: " + total;
    }

    // Getters
    public Cliente getCliente() {
        return cliente;
    }
}
