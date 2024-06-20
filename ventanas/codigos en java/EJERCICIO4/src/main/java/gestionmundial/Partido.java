package gestionmundial;

public class Partido {
    private Equipo equipoLocal;
    private Equipo equipoVisitante;
    private Estadio estadio;
    private String resultado;

    public Partido(Equipo equipoLocal, Equipo equipoVisitante, Estadio estadio) {
        this.equipoLocal = equipoLocal;
        this.equipoVisitante = equipoVisitante;
        this.estadio = estadio;
        this.resultado = null;
    }

    public Equipo getEquipoLocal() {
        return equipoLocal;
    }

    public void setEquipoLocal(Equipo equipoLocal) {
        this.equipoLocal = equipoLocal;
    }

    public Equipo getEquipoVisitante() {
        return equipoVisitante;
    }

    public void setEquipoVisitante(Equipo equipoVisitante) {
        this.equipoVisitante = equipoVisitante;
    }

    public Estadio getEstadio() {
        return estadio;
    }

    public void setEstadio(Estadio estadio) {
        this.estadio = estadio;
    }

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    public void jugarPartido(String resultado) {
        this.resultado = resultado;
    }

    public String mostrarResultado() {
        return "Partido: " + equipoLocal.getNombre() + " vs " + equipoVisitante.getNombre() + ", Resultado: " + resultado;
    }
}

