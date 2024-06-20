package biblioteca;

public class Usuario {
    private String nombre;
    private String apellido;
    private String idUsuario;

    public Usuario(String nombre, String apellido, String idUsuario) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.idUsuario = idUsuario;
    }

    public String mostrarInfo() {
        return "Usuario: " + nombre + " " + apellido + ", Id: " + idUsuario;
    }

    public String getIdUsuario() {
        return idUsuario;
    }
}


