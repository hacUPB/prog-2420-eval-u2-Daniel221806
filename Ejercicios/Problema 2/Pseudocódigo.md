# **SIMULACIÓN DE ORBITA DE UN SATÉLITE**

```
Inicio

Imprimir "Por favor, ingrese la altitud inicial del satélite: "
Leer AI
Imprimir "Por favor, ingrese el coeficiente de arastre: "
Leer CA
Imprimir  "Por favor, ingrese la altitud mínima segura: "
Leer AM

O = 0
NAM = AI
Mientras NAM > AM
    AP = NAM * CA
    NAM = NAM - AP
    CA = CA + 0,0001
    O = O + 1
    NA = NAM
    Si AP < 0,00001
        NAM = AM - 1
    fin si
fin mientras
Si Ap < 0,00001
    Imprimir "El satélite se ha estabilizado luego de " O " órbitas completadas. La altitud final alcanzada fue de: " NA
Si no
    Imprimir "El satélite ha reingresado a la atmósfera terrestre luego de " O " órbitas."
fin si
Fin