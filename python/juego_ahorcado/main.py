# crear un menu que tengas 3 opciones 1) jugar, 2)puntaje, 0) salir
from operaciones import jugar
while True:
    opc = input("""Que desea realizar
    1) Jugar
    2) Puntaje
    0) Salir
    """)
    if opc == '1':
        print("Empieza el juego")
        jugar()
    elif opc =='2':
        print("puntaje")
    elif opc =='0':
        print("gracias.....!!!")
        break
    else:
        print("opcion invalida intenta de nuevo")
