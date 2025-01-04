import turtle
import random


score=0
scr=turtle.Screen()
scr.title("space fighter")
scr.bgcolor("black")
scr.setup(800,800)
scr.tracer(0)
 


player_vertices=((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18,5),(15,0))
scr.register_shape("player",player_vertices)

asteriod_vertices=((0,10),(5,7),(3,3),(10,0),(7,4),(8,-6),(0,-10),(-5,-5),(-7,-7),(-10,0),(-5,4),(-1,8))
scr.register_shape("asteriod",asteriod_vertices)

player=turtle.Turtle()
player.color("white")
player.shape("player")
asteriods=[]
for i in range(5):
    asteriod=turtle.Turtle()
    asteriod.color("brown")
    heading=random.randint(0,360)
    distance=random.randint(400,600)
    asteriod.penup()
    asteriod.setheading(heading)
    asteriod.fd(distance)
    
    asteriod.shape("asteriod")
    asteriod.speed=0.01
    asteriods.append(asteriod)
missiles=[]
for i in range(3):
    
    missile=turtle.Turtle()
    missile.color("red")
    missile.penup()
    missile.goto(50,50)
     
    missile.shape("triangle")
    missiles.append(missile)
    missile.state="ready"
    missile.speed=4
    missile.hideturtle()

pen=turtle.Turtle()
pen.color("yellow")
pen.shape("turtle")
pen.penup()
pen.goto(0,350)
 
pen.write("score : {}".format(score),align="center",font=("arial",22,"bold"))
pen.hideturtle()


def player_left():
    player.left(10)

def player_right():
    player.right(10)

def fire_missile():
    for missile in missiles:
        if missile.state=="ready":
            missile.goto(0,0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state="fire"
            break
scr.listen()
scr.onkeypress(player_left,"Left")
scr.onkeypress(player_right,"Right")
scr.onkeypress(fire_missile,"space")

while True:
    scr.update()
    for missile in missiles:
        if missile.state=="fire":
            missile.fd(missile.speed)


        if  missile.xcor()>400 or missile.xcor()<-400 or missile.ycor()>400 or missile.ycor()<-400:
            missile.hideturtle()
            missile.state="ready"

        for asteriod in asteriods:
            asteriod.fd(-asteriod.speed)


            for missile in missiles:
                if asteriod.distance(missile)<20:
                    missile.hideturtle()
                    missile.goto(1000,1000)
                    heading=random.randint(0,360)
                    distance=random.randint(400,600)
                    asteriod.setheading(heading)
                    asteriod.fd(distance)

                    score+=10
                    pen.clear()
                    pen.write("score : {}".format(score),align="center",font=("arial",22,"bold"))

                if asteriod.distance(player)<20:
                    if asteriod.ycor()<-265:
                         print("game over")
                         exit()
 

                    




















                    












