from os import system

def Respuesta_Destino(Ciudad_Destino, Posibles_Ciudades):
    Respuesta_1 = Ciudad_Destino
    Ciudad_Destino = Ciudad_Destino.upper()
    if Ciudad_Destino in Posibles_Ciudades:
        print(f"Muy bien, has elegido {Respuesta_1}.")
    else:
        print(f"{Respuesta_1} no es un respuesta válida. Intente de nuevo.")
    
    return Respuesta_1
    


def main():

    # Primero conoceremos al cliente y generaremos un saludo personalizado.

    Genero = str(input("¿Cómo le gustaría que nos dirigiéramos hacía usted?: Señor o Señora: "))
    Nombre = str(input("Por favor, ingrese su nombre: "))
    Apellido = str(input("Por favor, ingrese su apellido: "))

    system("cls")

    print(f"{Genero}, {Nombre} {Apellido} ¡estamos muy contentos de servirle en TortugüitaFly!")
    
    # Ahora, pediremos al cliente seleccionar su ciudad de origen y destiino.

    Posibles_Ciudades = ["MEDELLIN", "BOGOTA", "CARTAGENA"]

    while True:

        print("¡Por favor, no use tildes en ninguna de sus respuestas!")
        Ciudad_Origen = str(input("Indique su ciudad de origen: Medellín, Bogotá o Cartagena: "))

        system("cls")

        Respuesta = Ciudad_Origen
        Ciudad_Origen = Ciudad_Origen.upper()

        if Ciudad_Origen in Posibles_Ciudades:
            print(f"Muy bien, has elegido {Respuesta}.")
            break
        else:
            print(f"{Respuesta} no es una respuesta válida. Intente de nuevo.")

    while True:
        print("Ahora indique su ciudad de destino: ")

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

    

if __name__ == "__main__":
    main()
