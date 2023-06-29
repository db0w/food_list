grfile = open('gr_semanal.txt', "a")


def enter_action():
  print('Qué quieres hacer?\n1 = Agregar alimento\n2 = Agregar cantidad\n3 = Salir')
  action = input('Seleccione: ')
  return int(action)

while True:
  action = enter_action()
  if action == 1:
    food = input('Introduzca un alimento: ')
  elif action == 3:
    break