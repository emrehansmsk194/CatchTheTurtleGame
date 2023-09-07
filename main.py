import turtle
import time
from random import randint

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch the Turtle Game")
drawing_board.setup(width=800, height=600)


score_Text = turtle.Turtle()
timer_Text = turtle.Turtle()
turtle_instance2 = turtle.Turtle()

#turtle codes
turtle_instance2.shape("turtle")
turtle_instance2.color("green")
turtle_instance2.penup()


game_over = False
time_variable = 20
count = 0
starting_time = time.time()
#score_Text codes
score_Text.pencolor("blue")
score_Text.hideturtle()
score_Text.penup()
score_Text.left(90)
score_Text.forward(250)
score_Text.write(f"Score: {count}", align="center",font=("Arial",24,"normal"))

#timer_Text codes
timer_Text.pencolor("red")
timer_Text.hideturtle()
timer_Text.penup()
timer_Text.left(90)
timer_Text.forward(200)
def turtle_movement():
    if not game_over:
        turtle_instance2.goto(randint(-350,350),randint(-200,200))
        drawing_board.ontimer(turtle_movement,500)





def time_counter():
    global game_over,time_variable
    for i in range(time_variable,0, -1):
        timer_Text.clear()
        timer_Text.write(f"Time: {i}",align="center",font=("Arial",24,"normal"))
        time.sleep(0.5)
    timer_Text.clear()
    timer_Text.write("Game Over!",align="center",font=("Arial",24,"normal"))
    game_over = True

def update_counter(x,y):
    global count
    if not game_over:
        count += 1
        score_Text.clear()
        score_Text.write(f"Score: {count}", align="center",font=("Arial",24,"normal"))


turtle_instance2.onclick(update_counter)
turtle_movement()
time_counter()





turtle.mainloop()






