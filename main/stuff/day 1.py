from turtle import * 

#we wanna paint a house.
speed(30)
width(7)
#first we need to draw a square
color("grey")
begin_fill()
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill() 

#now the door
forward(70)
color("brown")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)  #200-140
right(90)
forward(120)
end_fill()

 #the roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)  #90+60 degree cuz we want an equilateral triangle(tolgv)
forward(200)
left(120)
forward(200)
end_fill()

#the windows
penup()
goto(20, 160)
pendown()
begin_fill()
color("yellow")
left(30)
forward(70)
left(90)
forward(30)
left(90)
forward(70)
left(90)
forward(30)
end_fill()

penup()
goto(180, 160)
pendown()
begin_fill()
color("yellow")
forward(30)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(70)
end_fill()

exitonclick()
 

