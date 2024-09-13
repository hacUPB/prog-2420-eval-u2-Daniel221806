from os import system
import datetime
import random

def Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades):
    while True:
        Respuesta_1 = Ciudad_Destino
        Ciudad_Destino = Ciudad_Destino.upper()
        system("cls")
        if Ciudad_Destino in Posibles_Ciudades:
            print(f"Muy bien, has elegido {Respuesta_1}.")
            break
        else:
            print(f"{Respuesta_1} no es un respuesta válida.")
            Ciudad_Destino = str(input(f"Elije una de las ciudades a las cuales podemos llevarte {Posibles_Ciudades}: "))
    
    return Respuesta_1



def main():

    # Primero conoceremos al cliente y generaremos un saludo personalizado.

    Genero = str(input("¿Cómo te gustaría que nos dirigiéramos hacía ti?: Señor o Señora: "))
    Nombre = str(input("Por favor, ingresa tu nombre: "))
    Apellido = str(input("Por favor, ingresa tu apellido: "))

    system("cls")

    print(f"{Genero}, {Nombre} {Apellido} ¡estamos muy contentos de servirte en TortugüitaFly!")
    
    # Ahora, pediremos al cliente seleccionar su ciudad de origen y destiino.

    Posibles_Ciudades = ["MEDELLIN", "BOGOTA", "CARTAGENA"]

    while True:

        print("¡Por favor, no uses tildes en ninguna de tus respuestas!")
        Ciudad_Origen = str(input("Indica tu ciudad de origen: Medellin, Bogota o Cartagena: "))

        system("cls")

        Respuesta = Ciudad_Origen
        Ciudad_Origen = Ciudad_Origen.upper()

        if Ciudad_Origen in Posibles_Ciudades:
            print(f"Muy bien, has elegido {Respuesta}.")
            break
        else:
            print(f"Lamentablemente no volamos desde {Respuesta}. Intenta de nuevo.")

    while True:
        print("Ahora indica tu ciudad de destino: ")

        if Ciudad_Origen == "MEDELLIN":
            Ciudad_Destino = str(input("Bogota o Cartagena: "))
            Posibles_Ciudades_Destino = ["BOGOTA", "CARTAGENA"]
            Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades_Destino)
            break
        elif Ciudad_Origen == "BOGOTA":
            Ciudad_Destino = str(input("Medellin o Cartagena: "))
            Posibles_Ciudades_Destino = ["MEDELLIN", "CARTAGENA"]
            Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades_Destino)
            break
        elif Ciudad_Origen == "CARTAGENA":
            Ciudad_Destino = str(input("Medellin o Bogota: "))
            Posibles_Ciudades_Destino = ["MEDELLIN", "BOGOTA"]
            Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades_Destino)
            break
    
    # Preguntaremos al cliente qué día quiere viajar

    Fecha_Ingresada = input("Indica a fecha en la que quieres viajar (dd/mm/aaaa): ")
    Fecha_Vuelo = datetime.datetime.strptime(Fecha_Ingresada, "%d/%m/%Y")
    system("cls")

    Días_Semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    Meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agoto", "septiembre", "octubre", "noviembre", "diciembre"]
    
    Día_Semana = Fecha_Vuelo.weekday()
    Día_Vuelo = Días_Semana[Día_Semana]
    Día = Fecha_Vuelo.day
    Mes_Vuelo = Meses[Fecha_Vuelo.month - 1]
    Año_Vuelo = Fecha_Vuelo.year

    print(f"¡Viajarás con TortugüitaFly el día {Día_Vuelo} {Día} de {Mes_Vuelo} del {Año_Vuelo}!")

    # Determinamos el valor del pasaje

    if Ciudad_Origen == "MEDELLIN":
        if Ciudad_Destino == "BOGOTA":
            Distancia_Ciudades = 240
        else:
            Distancia_Ciudades = 461
    elif Ciudad_Origen == "BOGOTA":
        if Ciudad_Destino == "MEDELLIN":
            Distancia_Ciudades = 240
        else:
            Distancia_Ciudades = 657
    elif Ciudad_Origen == "CARTAGENA":
        if Ciudad_Destino == "MEDELLIN":
            Distancia_Ciudades = 461
        else:
            Distancia_Ciudades = 657

    if Distancia_Ciudades < 400:
        if Día_Semana < 4:
            Precio = "79.900"
        else:
            Precio = "119.900"
    else:
        if Día_Semana < 4:
            Precio = "156.900"
        else:
            Precio = "213.000"
    
    # Preguntamos al usuario su preferencia de silla

    Posibles_Asientos = ["VENTANA", "PASILLO", "SIN PREFERENCIA", "SINPREFERENCIA"]

    while True:

        Asiento = str(input("Elije tu asiento de preferencia (ventana, pasillo, sin preferencia): "))

        system("cls")

        Respuesta2 = Asiento
        Asiento = Asiento.upper()

        if Asiento in Posibles_Asientos:
            print(f"Muy bien, has elegido {Respuesta2}.")
            break
        else:
            print(f"{Respuesta2} no es una opción válida. Intenta de nuevo.")

    if Asiento == "VENTANA":
        Asiento_Asignado = "A"
    else:
        if Asiento == "PASILLO":
            Asiento_Asignado = "C"
        else:
            Asiento_Asignado = "B"
    
    Número_Fila = random.randint(1,29)

    # Finalmente, informamos al usuario de la reserva que ha generado

    print(f"{Genero}, {Nombre} {Apellido}, tu reserva se ha confirmado. Volarás el día {Día_Vuelo} {Día} de {Mes_Vuelo} del {Año_Vuelo} desde {Ciudad_Origen} hasta {Ciudad_Destino}. Tu boleto tiene un valor de ${Precio}. Te corresponde el asiento {Número_Fila}{Asiento_Asignado}. ¡Gracias por volar con TortugüitaFLy!") 
 
    

if __name__ == "__main__":
    main()
