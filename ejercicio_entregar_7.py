datos= []
while True:
    nombre= input('Nombre:')
    if nombre == 'fin':
        break
    apellido1 = input('Primer apellido:')
    apellido2= input('Segundo apellido:')
    telefono= input('Telefono movil:')
    #CREAMOS UN DICCIONARIO
    linea= {}
    linea['Nombre'] = nombre
    linea['1er apellido'] = apellido1
    linea['2do apellido'] = apellido2
    linea['Teléfono'] = telefono
    #AÑADIMOS DICCIONARIO A LA LISTA
    datos.append(linea)

print('Nombre completo y Número:\n',datos)