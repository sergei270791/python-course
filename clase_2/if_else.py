
#pedro tiene x años
#print('pedro tiene',x,'años.')
#print('pedro tiene {} años.'.format(x))
#print(type(x))

#x=10
#print(x)
#x=x**3
#print(x)
#x=x//89 # '%'  es para el residuo de la division 
#print(x)

# name=input('what\'s your name? ')
# age=int(input('How old are you? '))

# # print(type(name))
# # print(type(age))

# if age < 0:
#     print('Error! an age can\'t be negative')
# else:
#     print('hi',name,'\b!')
#     print('you are',age,'years old!')

radio=int(input('insertar el radio del circulo '))
if radio < 0:
  print('Error el radio no puede ser negativo')
else:
  print('El radio es',radio)
  if radio > 0:
    radio=radio**2
    radio=(22/7)*radio
    
    print('el area del circulo es ',radio)
  else:
    print('El punto no tiene area')







