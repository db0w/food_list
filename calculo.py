# Variables to save data from loop for write in dictionary
gramage = 0
food = ''

# Dictionary that have all the entered data for write in a file text
dfood = dict()
# Read existing data and add it into dictionary
rfile = open('gr_semanal.txt')
for line in rfile:
    line.rstrip()
    word = line.split()
    dfood[word[0]] = word[2]

# Infinite loop allow user enter infinite data
while True:
    # Print statement to explain how work the loop
    print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Guardar en diccionario\n4 = Mostrar lista\nexit = Salir')

    # Input for choose what if must run
    action = input('Seleccione: ')

    if action == '1':
        # Turn food variable to empty
        food = ''
        # Input with print, explain how must user write the food name
        inpfood = input('Introduzca un alimento: ')
        # Switch inpfood to internal name convention
        for f in inpfood:
            if f.isupper():
                f = str.lower(f)
            if f==' ':
                f = '%'
            food += f
        # Switch spanish plural to spanish singular
        if food.endswith('es'):
            food = food[:-2]
        elif food.endswith('s'):
            food = food[:-1]
        # Iterate throw dictionay to find food already entered
        for key,value in dfood.items():
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
        if gramage is 0 or food is '':
            print(str.upper("Atención ningún gramo o alimento añadido!"))
        else:
            dfood[food] = str(gramage)
            gramage = 0
            print('Guardado:', dfood)
    elif action == '4':
        # Print dictionary to revise what food was entered
        print(dfood)
    elif action == 'exit':
        # Break while loop
        break

# Write dictionary into file text if dict have data
if dfood != {}:
    # Write in an existing text file
    wfile = open('gr_semanal.txt', "w")
    for f, q in dfood.items():
        word = f + ' = ' + q + '\n'
        wfile.write(word)
    print('Guardado!')
else:
    print(str.upper('Diccionario vacío!'))