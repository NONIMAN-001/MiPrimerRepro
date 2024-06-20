package gestionmundial;

import java.util.ArrayList;
import java.util.List;

public class Mundial {
    private List<Grupo> grupos;
    private List<Estadio> estadios;

    public Mundial() {
        this.grupos = new ArrayList<>();
        this.estadios = new ArrayList<>();
    }

    public List<Grupo> getGrupos() {
        return grupos;
    }

    public List<Estadio> getEstadios() {
        return estadios;
    }

    public void registrarGrupo(Grupo grupo) {
        grupos.add(grupo);
    }

    public void registrarEstadio(Estadio estadio) {
        estadios.add(estadio);
    }

    public List<Partido> generarFixture() {
        List<Partido> fixture = new ArrayList<>();
        for (Grupo grupo : grupos) {
            List<Equipo> equipos = grupo.getEquipos();
            for (int i = 0; i < equipos.size(); i++) {
                for (int j = i + 1; j < equipos.size(); j++) {
                    Partido partido = new Partido(equipos.get(i), equipos.get(j), estadios.get(0));  // simplificado para usar el primer estadio
                    fixture.add(partido); // Cambiar append por add
                }
            }
        }
        return fixture;
    }
}

