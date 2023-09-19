import turtle

# Create a turtle object
t = turtle.Turtle()

# Move the turtle to a specific position
t.penup()
t.goto(-300, 100)
t.pendown()

# Get the current position of the turtle's pen
position = t.pos()
print("The current position of the turtle's pen is:", position)

# Keep the window open until it is closed
turtle.done()
