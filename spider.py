import turtle as t


# define turtle speed
t.speed(2)


# radical thread
for i in range(6):
   t.forward(150)
   t.backward(150)
   t.right(60)

   
# spiral thread length
side = 50
t.fillcolor("Orange")


#Create a web for Spiral web using Python Turtle


# building web
t.begin_fill()

for i in range(15):
   t.penup()
   t.goto(0, 0)
   t.pendown()
   t.setheading(0)
   t.forward(side)
   t.right(120)

   for j in range(6):
      t.forward(side-2)
      t.right(60)
   side = side - 10
