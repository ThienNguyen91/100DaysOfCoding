from turtle import Screen, Turtle, colormode

colormode(255)  # Ensure the color mode allows for RGB values in the 0-255 range

def change_color(turtle_instance, rgb):
    print(rgb)
    turtle_instance.pencolor(rgb)  # Set the pencolor using the RGB tuple

color_list = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
    (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
    (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
    (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
    (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
]

Tom = Turtle()  # Create the turtle instance
Tom.hideturtle()
Tom.speed("fastest")  # Speed up the drawing

color_count = 0
Tom.setheading(255)
Tom.penup()
Tom.forward(300)
Tom.setheading(0)
Tom.pendown()

# Get the starting x and y coordinates
y = Tom.pos()[1]
x_start = Tom.pos()[0]

for row_index in range(10):  # Loop through 10 rows
    for col_index in range(10):  # Loop through 10 columns
        change_color(Tom, color_list[color_count % len(color_list)])  # Pass the turtle instance 'Tom'
        Tom.dot(20)  # Draw a dot of size 20
        Tom.penup()  # Lift the pen to move without drawing
        Tom.forward(50)  # Move 50 units to the right
        color_count += 1  # Increment the color count
    Tom.penup()
    y += 50  # Move down 50 units for the next row
    Tom.goto(x_start, y)  # Reset the x position to start and move to the next row
    Tom.pendown()

screen = Screen()
screen.exitonclick()
