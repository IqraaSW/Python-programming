from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["red", "orange", "green","yellow", "blue"]
turtle_list = []
step = 100
for i in range(5):
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.goto(x=-230, y=step)
  step = step - 40
  turtle_list.append(new_turtle)

player = Turtle(shape="turtle")
player.color("pink")
player.penup()
player.goto(x=-230, y=-100)

# Defining a function
def go_forward():
  rand_distance = random.randint(0, 10)
  player.forward(rand_distance)
 
# Get keyboard events
screen.listen()
screen.onkey(go_forward, "Right")

while is_race_on:
  for turtle in turtle_list:
    if turtle.xcor() > 230  or player.xcor() > 230:
      if turtle.xcor() > 230:
        winning_color = turtle.pencolor()
      else:
        winning_color = player.pencolor()
      is_race_on = False
      
    rand_distance = random.randint(0, 10)
    turtle.forward(rand_distance)

if winning_color == "pink":
  player.hideturtle()
  player.goto(0,0)
  player.color("black")
  player.write("You've won!",font=("Arial",24,"bold"))
else:
  turtle.hideturtle()
  turtle.goto(-230,0)
  turtle.color("black")
  turtle.write(f"You've lost! {winning_color} turtle wins!",font=("Arial",24,"bold"))

screen.exitonclick()