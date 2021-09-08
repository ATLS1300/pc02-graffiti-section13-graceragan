#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Grace Ragan
May 29, 2020
'''

import turtle 



turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("White")
panel.bgpic(image)

s = turtle.getscreen()
t = turtle.Turtle()

t.hideturtle()

t.penup()
t.speed(10)
t.goto(130,-130)
t.pendown()

t.pensize(5)
t.shape("circle")

t.fillcolor("DarkOliveGreen1")
t.pencolor("green")


t.begin_fill()
t.fd(175)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(175)
t.lt(90)
t.fd(100)
t.end_fill()

t.penup()
t.goto(180,-80)
t.pendown()
t.pencolor("Green")
t.fillcolor("Green")
t.speed(10)
t.circle(40)

t.penup()
t.goto(218,-55)
t.pendown()
t.speed(10)
t.pencolor("green")
t.fillcolor("green")
t.goto(218,-105)



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
