grfile = open('gr_semanal.txt', "a")


#Loop for make easy put all data, choose number 3 to break the loop
while True:
    print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Salir')
    action = input('Seleccione: ')
    if action == 1:
        food = input('Introduzca un alimento: ')
    elif action == 3:
        break