from os import system

def main():

    # Comenzaremos registrando la informcaión de partida del sátelite 

    Altitud_Inicial = int(input("Por favor, ingrese la altitud inicial del satélite en km: "))
    system("cls")
    Coeficiente_Arrastre = float(input("Por favor, ingrese el coeficiente de arrastre (Ej: 0.01): "))
    system("cls")
    Altitud_Minima =  int(input("Por favor, ingrese la altitud mínima segura en km: "))
    system("cls")

    # Simulación de orbitas

    Contador_Orbitas = 0
    Nueva_Altitud_Inicial = Altitud_Inicial

    while Nueva_Altitud_Inicial > Altitud_Minima:
        Altitud_Perdida = Nueva_Altitud_Inicial * Coeficiente_Arrastre
        Nueva_Altitud_Inicial -= Altitud_Perdida
        Coeficiente_Arrastre += 0.0001
        Contador_Orbitas += 1
        Nueva_Altitud = Nueva_Altitud_Inicial

        print(f"El satélite ha completado la orbita {Contador_Orbitas} llegando a una altitud de {Nueva_Altitud}km.")

        if Altitud_Perdida < (0.001):
            break

    if Altitud_Perdida < (0.001):
        print(f"El satélite se ha estabilizado luego de {Contador_Orbitas} órbitas completadas. La altitud final alcanzada fue de {Nueva_Altitud}.")
    else:
        print(f"El stálite ha reingresado a la atmósfera terrestre luego de {Contador_Orbitas} órbitas completadas alcanzando una altitud de {Nueva_Altitud}.")

if __name__ == "__main__":
    main()
