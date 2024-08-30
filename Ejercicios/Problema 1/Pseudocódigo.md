# **Sistema de Reservas de Aerolínea**

```
Inicio

Imprimir "¿Cómo le gustaría que nos dirigiéramos hacía usted?: Señor o Señora: "
Leer G
Imprimir "Por favor, ingrese su nombre: "
Leer N
Imprimir "Por favor, ingrese su apellido: "
Leer AP
Imprimir G; N, AP " ¡estamos muy contentos de servirle en TortugüitaFly!"

Imprimir G, N, AP " por favor, seleccione su ciudad de origen: Medellín, Bogotá o Cartagena: "
Leer CO
imprimir "Ahora seleccione su ciudad de destino: "
Si CO = Medellín
    Imprimir "Bogotá o Cartagena: "
Si no 
    Si CO = Bogotá
        Imprimir "Medellín o Cartagena: "
    Si no
        Si CO = Cartagena
            Imprimir "Medellín o Bogotá"
        fin si
    fin si
fin si
Leer CD
Imprimir "¿Qué día de la semana preferiría viajar?: (lunes, martes, miercoles, jueves, viernes, sabado, domingo): "
Leer D
Imprimir "¿Qué día del mes quisiera viajar?: (1-30): "
Leer F
Si CO = Medellín
    Si CD = Bogotá
        DI = 240
    Si no
        DI = 461
    fin si
Si no 
    Si CO = Bogotá
        Si CD = Medellín
            DI = 240
        Si no
            DI = 657
        fin si
    Si no
        Si CO = Cartagena
            Si CD = Medellín
                DI = 461
            Si no
                DI = 657
            fin si
        fin si
    fin si
fin si
Si DI < 400
    Si D = lunes ó D 0 martes ó D = miercoles ó D = jueves
        P = 79900
    Si no
        P = 119900
    fin si
Si no
    Si D = lunes ó D 0 martes ó D = miercoles ó D = jueves
        P = 156900
    Si no
        P = 213000
    fin si
fin si

Imprmir "Elija su asiento de preferencia: (ventana, pasillo, sin preferencia): "
Leer A
Si A = ventana
    AA = A
Si no
    Si A = pasillo
        AA = C
    Si no
        AA = B
    fin si
fin si
N = GenerarNumeroAleatorio(1,29)
NA = N + AA

imprimir "Querido" G, N, AP " su reserva se ha confirmado. Volarás el día " D, F " de " M " desde "  CO " hasta " CD ". Tu boleto tiene un valor de $" P ". Tu asiento es " NA ". ¡Gracias por volar con TortugüitaFly!"

FIN