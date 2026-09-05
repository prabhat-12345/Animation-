import streamlit as st
from streamlit_turtle import Turtle # Standard turtle ki jagah ise import karein
import colorsys
import math

st.set_page_config(page_title="Vortex Mandala Art", page_icon="🌀", layout="centered")
st.title("🌀 Vortex Mandala Art on Streamlit Cloud")

# Streamlit-Turtle ka setup
t = Turtle(width=600, height=600)
t.speed(0)
t.hideturtle()

iterations = 360
cycles = 6

# Aapka original logic bina kisi badlav ke chalega
for i in range(iterations):
    hue = i / iterations
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(color)
    
    t.pensize(abs(math.sin(i * 0.05)) * 2 + 1)
    
    angle = i * (360 / cycles) + (i * 0.5)
    distance = math.sqrt(i) * 12 # Screen ke hisab se scale kiya
    
    t.penup()
    t.goto(0, 0)
    t.setheading(angle)
    t.forward(distance)
    t.pendown()
    
    t.begin_fill()
    fill_color = colorsys.hsv_to_rgb((hue + 0.5) % 1.0, 0.8, 0.3)
    t.fillcolor(fill_color)
    
    for _ in range(5):
        t.forward(i * 0.12)
        t.right(144)
        t.forward(i * 0.12)
        t.left(72)
    t.end_fill()

# Canvas ko Streamlit widget mein convert karke show karna
t.window.mainloop()
