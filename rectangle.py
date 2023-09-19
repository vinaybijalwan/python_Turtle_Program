import turtle

# Create a turtle object
t = turtle.Turtle()

t.penup()
t.goto(-200, 100)
t.pendown()

t.forward(300)
t.right(90)
t.forward(150)
t.right(90)
t.forward(300)
t.right(90)
t.forward(150)

# Keep the window open until it is closed
turtle.done()