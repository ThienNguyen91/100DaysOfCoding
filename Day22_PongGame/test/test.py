from turtle import Turtle, Screen

# Create the turtle object
testing = Turtle()

# Function to move the turtle based on mouse movement
def move_turtle(event):
    y =screen.window_height() // 2 - event.y  # Adjust coordinates
    testing.sety(y)

# Create the screen object
screen = Screen()

# Bind the mouse motion to the move_turtle function
screen.cv.bind("<Motion>", move_turtle)

# Keeps the window open
screen.mainloop()
