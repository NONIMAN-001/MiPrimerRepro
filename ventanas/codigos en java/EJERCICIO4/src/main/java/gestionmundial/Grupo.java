package gestionmundial;

import java.util.ArrayList;
import java.util.List;

public class Grupo {
    private String nombre;
    private List<Equipo> equipos;

    public Grupo(String nombre) {
        this.nombre = nombre;
        this.equipos = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public List<Equipo> getEquipos() {
        return equipos;
    }

    public void agregarEquipo(Equipo equipo) {
        equipos.add(equipo);
    }

    public String mostrarInfo() {
        StringBuilder equiposInfo = new StringBuilder();
        for (Equipo equipo : equipos) {
            equiposInfo.append(equipo.mostrarInfo()).append("\n");
        }
        return "Grupo: " + nombre + "\nEquipos:\n" + equiposInfo;
    }
}

