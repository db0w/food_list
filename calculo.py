grfile = open('gr_semanal.txt', "a")


#Loop for make easy put all data, choose number 3 to break the loop
gramage = 0
food = ''
while True:
    print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Salir')
    action = int(input('Seleccione: '))
    if action == 1:
        food = input('Introduzca un alimento: ')
    if action == 2:
        #Loop for enter infinite quantities, press 0 to break it
        while True:
            print('Para salir introducir 0')
            gr = int(input('Agrega los gramos: '))
            if gr == 0:
                break
            else:
                gramage += gr
    elif action == 3:
        break

lstfood = dict()
lstfood[food] = gramage

grfile.write(str(lstfood))