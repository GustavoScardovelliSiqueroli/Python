
import turtle as t

t.pensize(3)
t.penup()
t.goto(0, 0)
t.pendown()

# Desenha o corpo
t.fillcolor('yellow')
t.begin_fill()
t.circle(50)
t.end_fill()

# Desenha os olhos
t.penup()
t.goto(-20, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(5)
t.end_fill()

t.penup()
t.goto(20, 60)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(5)
t.end_fill()

# Desenha a boca
t.penup()
t.goto(-20, 40)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(20, 180)
t.end_fill()

# Desenha a orelha esquerda
t.penup()
t.goto(-50, 50)
t.pendown()
t.fillcolor('pink')
t.begin_fill()
t.circle(20, 180)
t.end_fill()

# Desenha a orelha direita
t.penup()
t.goto(50, 50)
t.pendown()
t.fillcolor('pink')
t.begin_fill()
t.circle(-20, 180)
t.end_fill()

# Desenha as barbelas
t.penup()
t.goto(-15, 25)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(15, 25)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()

t.penup()
t.goto(0, 0)
t.pendown()

t.done()