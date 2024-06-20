package gestionmundial;

import java.util.ArrayList;
import java.util.List;

public class Equipo {
    private String nombre;
    private String entrenador;
    private List<Jugador> jugadores;

    public Equipo(String nombre, String entrenador) {
        this.nombre = nombre;
        this.entrenador = entrenador;
        this.jugadores = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getEntrenador() {
        return entrenador;
    }

    public void setEntrenador(String entrenador) {
        this.entrenador = entrenador;
    }

    public List<Jugador> getJugadores() {
        return jugadores;
    }

    public void agregarJugador(Jugador jugador) {
        jugadores.add(jugador);
    }

    public String mostrarInfo() {
        StringBuilder jugadoresInfo = new StringBuilder();
        for (Jugador jugador : jugadores) {
            jugadoresInfo.append(jugador.mostrarInfo()).append("\n");
        }
        return "Equipo: " + nombre + ", Entrenador: " + entrenador + "\nJugadores:\n" + jugadoresInfo;
    }
}

