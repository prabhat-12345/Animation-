import turtle
import colorsys
import math

def draw_vortex():
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Vortex Mandala")
    screen.setup(width=800, height=800)
    
    # Turtle configuration
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(10, 0)  # Speed ko super-fast karne ke liye
    
    iterations = 360
    cycles = 6
    
    for i in range(iterations):
        # Rainbow colors calculate karne ke liye
        hue = i / iterations
        color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        t.pencolor(color)
        
        # Pen ki dynamic thickness (motai) badalne ke liye
        t.pensize(abs(math.sin(i * 0.05)) * 2 + 1)
        
        # Spiral angles aur distance math calculation
        angle = i * (360 / cycles) + (i * 0.5)
        distance = math.sqrt(i) * 16
        
        t.penup()
        t.goto(0, 0)
        t.setheading(angle)
        t.forward(distance)
        t.pendown()
        
        # Har ek patti (petal) ke andar color fill karne ke liye
        t.begin_fill()
        fill_color = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 0.8, 0.3)
        t.fillcolor(fill_color)
        
        # Star/Petal shape draw karne ka loop
        for _ in range(5):
            t.forward(i * 0.15)
            t.right(144)
            t.forward(i * 0.15)
            t.left(72)
        t.end_fill()
        
    # Window ko open rakhne ke liye
    turtle.done()

# Code ko chalane ke liye function call
if __name__ == "__main__":
    draw_vortex()
    
