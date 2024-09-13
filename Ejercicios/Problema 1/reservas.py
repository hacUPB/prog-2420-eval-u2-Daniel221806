from os import system
import datetime

def Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades):
    while True:
        Respuesta_1 = Ciudad_Destino
        Ciudad_Destino = Ciudad_Destino.upper()
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
        system("cls")
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

    while True:
        Fecha_Ingresada= input("Indica a fecha en la que quieres viajar (dd/mm/aaaa): ")
        Fecha_Vuelo = datetime.datetime.strptime(Fecha_Ingresada, "%d/%m/%Y")
        if Fecha_Vuelo < datetime.now():
            print("En TortugüitaFly ofrecemos un excelente servicio, pero en este momento no podemos llevarte al pasado. Por Favor, selecciona una fecha válida")
    
            
    
    

if __name__ == "__main__":
    main()
