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
    posicionNewRadio = 0
    link = ""
    nameLink.append(str(input("Para agregar una nueva emisora, ingrese el índice numérico,\n"
                              "luego un punto, un espacio y a continuación el nombre de la emisora: ")))
    nameLink.append(str("\n"))
    link = str(input("Ahora ingrese el link de la emisora: "))

    nameLink.
    #for x in range(len(nameLink)):
        #nameLink
    radios.writelines(nameLink)
    #radios.writelines("".strip(" "))
    radios.writelines("\n")
    radios.close()
    print("Su emisora se ha agregado con éxito.")

def deleteRadio():
    radios = open("links.txt", "r")
    chainRadios = []
    c = 0
    d = 0
    print("\nRadios disponibles:")
    for line in radios:
        c = c + 1
        chainRadios.append(line.strip("\n"))
        if c % 2:
            print("\t", line.strip("\n"))
    #print("Esto es chainRadios:", chainRadios)
    askDelete = int(input("Elija el índice de la emisora que desea eliminar: "))
    deleteIndex = ((askDelete * 2) - 1)
    radios.close()
    radiosReopen = open("links.txt", "w")
    #print("deleteIndex:", deleteIndex)
    chainRadios.pop(deleteIndex)
    chainRadios.pop(deleteIndex - 1)
    #print("Esto es chainRadios final:", chainRadios)
    for z in chainRadios:
        d = d + 1
        # if d == 1:
        # print("¿Está seguro de que desea eliminar esta emisora?")
        # deleteDesicion = int(input("Presione 0 para cancelar ó 1 para continuar: "))
        # pass
        radiosReopen.write(chainRadios[d - 1])
        radiosReopen.write("\n")
    radiosReopen.write("\n".strip("\n"))
    print("Radio borrada con éxto.")
    radios.close()

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
        #print("\nError, opción no existente\nElija una opción válida: ")
        #cont = False
        pass
