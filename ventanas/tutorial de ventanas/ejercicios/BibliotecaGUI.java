import java.awt.Color;
import java.awt.GridLayout;
import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

// Clases de Biblioteca
class Libro {
    String titulo;
    String id;
    Autor autor;
    Categoria categoria;

    public Libro(String titulo, String id, Autor autor, Categoria categoria) {
        this.titulo = titulo;
        this.id = id;
        this.autor = autor;
        this.categoria = categoria;
    }

    public String mostrarInfo() {
        return "Titulo: " + titulo + "\nId: " + id + "\nAutor: " + autor.nombre + " " + autor.apellido + "\nCategoria: " + categoria.nombre;
    }
}

class Autor {
    String nombre;
    String apellido;

    public Autor(String nombre, String apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

class Usuario {
    String nombre;
    String apellido;
    String idUsuario;

    public Usuario(String nombre, String apellido, String idUsuario) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.idUsuario = idUsuario;
    }

    public String mostrarInfo() {
        return "Usuario: " + nombre + " " + apellido + ", Id: " + idUsuario;
    }
}

class Prestamo {
    Libro libro;
    Usuario usuario;
    String fechaPrestamo;
    String fechaDevolucion;

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

class Categoria {
    String nombre;

    public Categoria(String nombre) {
        this.nombre = nombre;
    }
}

class Biblioteca {
    List<Libro> libros;
    List<Usuario> usuarios;
    List<Prestamo> prestamos;

    public Biblioteca() {
        libros = new ArrayList<>();
        usuarios = new ArrayList<>();
        prestamos = new ArrayList<>();
    }

    public void registrarLibro(Libro libro) {
        libros.add(libro);
    }

    public void registrarUsuario(Usuario usuario) {
        usuarios.add(usuario);
    }

    public void realizarPrestamo(Prestamo prestamo) {
        prestamos.add(prestamo);
    }

    public String mostrarLibros() {
        StringBuilder infoLibros = new StringBuilder();
        for (Libro libro : libros) {
            infoLibros.append(libro.mostrarInfo()).append("\n\n");
        }
        return infoLibros.toString().trim();
    }
}

// Ventana Principal
public class BibliotecaGUI extends JFrame {
    private final Biblioteca biblioteca;

    private final JTextField entryTitulo;
    private final JTextField entryIdLibro;
    private final JTextField entryAutorNombre;
    private final JTextField entryAutorApellido;
    private final JTextField entryCategoria;
    private final JTextField entryUsuarioNombre;
    private final JTextField entryUsuarioApellido;
    private final JTextField entryIdUsuario;
    private final JTextField entryIdPrestamoLibro;
    private final JTextField entryIdPrestamoUsuario;
    private final JTextField entryFechaPrestamo;
    private final JTextField entryFechaDevolucion;

    public BibliotecaGUI() {
        biblioteca = new Biblioteca();

        setTitle("Biblioteca");
        setSize(400, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(20, 2));
        panel.setBackground(new Color(255, 248, 220));

        // Widgets para registrar libros
        panel.add(new JLabel("Registrar Libro"));
        panel.add(new JLabel(""));
        panel.add(new JLabel("Título:"));
        entryTitulo = new JTextField();
        panel.add(entryTitulo);

        panel.add(new JLabel("ID:"));
        entryIdLibro = new JTextField();
        panel.add(entryIdLibro);

        panel.add(new JLabel("Autor Nombre:"));
        entryAutorNombre = new JTextField();
        panel.add(entryAutorNombre);

        panel.add(new JLabel("Autor Apellido:"));
        entryAutorApellido = new JTextField();
        panel.add(entryAutorApellido);

        panel.add(new JLabel("Categoría:"));
        entryCategoria = new JTextField();
        panel.add(entryCategoria);

        JButton btnRegistrarLibro = new JButton("Registrar Libro");
        btnRegistrarLibro.addActionListener(e -> registrarLibro());
        panel.add(btnRegistrarLibro);

        panel.add(new JLabel("Registrar Usuario"));
        panel.add(new JLabel(""));
        panel.add(new JLabel("Nombre:"));
        entryUsuarioNombre = new JTextField();
        panel.add(entryUsuarioNombre);

        panel.add(new JLabel("Apellido:"));
        entryUsuarioApellido = new JTextField();
        panel.add(entryUsuarioApellido);

        panel.add(new JLabel("ID Usuario:"));
        entryIdUsuario = new JTextField();
        panel.add(entryIdUsuario);

        JButton btnRegistrarUsuario = new JButton("Registrar Usuario");
        btnRegistrarUsuario.addActionListener(e -> registrarUsuario());
        panel.add(btnRegistrarUsuario);

        panel.add(new JLabel("Realizar Préstamo"));
        panel.add(new JLabel(""));
        panel.add(new JLabel("ID Libro:"));
        entryIdPrestamoLibro = new JTextField();
        panel.add(entryIdPrestamoLibro);

        panel.add(new JLabel("ID Usuario:"));
        entryIdPrestamoUsuario = new JTextField();
        panel.add(entryIdPrestamoUsuario);

        panel.add(new JLabel("Fecha Préstamo:"));
        entryFechaPrestamo = new JTextField();
        panel.add(entryFechaPrestamo);

        panel.add(new JLabel("Fecha Devolución:"));
        entryFechaDevolucion = new JTextField();
        panel.add(entryFechaDevolucion);

        JButton btnRealizarPrestamo = new JButton("Realizar Préstamo");
        btnRealizarPrestamo.addActionListener(e -> realizarPrestamo());
        panel.add(btnRealizarPrestamo);

        JButton btnMostrarLibros = new JButton("Mostrar Libros");
        btnMostrarLibros.addActionListener(e -> mostrarLibros());
        panel.add(btnMostrarLibros);

        add(panel);
    }

    private void registrarLibro() {
        Autor autor = new Autor(entryAutorNombre.getText(), entryAutorApellido.getText());
        Categoria categoria = new Categoria(entryCategoria.getText());
        Libro libro = new Libro(entryTitulo.getText(), entryIdLibro.getText(), autor, categoria);
        biblioteca.registrarLibro(libro);
        JOptionPane.showMessageDialog(this, "Libro registrado con éxito");
    }

    private void registrarUsuario() {
        Usuario usuario = new Usuario(entryUsuarioNombre.getText(), entryUsuarioApellido.getText(), entryIdUsuario.getText());
        biblioteca.registrarUsuario(usuario);
        JOptionPane.showMessageDialog(this, "Usuario registrado con éxito");
    }

    private void realizarPrestamo() {
        try {
            Libro libro = biblioteca.libros.stream()
                    .filter(l -> l.id.equals(entryIdPrestamoLibro.getText()))
                    .findFirst()
                    .orElseThrow(NoSuchElementException::new);
            Usuario usuario = biblioteca.usuarios.stream()
                    .filter(u -> u.idUsuario.equals(entryIdPrestamoUsuario.getText()))
                    .findFirst()
                    .orElseThrow(NoSuchElementException::new);
            Prestamo prestamo = new Prestamo(libro, usuario, entryFechaPrestamo.getText(), entryFechaDevolucion.getText());
            biblioteca.realizarPrestamo(prestamo);
            JOptionPane.showMessageDialog(this, "Préstamo realizado con éxito");
        } catch (NoSuchElementException e) {
            JOptionPane.showMessageDialog(this, "Libro o Usuario no encontrado", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void mostrarLibros() {
        String infoLibros = biblioteca.mostrarLibros();
        JOptionPane.showMessageDialog(this, infoLibros.isEmpty() ? "No hay libros registrados" : infoLibros);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new BibliotecaGUI().setVisible(true));
    }
}


