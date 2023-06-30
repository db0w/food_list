grfile = open('gr_semanal.txt', "a")


#Loop for make easy put all data, choose number 3 to break the loop
gramage = 0
food = None
lstfood = dict()
while True:
    print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Guardar en diccionario\n4 = Salir')
    action = int(input('Seleccione: '))
    if action == 1:
        food = input('Introduzca un alimento en minúsculas, sin acentos, singular y con "_" como separación: ')
        for key in lstfood.keys():
            if food == key:
                print('Alimento ya agregado')
                food = None
    if action == 2:
        #Loop for enter and sum infinite quantities, press 0 to break it
        while True:
            print('Para salir introducir 0')
            gr = int(input('Agrega los gramos: '))
            if gr == 0:
                break
            else:
                gramage += gr
    elif action == 3:
        if gramage is None or food is None:
            print(str.upper("Atención ningún gramo o alimento añadido!"))
        else:
            lstfood[food] = str(gramage)
            gramage = None
            print('Guardado:', lstfood)
    elif action == 4:
        break
    
if lstfood != {}:
    grfile.write(str(lstfood))
else:
    print(str.upper('Diccionario vacío!'))