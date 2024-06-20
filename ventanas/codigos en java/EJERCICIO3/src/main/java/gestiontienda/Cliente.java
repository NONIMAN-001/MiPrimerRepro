package gestiontienda;

public class Cliente {
    private String nombre;
    private String apellido;
    private String idCliente;

    public Cliente(String nombre, String apellido, String idCliente) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.idCliente = idCliente;
    }

    public String mostrarInfo() {
        return "Nombre: " + nombre + " " + apellido + ", ID: " + idCliente;
    }

    // Getters
    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getIdCliente() {
        return idCliente;
    }
}

