from turtle import Turtle,onscreenclick, onkey, listen, Screen
leo = Turtle ()
tela = Screen()
leo.speed(0)
resultado = 0
numero = 0

def trocar ():
    global resultado
    global numero
    numero = numero + 1
    resultado = numero % 2

def jogar(x, y): 
    leo.penup()
    leo.goto(x, y)
    if resultado == 0:
        circulo()

def circulo():
    leo.color('green')
    r = 50
    leo.pendown()
    leo.circle(r)

def x2():
    leo.color('purple')
    leo.pendown()
    leo.right(45)
    for _ in range(4):
        leo.forward(70)
        leo.forward(-70)
        leo.right(90)
    leo.left(45)

tela.onscreenclick(jogar)

listen()
tela.mainloop()