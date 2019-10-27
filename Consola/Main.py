import vlc
import time

exitProgram = False
exitMenu = False
methodCalled = False

#Segunda opción
def showRadios():
    radios = open("links.txt", "r")
    numLines = 0
    print("\nEmisoras disponibles:")
    for line in radios:
        numLines += 1
        if numLines % 2:
            print("\t", line.strip("\n"))
    print("\n".strip("\n"))
    radios.close()

#Tercera opción
def showDetailedRadios():
    lines = []
    radios = open("links.txt", "r")
    print("\n".strip("\n"))
    print("Emisoras disponibles:\n")
    for line in radios:
        lines.append(line.strip("\n"))
        print("\t", line.strip("\n"))
    print("\n".strip("\n"))
    radios.close()

#Primera opción
def selectRadio():
    index = 0
    indexReproduction = 0
    lines = []
    radios = open("links.txt", "r")
    showRadios()
    for line in radios:
        lines.append(line.strip("\n"))
    numSelectRadio = int(input("Seleccione la emisora desea escuchar: "))
    index = (numSelectRadio * 2) - 1
    indexReproduction = index - 1
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(lines[index])
    print("\nReproduciendo:", lines[indexReproduction][3:], "\n")
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    player.audio_set_volume(80)
    #time.sleep(1)
    userStop = input("Para detener la reproducción ingrese la letra q: ")
    if userStop == "q":
        exit()
        exitProgram = True
        radios.close()
    #radios.close()

#Cuarta opción
def addRadio():
    radios = open("links.txt", "a")
    nameLink = []
    nameLink.append(str(input("Para agregar una nueva emisora, ingrese el índice numérico,\n"
                              "luego un punto, un espacio y a continuación el nombre de la emisora: ")))
    nameLink.append(str("\n"))
    nameLink.append(input("Ahora ingrese el link de la emisora: ")[:-1])
    radios.writelines(nameLink)
    radios.writelines("\n")
    radios.close()
    print("Su emisora se ha agregado con éxito.")

#Quinta opción
def deleteRadio():
    radios = open("links.txt", "r")
    chainRadios = []
    index1 = 0
    index2 = 0
    print("\nRadios disponibles:")
    for line in radios:
        index1 += 1
        chainRadios.append(line.strip("\n"))
        if index1 % 2:
            print("\t", line.strip("\n"))
    askDelete = int(input("Elija el índice de la emisora que desea eliminar: "))
    deleteIndex = ((askDelete * 2) - 1)
    radios.close()
    radiosReopen = open("links.txt", "w")
    chainRadios.pop(deleteIndex)
    chainRadios.pop(deleteIndex - 1)
    deleteDesicion = input("¿Está seguro de que desea eliminar esta emisora?\n"
                           "Para confirmar la desición escriba SI en mayúsculas: ")
    if deleteDesicion == "SI":
        for z in chainRadios:
            index2 += 1
            radiosReopen.write(chainRadios[index2 - 1])
            radiosReopen.write("\n")
        radiosReopen.write("\n".strip("\n"))
        print("Radio borrada con éxto.")
    else:
        print("\nOperación cancelada.")
    radios.close()

print("Bienvenido a Radio Streamer")

while exitProgram == False:

    while exitMenu == False:
        try:
            print("Seleccione una acción:")
            numMenu = int(input("\t1. Elegir emisora\n\t2. Mostrar lista de emisoras\n"
                                "\t3. Mostrar lista de emisoras detallada, con sus links\n"
                                "\t4. Agregar emisora\n\t5. Eliminar emisora\n\t6. Salir del programa\n"
                                "Su elección: "))
            #conditionEnterMenu = True
            if numMenu == 1:
                selectRadio()

            elif numMenu == 2:
                showRadios()

            elif numMenu == 3:
                showDetailedRadios()

            elif numMenu == 4:
                addRadio()

            elif numMenu == 5:
                deleteRadio()

            elif numMenu == 6:
                exitProgram = True
                exitMenu = True
                print("\nPrograma cerrado con éxito, ¡Hasta luego!")

            else:
                print("\nError, opción no existente. Por favor elija una opción válida.")
                exitMenu = False

        except:
            print("\nError, opción no existente. Por favor elija una opción válida.")
            exitMenu = False
            pass
