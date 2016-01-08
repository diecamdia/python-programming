#manejo de ficheros
nombreFichero = 'Invitados.txt'
WRITE = 'w' #destruye el fichero.
APPEND = 'a'
READ = 'r'
READWRITE = 'w+'

fichero = open(nombreFichero, mode = WRITE)
fichero.write('Esta es un texto\n')
fichero.write('Esto es otro texto')
fichero.close()

print('Fichero creado')

