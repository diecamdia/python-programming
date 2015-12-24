#declaración de lista
invitados = ['Manolo','Carmen','Pedro', 'Jorge']

#acceso a elementos
print (invitados[0])

#borrar elementos
invitados.remove('Carmen')
del invitados[0]
print (invitados[0])

#agregar elementos
invitados.append('Maria')

#acceder al último elemento
print('El ultimo invitado es', invitados[-1])

#encontrar la posición de un valor
print (invitados.index('Pedro'))
#la siguiente instrucción da error porque no existe en la lista
#print (invitados.index('Manolo'))

longitud = len(invitados)
print('La lista tiene %d elementos' % longitud)
for indice in range(longitud):
    print(invitados[indice])

print('Lista de invitados')
for invitado in invitados:
    print(invitado)
