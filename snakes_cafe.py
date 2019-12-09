appetizers = {
    'wings' : 0,
    'cookies' : 0,
    'spring rolls' : 0
}
entrees = {
    'salmon' : 0,
    'steak' : 0,
    'meat tornado' : 0,
    'a literal garden': 0
}
desserts = {
    'ice cream' : 0,
    'cake' : 0,
    'pie' : 0,
}
drinks = {
    'coffee' : 0,
    'tea' : 0,
    'unicorn tears' : 0,
}

def exit_app():
  print('Thank you. Come Again!')
  exit()

def start_up():
  print('*' * 38)
  print('**    Welcome to the Snakes Cafe!   **')
  print('**    Please see our menu below.    **')
  print('**')
  print('** To quit at any time, type "quit" **')
  print('*' * 38)
  print('')
  print('Appetizers')
  print('----------')
  for i in appetizers:
    print(i)
  print('')
  print('Entrees')
  print('-------')
  for i in entrees:
    print(i)
  print('')
  print('Desserts')
  print('-------')
  for i in desserts:
    print(i)
  print('')
  print('Drinks')
  print('-------')
  for i in drinks:
    print(i)
  return ''
  
print(start_up())

while True:
  print('*' * 35)
  print('** What would you like to order? **')
  print('*' * 35)
  answer = input()
  if answer == 'quit':
    exit_app()
  if answer in drinks:
    drinks[answer] += 1
    print('** ' + str(drinks[answer]) + ' order of ' + answer + ' have been added to your meal **')
  elif answer in appetizers:
    appetizers[answer] += 1
    print('** ' + str(appetizers[answer]) + ' order of ' + answer + ' have been added to your meal **')
  elif answer in entrees:
    entrees[answer] += 1
    print('** ' + str(entrees[answer]) + ' order of ' + answer + ' have been added to your meal **')
  elif answer in desserts:
    desserts[answer] += 1
    print('** ' + str(desserts[answer]) + ' order of ' + answer + ' have been added to your meal **')
  else:
    print('please enter something from the Menu')
