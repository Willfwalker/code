import turtle
import math
import time
import datetime
import pygame
from pygame.locals import *
from pygame import mixer

#Envirment
Wn = turtle.Screen()
Wn.title("Pong with lil Shuster")
Wn.bgcolor("black")
Wn.setup(width=800, height=600)
Wn.tracer(0)
#Score

Player1_score = 0
Player2_score = 0

# Platform A
Platform_a = turtle.Turtle()
Platform_a.speed(0)
Platform_a.shape("square")
Platform_a.color("white")
Platform_a.shapesize(stretch_wid=5, stretch_len=1)
Platform_a.penup()
Platform_a.goto(-350, 0)


# Platform B

Platform_b = turtle.Turtle()
Platform_b.speed(0)
Platform_b.shape("square")
Platform_b.color("white")
Platform_b.shapesize(stretch_wid=5, stretch_len=1)
Platform_b.penup()
Platform_b.goto(350, 0)

#Scorceboard
scoreboard_left_1st = turtle.Turtle()
scoreboard_left_1st.speed(0)
scoreboard_left_1st.color("black")
scoreboard_left_1st.shape("square")
scoreboard_left_1st.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_left_1st.penup()
scoreboard_left_1st.goto(-250,250)

scoreboard_left_2nd = turtle.Turtle()
scoreboard_left_2nd.speed(0)
scoreboard_left_2nd.color("black")
scoreboard_left_2nd.shape("square")
scoreboard_left_2nd.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_left_2nd.penup()
scoreboard_left_2nd.goto(-215,250)

scoreboard_left_3rd = turtle.Turtle()
scoreboard_left_3rd.speed(0)
scoreboard_left_3rd.color("black")
scoreboard_left_3rd.shape("square")
scoreboard_left_3rd.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_left_3rd.penup()
scoreboard_left_3rd.goto(-180,250)

scoreboard_right_1st = turtle.Turtle()
scoreboard_right_1st.speed(0)
scoreboard_right_1st.color("black")
scoreboard_right_1st.shape("square")
scoreboard_right_1st.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_right_1st.penup()
scoreboard_right_1st.goto(250,250)

scoreboard_right_2nd = turtle.Turtle()
scoreboard_right_2nd.speed(0)
scoreboard_right_2nd.color("black")
scoreboard_right_2nd.shape("square")
scoreboard_right_2nd.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_right_2nd.penup()
scoreboard_right_2nd.goto(215,250)

scoreboard_right_3rd = turtle.Turtle()
scoreboard_right_3rd.speed(0)
scoreboard_right_3rd.color("black")
scoreboard_right_3rd.shape("square")
scoreboard_right_3rd.shapesize(stretch_len=1, stretch_wid=3)
scoreboard_right_3rd.penup()
scoreboard_right_3rd.goto(180,250)


#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("pink")
ball.penup()
ball.goto(0, 0)

#Function
#Left going up
def platform_a_up():
    y = Platform_a.ycor()
    y += 30 
    Platform_a.sety(y)

Wn.listen()
Wn.onkeypress(platform_a_up,"w")

#left going down
def platform_a_down():
    y = Platform_a.ycor()
    y -= 30
    Platform_a.sety(y)

Wn.listen()
Wn.onkeypress(platform_a_down,"s")

#Right going up

def platform_b_up():
    y = Platform_b.ycor()
    y += 30 
    Platform_b.sety(y)

Wn.listen()
Wn.onkeypress(platform_b_up,"Up")

#Right going down
def platform_b_down():
    y = Platform_b.ycor()
    y -= 30 
    Platform_b.sety(y)

Wn.listen()
Wn.onkeypress(platform_b_down,"Down")

#Moving the ball
ball.dx = .25
ball.dy = .25


#Game loop
while True:
    #End the Game
    #if Player1_score == 3 or Player2_score == 3:
       #turtle.clear()
     #turtle.done()
   
    Wn.update() 
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Borders
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #Ball Reset and Scoring for Player 1
    if ball.xcor() > 395:
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx/abs (ball.dx) *.25
        Player1_score += 1
        if Player1_score == 1:
            scoreboard_left_1st.color("white")
            Wn.update()
            time.sleep(2)
            
        if Player1_score == 2:
            scoreboard_left_2nd.color("white")
            Wn.update()
            time.sleep(2)

        if Player1_score == 3:
            scoreboard_left_3rd.color("white")
            Wn.update()
            time.sleep(2)

    #Ball Reset and Scoring for Player 2   
    if ball.xcor() < -395:  
        ball.goto(0, 0)
        ball.dx = -1 * ball.dx/abs (ball.dx) *.25
        Player2_score += 1
        if Player2_score == 1:
            scoreboard_right_1st.color("white")
            Wn.update()
            time.sleep(2)

        if Player2_score == 2:
            scoreboard_right_2nd.color("white")
            Wn.update()
            time.sleep(2)

        if Player2_score == 3:
            scoreboard_right_3rd.color("white")
            Wn.update()
            time.sleep(2)
    
  
#Platform's Hardness

    if ball.xcor() < -340 and (ball.ycor() < Platform_a.ycor() + 40 and ball.ycor() > Platform_a.ycor() -40):
        ball.dx *= -1.25
    
     
    if ball.xcor() > 340 and (ball.ycor() < Platform_b.ycor() + 40 and ball.ycor() > Platform_b.ycor() -40):
        ball.dx *= -1.25
      
        





#Bug fixes
#Background music?
