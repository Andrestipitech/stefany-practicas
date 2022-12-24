from datos import palabras,puntajes_c
import random



def esconderLetra(palabra):
    estado =''
    longitud = len(palabra)
    count=0
    while count<longitud:
        estado +='*'
        count +=1
    return estado

def cambiarLetra(palabra, letra, estado):
    nuevo_estado =''
    longitud = len(palabra)
    count=0
    while count < longitud:
        if palabra[count] == letra:
            nuevo_estado += letra
        else:
            nuevo_estado +=estado[count]
        count +=1
    return nuevo_estado

def jugar():
    categoria_alea = random.choice(list(palabras.keys()))
    palabra_ale = random.choice(palabras[categoria_alea])
    print(categoria_alea,palabra_ale)
    puntaje =0
    count_error =0
    palabra_juego = palabra_ale.lower()
    palabra_oculta = esconderLetra(palabra_ale.lower())
    print(palabra_oculta)
    while True:
        letra_user = input("Ingrese la letra: ")
        if letra_user in palabra_juego:
            print("correcto")
            palabra_juego = palabra_juego.replace(letra_user,'')
            puntaje += puntajes_c[categoria_alea][letra_user]
            palabra_oculta = cambiarLetra(palabra_ale.lower(), letra_user, palabra_oculta)
            print(palabra_oculta)
            if palabra_juego == '':
                print("Ganaste !!!!!!!!!!!")
                break
        else:
            print("intenta de nuevo")
            count_error +=1
            if count_error > 2:
                print("perdiste")
                break
    print(puntaje)
