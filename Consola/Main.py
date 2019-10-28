<<<<<<< HEAD
from Functions import *
from Consola.Functions import Functions


class RadioStreamer:

    exitProgram = False
    exitMenu = False

    def __init__(self):
        print("Bienvenido a Radio Streamer.\n"
              "Copyright ©2019. All rights reserved. Julián Software Foundation.\n")
        functions = Functions()

        while not self.exitProgram:

            while not self.exitMenu:
                try:
                    print("Menú Principal.\nSeleccione una acción:")
                    numMenu = int(input("\t1. Elegir emisora para reproducir\n"
                                        "\t2. Mostrar lista de emisoras disponibles\n"
                                        "\t3. Mostrar lista de emisoras detallada, con sus links\n"
                                        "\t4. Agregar emisora\n\t5. Eliminar emisora\n\t6. Salir del programa\n"
                                        "Su elección: "))

                    if numMenu == 1:
                        functions.selectRadio()

                    elif numMenu == 2:
                        functions.showRadios()

                    elif numMenu == 3:
                        functions.showDetailedRadios()

                    elif numMenu == 4:
                        functions.addRadio()

                    elif numMenu == 5:
                        functions.deleteRadio()

                    elif numMenu == 6:
                        self.exitProgram = True
                        self.exitMenu = True
                        print("\nPrograma cerrado con éxito, ¡Hasta luego!")

                    elif numMenu == 117:
                        pass

                    else:
                        print("\nError, opción no existente. Por favor elija una opción válida.")
                        self.exitMenu = False

                except:
                    print("\nError, opción no existente. Por favor elija una opción válida.")
                    self.exitMenu = False
                    pass


RadioStreamer()
=======
import vlc
import time

cont = False
methodCalled = False

def showRadios():
    radios = open("links.txt", "r")
    numLines = 0
    print("\nEmisoras disponibles:")
    for line in radios:
        numLines = numLines + 1
        if numLines % 2:
            print("\t", line.strip("\n"))
    global methodCalled
    methodCalled = True
    radios.close()

def showDetailedRadios():
    lines = []
    counter = 0
    radios = open('links.txt', 'rt')
    print("\n".strip("\n"))
    print("Emisoras disponibles:\n")
    for line in radios:
        lines.append(line.strip("\n"))
        print("\t", line.strip("\n"))

def selectRadio():
    index = 0
    indexReproduction = 0
    lines = []
    radios = open('links.txt', 'rt')
    for line in radios:
        lines.append(line.strip("\n"))
    if methodCalled == True:
        numSelectRadio = int(input("Seleccione que emisora desea escuchar: " ))
    else:
        numSelectRadio = int(input("\nSeleccione que emisora desea escuchar: "))
    index = (numSelectRadio * 2) - 1
    indexReproduction = index - 1
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(lines[index])
    print("\nReproduciendo:", lines[indexReproduction][3:])
    #print(lines[index])
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    player.audio_set_volume(60)
    time.sleep(999999)
    radios.close()

def addRadio():
    radios = open("links.txt", "a")
    nameLink = []
    nameLink.append(str(input("Para agregar una nueva emisora, ingrese el índice numérico,\n"
                              "luego un punto, un espacio y a continuación el nombre de la emisora: ")))
    nameLink.append(str("\n"))
    nameLink.append(str(input("Ahora ingrese el link de la emisora: ")))
    radios.writelines(nameLink)
    radios.close()
    print("Su emisora se ha agregado con éxito.")

def deleteRadio():
    pass

print("Bienvenido a Radio Streamer\nSeleccione una acción:")

while cont == False:
    try:
        numMenu = int(input("\t1. Mostrar lista de emisoras\n\t2. Mostrar lista detallada de emisoras\n"
                            "\t3. Agregar emisora\n\t4. Eliminar emisora\nSu elección: "))
        cont = True
        if numMenu == 1:
            showRadios()
            selectRadio()

        elif numMenu == 2:
            showDetailedRadios()
            selectRadio()

        elif numMenu == 3:
            addRadio()

        elif numMenu == 4:
            deleteRadio()

        else:
            print("\nError, opción no existente\nElija una opción válida: ")
            cont = False

    except:
        print("\nError, opción no existente\nElija una opción válida: ")
        cont = False
>>>>>>> 37c7593b034ed207409bb392da6ed1806802605a
