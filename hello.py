import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(2)

# Move the turtle to the starting position
t.penup()
t.goto(-100, 100)
t.pendown()

# Write "Hello, World!" using the turtle
for char in "Hello, Darling":
    t.write(char, font=("Arial", 16, "normal"))
    t.forward(20)

# Hide the turtle when finished
t.hideturtle()

# Keep the window open until it is closed
turtle.done()
