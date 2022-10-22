
import turtle as t
import random
import colorgram

#configuration of environment/ We name our turtle object as Tim(the turtle)

tim = t.Turtle()
t.colormode(255)
t.screensize(2000,2000)
t.bgcolor(0,0,0)
tim.speed("fastest")


#Setting up color extractor from image provided 'image.png'

rgb_colors = []
colors = colorgram.extract('image.png', 30)  #the int denotes number of colors extracted from the image

for color in colors:
    rgb_colors.append(color.rgb)

#example output : rgb_colors = [Rgb(r=239, g=193, b=222), Rgb(r=148, g=124, b=172), Rgb(r=210, g=144, b=187), Rgb(r=255, g=223, b=211)]




#Makes a touple list from the colors extracted in 'rgb_colors'

palette = []

def palette_maker():

    for i in range(len(colors)):
        first_color = colors[i]
        rgb = first_color.rgb
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        touple =(red,green,blue)
        palette.append(touple)

    return palette

palette_to_use = palette_maker()

#example output : palette_to_use = [(239, 193, 222), (148, 124, 172), (210, 144, 187), (255, 223, 211)]


#Drawing the dotted artwork


#Part1: Generate the horizontal dots for the artwork

def dot_lines():
    for x in range(0,30) :
        random_color = random.choice(palette_to_use)
        tim.penup()
        tim.dot(10,random_color)
        tim.forward(20)

#Part2: Generate the vertical dots for the artwork by looping the horizontals

def vertical_dots():
    yaxis = -200
    tim.penup()
    tim.goto(-300, yaxis)
    for y in range(0,30):
        dot_lines()
        yaxis += 20
        tim.goto(-300, yaxis)

#Call the function to generate a unique artwork for every run

vertical_dots()
t.exitonclick()









