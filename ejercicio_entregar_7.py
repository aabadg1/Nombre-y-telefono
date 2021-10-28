datos= []
while True:
    nombre= input('Nombre:')
    if nombre == 'fin':
        break
    apellido1 = input('primer apellido:')
    apellido2= input('segundo apellido:')
    telefon= input('telefono movil:')
    #CREAMOS UN DICCIONARIO
    linea= {}
    linea['Nombre'] = nombre
    linea['1er apellido'] = apellido1
    linea['2do apellido'] = apellido2
    #AÑADIMOS DICCIONARIO A LA LISTA
    datos.append(linea)

print('Nombre completo y Número:\n',datos)