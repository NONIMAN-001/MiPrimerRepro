import java.util.Scanner;

// Procedimiento de desarrollo
// Paso 1. Se crea la clase Cliente con datos básicos del cliente.
// Paso 2. Se crea la clase Cuenta que hereda Cliente y añade detalles bancarios.
// Paso 3. Se programa calcularInteres para calcular interés según tipo de cuenta.
// Paso 4. Se crea CuentaCorriente que hereda Cliente con atributos extra y método calcularInteres redefinido.
// Paso 5. Se usa Scanner para leer datos desde teclado.
// Paso 6. Se muestra toda la información y cálculos en pantalla.

// la calse cliente
class Cliente {
    private long documentoIdentidad;   //los datos que pide la guia 
    private String nombre;
    private String correoElectronico;
    private int numeroCelular;
    private String direccion;

    //el constructor de la clase cliente 
    public Cliente(long documentoIdentidad, String nombre, String correoElectronico, int numeroCelular, String direccion) { 
        this.documentoIdentidad = documentoIdentidad;
        this.nombre = nombre;
        this.correoElectronico = correoElectronico;
        this.numeroCelular = numeroCelular;
        this.direccion = direccion;
    }

    // Getters obtener valores 
    public long getDocumentoIdentidad() {
        return documentoIdentidad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public int getNumeroCelular() {
        return numeroCelular;
    }

    public String getDireccion() {
        return direccion;
    }
}

// Clase Cuenta que hereda Cliente
class Cuenta extends Cliente { //
    protected long numeroCuenta;
    protected String fechaApertura; 
    protected double saldo;
    protected int tipoCuenta; // osea 1,2,3 para tipos diferentes

    // el constructor de la clase cuenta
    public Cuenta(long documentoIdentidad, String nombre, String correoElectronico, int numeroCelular, String direccion,
                  long numeroCuenta, String fechaApertura, double saldo, int tipoCuenta) {
        super(documentoIdentidad, nombre, correoElectronico, numeroCelular, direccion);
        this.numeroCuenta = numeroCuenta;
        this.fechaApertura = fechaApertura;
        this.saldo = saldo;
        this.tipoCuenta = tipoCuenta;
    }

    // este es el Método para calcular interés según tipo de cuenta
    public double calcularInteres() {
        double tasaInteres = 0;
        switch(tipoCuenta) {
            case 1: tasaInteres = 1.5; break; //break para que no siga evaluando
            case 2: tasaInteres = 1.7; break;
            case 3: tasaInteres = 1.6; break;
            default: tasaInteres = 0; break;
        }
        return saldo * tasaInteres / 100;
    }

    // Método para mostrar información de la cuenta la obtiene y la muestra 
    public void mostrarInformacion() {
        System.out.println("Cliente: " + getNombre() + ", Documento: " + getDocumentoIdentidad());
        System.out.println("Cuenta: " + numeroCuenta + ", Fecha apertura: " + fechaApertura);
        System.out.println("Saldo: " + saldo);
        System.out.println("Interes mensual: " + calcularInteres());
        System.out.println("Saldo con interes: " + (saldo + calcularInteres()));
    }
}

// Clase CuentaCorriente que hereda Cliente
class CuentaCorriente extends Cliente {
    private long numeroCuenta;
    private String fechaApertura;
    private double saldo;
    private double porcentajeInteres;
    private double valorSobregiro;

    //su constructor
    public CuentaCorriente(long documentoIdentidad, String nombre, String correoElectronico, int numeroCelular, String direccion,
                           long numeroCuenta, String fechaApertura, double saldo, double porcentajeInteres, double valorSobregiro) {
        super(documentoIdentidad, nombre, correoElectronico, numeroCelular, direccion);
        this.numeroCuenta = numeroCuenta;
        this.fechaApertura = fechaApertura;
        this.saldo = saldo;
        this.porcentajeInteres = porcentajeInteres;
        this.valorSobregiro = valorSobregiro;
    }

    // Sobrescribir método para calcular interés
    public double calcularInteres() {
        return saldo * porcentajeInteres / 100;
    }

    // Método para mostrar información de la cuenta corriente
    public void mostrarInformacion() {
        System.out.println("Cliente: " + getNombre() + ", Documento: " + getDocumentoIdentidad());
        System.out.println("Cuenta Corriente: " + numeroCuenta + ", Fecha apertura: " + fechaApertura);
        System.out.println("Saldo: " + saldo + ", Sobregiro permitido: " + valorSobregiro);
        System.out.println("Interes mensual: " + calcularInteres());
        System.out.println("Saldo con interes: " + (saldo + calcularInteres()));
    }
}

//el main xd
public class Ejemplo2B{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Leer datos Cliente y Cuenta
        System.out.println("Ingrese datos del cliente y cuenta de ahorro:");

        System.out.print("Documento de identidad: ");
        long doc = sc.nextLong();
        sc.nextLine(); 

        System.out.print("Nombre: ");
        String nombre = sc.nextLine();

        System.out.print("Correo electrónico: ");
        String correo = sc.nextLine();

        System.out.print("Número de celular: ");
        int celular = sc.nextInt();
        sc.nextLine();

        System.out.print("Dirección: ");
        String direccion = sc.nextLine();

        System.out.print("Número de cuenta: ");
        long cuentaNum = sc.nextLong();
        sc.nextLine();

        System.out.print("Fecha de apertura (aaaa/mm/dd): ");
        String fecha = sc.nextLine();

        System.out.print("Saldo: ");
        double saldo = sc.nextDouble();

        System.out.print("Tipo de cuenta (1 Ahorro Diario, 2 Cuenta Joven, 3 Tradicional): ");
        int tipo = sc.nextInt();

        Cuenta cuenta = new Cuenta(doc, nombre, correo, celular, direccion, cuentaNum, fecha, saldo, tipo);
        System.out.println("\nInformación cuenta de ahorro:");
        cuenta.mostrarInformacion();

        // Leer datos Cuenta Corriente
        System.out.println("\nIngrese datos de cuenta corriente:");

        System.out.print("Documento de identidad: ");
        long doc2 = sc.nextLong();
        sc.nextLine();

        System.out.print("Nombre: ");
        String nombre2 = sc.nextLine();

        System.out.print("Correo electrónico: ");
        String correo2 = sc.nextLine();

        System.out.print("Número de celular: ");
        int celular2 = sc.nextInt();
        sc.nextLine();

        System.out.print("Dirección: ");
        String direccion2 = sc.nextLine();

        System.out.print("Número de cuenta corriente: ");
        long cuentaNum2 = sc.nextLong();
        sc.nextLine();

        System.out.print("Fecha de apertura (aaaa/mm/dd): ");
        String fecha2 = sc.nextLine();

        System.out.print("Saldo: ");
        double saldo2 = sc.nextDouble();

        System.out.print("Porcentaje de interés mensual: ");
        double porcentajeInteres = sc.nextDouble();

        System.out.print("Valor permitido de sobregiro: ");
        double valorSobregiro = sc.nextDouble();

        CuentaCorriente cuentaCorriente = new CuentaCorriente(doc2, nombre2, correo2, celular2, direccion2,
                cuentaNum2, fecha2, saldo2, porcentajeInteres, valorSobregiro);

        System.out.println("\nInformación cuenta corriente:");
        cuentaCorriente.mostrarInformacion();

        sc.close();
    }
}
