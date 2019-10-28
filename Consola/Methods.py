import vlc


class Methods:

    def __init__(self):
        pass

    # Segunda opción: mostrar radios disponibles
    def showRadios(self):
        radios = open("links.txt", "r")
        numLines = 0
        print("\nEmisoras disponibles:")
        for line in radios:
            numLines += 1
            if numLines % 2:
                print("\t", line.strip("\n"))
        print("\n".strip("\n"))
        radios.close()

    # Tercera opción: mostrar radios disponibles con sus links
    def showDetailedRadios(self):
        lines = []
        radios = open("links.txt", "r")
        print("\n".strip("\n"))
        print("Emisoras disponibles:\n")
        for line in radios:
            lines.append(line.strip("\n"))
            print("\t", line.strip("\n"))
        print("\n".strip("\n"))
        radios.close()

    # Primera opción: reproducir radio
    def selectRadio(self):
        index = 0
        indexReproduction = 0
        conditionExitWhile = False
        lines = []
        radios = open("links.txt", "r")
        Methods().showRadios()
        for line in radios:
            lines.append(line.strip("\n"))
        numSelectRadio = int(input("Seleccione la emisora desea escuchar: "))
        if (len(lines) / 2) >= numSelectRadio > 0:
            try:
                volumeLevel = int(input("\nIngrese el nivel de volumen de reproducción\ndel 0 "
                                        "al 100 (por defecto será 40): "))
            except:
                volumeLevel = 40

            index = (numSelectRadio * 2) - 1
            indexReproduction = index - 1
            Instance = vlc.Instance()
            player = Instance.media_player_new()
            Media = Instance.media_new(lines[index])
            print("\nReproduciendo:", lines[indexReproduction][3:])
            Media.get_mrl()
            player.set_media(Media)
            player.play()
            player.audio_set_volume(volumeLevel)
            while not conditionExitWhile:
                try:
                    userStop = input("\nPara detener la reproducción y regresar al menú"
                                     "\nprincipal ingrese la letra " + '"' + "s" + '"' + ". Si desea"
                                     "cambiar el volumen\nde reproducción, ingrese el nuevo volumen "
                                     "deseado: ".strip("\n"))

                    if userStop == "s":
                        player.stop()
                        print("\nSe ha detenido la reproducción.\n")
                        conditionExitWhile = True

                    elif 0 <= int(userStop) <= 100:
                        player.audio_set_volume(int(userStop))
                        print("\nEl volumen de reproducción ha cambiado a:", int(userStop))

                    else:
                        print("\nNivel de volumen no válido.")

                except:
                    conditionExitWhile = False
                    print("\nOpción no existente. Ingrese una opción válida.")

        else:
            print("Radio no válida. Intente nuevamente.\n")
        radios.close()

    # Cuarta opción: agregar radio
    def addRadio(self):
        radios = open("links.txt", "a")
        nameLink = []
        nameLink.append(input("Para agregar una nueva emisora, ingrese el índice numérico,\n"
                              "luego un punto, un espacio y a continuación el nombre de la emisora: "))
        nameLink.append("\n")
        nameLink.append(input("Ahora ingrese el link de la emisora y luego coloque"
                              "un espacio antes de pulsar Enter: ")[:-1])
        radios.writelines(nameLink)
        radios.writelines("\n")
        radios.close()
        print("\nSu emisora se ha agregado con éxito.\n")

    # Quinta opción: eliminar radio
    def deleteRadio(self):
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
        print("\n¿Está seguro de que desea eliminar la emisora "+'"'+chainRadios[deleteIndex - 1][3:]+'"'+"?")
        deleteDecision = input("Para cancelar la operación solo pulse " + '"' + "Enter" + '"' + ".\n"
                               "Para confirmar la desición escriba SI en mayúsculas: ")
        if deleteDecision == "SI":
            radiosReopen = open("links.txt", "w")
            chainRadios.pop(deleteIndex)
            chainRadios.pop(deleteIndex - 1)
            for z in chainRadios:
                index2 += 1
                radiosReopen.write(chainRadios[index2 - 1])
                radiosReopen.write("\n")
            radiosReopen.write("\n".strip("\n"))
            print("\nRadio borrada con éxto.\n")
        else:
            print("\nOperación cancelada.\n")
        radios.close()
