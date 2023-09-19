import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(2)

# Move the turtle to the starting position
t.penup()
t.goto(-600, 100)
t.pendown()

# Define the sentence to be written
sentence = "Hello, Vinay How are you and where you go. im with you "

# Write each letter of the sentence one at a time
for char in sentence:
    t.write(char, font=("Arial", 16, "normal"))
    t.forward(20)

# Hide the turtle when finished
t.hideturtle()

# Keep the window open until it is closed
turtle.done()
