# Write in an existing text file
wfile = open('gr_semanal.txt', "w")

#WRITE PART
# Variables to save data from loop for write in dictionary
gramage = 0
food = None

# Dictionary that have all the entered data for write in a file text
lstfood = dict()

# Infinite loop allow user enter infinite data
while True:
    # Print statement to explain how work the loop
    print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Guardar en diccionario\n4 = Mostrar lista\nexit = Salir')

    # Input for choose what if must run
    action = input('Seleccione: ')

    if action == '1':
        # Input with print, explain how must user write the food name
        food = input('Introduzca un alimento en minúsculas, sin acentos, singular y con "_" como separación: ')
        # Iterate throw dictionay to find food already entered
        for key,value in lstfood.items():
            if food == str(key):
                print('Alimento ya agregado, actualizar', key, value)
                food = key
                gramage = int(value)
    if action == '2':
        # Loop for enter and sum infinite quantities, press 0 to break it
        while True:
            print('Para salir introducir 0')
            gr = int(input('Agrega los gramos: '))
            if gr == 0:
                break
            else:
                gramage += gr
    elif action == '3':
        # First prevent if no food or gramage was added, else add food and gramage in dictionary
        if gramage is 0 or food is None:
            print(str.upper("Atención ningún gramo o alimento añadido!"))
        else:
            lstfood[food] = str(gramage)
            gramage = 0
            print('Guardado:', lstfood)
    elif action == '4':
        # Print dictionary to revise what food was entered
        print(lstfood)
    elif action == 'exit':
        # Break while loop
        break

# Write dictionary into file text if this have data
if lstfood != {}:
    wfile.write(str(lstfood.items()))
    print('Guardado!')
else:
    print(str.upper('Diccionario vacío!'))

#READER PART