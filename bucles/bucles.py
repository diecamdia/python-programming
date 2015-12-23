import turtle
#for steps in range(4):
#    turtle.forward(100)
#    turtle.right(90)

#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)
#turtle.right(90)
#turtle.forward(100)


lados = int(input('Cuantos lados desea? '))
#for steps in range(lados):
#    turtle.forward(16)
#    turtle.right(360/lados)
#    for moresteps in range(lados):
#        turtle.forward(25)
#        turtle.right(360/lados)


#contador = 0
while contador < lados:
     turtle.forward(100)
     turtle.left(360/lados)
     contador += 1
