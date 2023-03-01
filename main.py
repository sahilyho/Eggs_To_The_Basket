from turtle import Turtle, Screen
from random import randint

from scoreboard import Scoreboard
from pixel import Pixel
from eggs import Eggs

import tkinter.font as font
from tkinter import *

import time

# ------------------------CONSTANTS-----------------------
RED_EGG = "red"
YELLOW_EGG = "yellow"
MAIN_FONT = "Courier New"
RESTART = "Do you want to restart ? (y/n)"
background_img = "bg.gif"
basket_img = "basket.gif"

# ------------------------GAME PIECES-----------------------
screen = Screen()
screen.setup(500, 640)
screen.addshape(background_img)
screen.addshape(basket_img)
screen.bgpic(background_img)
rules = Turtle()
egg_image = PhotoImage(file="fried-egg.png")
canvas = screen.getcanvas()


# ------------------------GAME LOGIC-----------------------

# ------------------------ON-GAME--------------------------


def you_win():
    winner = Turtle()
    winner.hideturtle()
    winner.color("Red")
    winner.penup()
    winner.setposition(0, 100)
    winner.write("Winner, Winner.\n"
                 "Chicken Dinner!",
                 False,
                 "center",
                 font=(MAIN_FONT, 25, "bold"))


def game_over():
    """Pops up when the game is over. is_game_on = False"""
    over = Turtle()
    over.color("white")
    over.penup()
    over.setposition(0, 100)
    over.write("Thee hath lost!",
               False,
               "center",
               font=(MAIN_FONT, 30, "bold"))


def rules_func():
    rules.color("black")
    rules.penup()
    rules.hideturtle()
    rules.goto(-0, 80)
    rules.write("Thee wants to be a chicken catcher?\n\n"
                "Let us see if thee can catch some eggs.\n\n"
                "Her Majesty fancies the red ones.\n\n"
                "Thee must get them before the wild beasts.\n\n"
                "Although their touch has the power\nto change colors.\n\n"
                "Oh, and watch for the spoiled eggs.\n\n"
                "Thee hath 60 SECONDS to collect 20 eggs!",
                False,
                "center",
                font=("Courier New", 12, "normal"))


rules_func()


def start_game():
    screen.tracer(0)
    starting_egg = Eggs()
    basket = Turtle()
    pixel = Pixel()
    basket.shape(basket_img)
    scoreboard = Scoreboard()
    rules.clear()
    start_button.destroy()

    eggs_list = [starting_egg]
    is_game_on = True

    # timer
    timer_text = Turtle()
    start = time.time()
    timer_text.hideturtle()
    timer_text.color("white")
    timer_text.goto(-220, 250)

    while is_game_on:
        time.sleep(0.01)
        screen.update()

        # timer starts
        timer_text.clear()
        timer_number = int(time.time() - start)
        timer_text.write(timer_number, font=(MAIN_FONT, 30, "bold"))
        try:
            # pixel or square moves around the screen and bounces off wall
            pixel.move()

            if pixel.xcor() > 245 or pixel.xcor() < -245:
                pixel.x_bounce()

            if pixel.ycor() > 315 or pixel.ycor() < -315:
                pixel.y_bounce()

            # each egg changes color when colliding with the square
            for egg in eggs_list:
                egg.change_on_collision(pixel)

                if timer_number < 60 and scoreboard.score >= 20:
                    you_win()
                    restart = screen.textinput(title="Restart", prompt=RESTART)
                    if restart == "y":
                        screen.clearscreen()
                        start_game()
                    else:
                        is_game_on = False

                elif not timer_number == 60:
                    # egg can only enter the basket if red.
                    if "red" in egg.new_color:

                        if egg.distance(basket) < 20:
                            scoreboard.inc_score()
                            egg.hideturtle()

                            for new_egg in range(randint(2, 5)):
                                new_egg = Eggs()
                                eggs_list.append(new_egg)
                            egg.new_color.remove("red")
                            egg.new_color.append("white")

                    elif egg.distance(pixel) < 5 and "white" in egg.new_color:

                        if scoreboard.score > 0:
                            scoreboard.dec_score()

                        elif scoreboard.score == 0:
                            game_over()
                            restart = screen.textinput(title="Restart", prompt=RESTART)
                            if restart == "y":
                                screen.clearscreen()
                                start_game()
                            else:
                                is_game_on = False
                else:
                    game_over()
                    restart = screen.textinput(title="Restart", prompt=RESTART)
                    if restart == "y":
                        screen.clearscreen()
                        start_game()
                    else:
                        is_game_on = False
        except ConnectionRefusedError:
            print("Sorry. No connection")


# ------------------------PRE-GAME-------------------------

start_button_font = font.Font(family=MAIN_FONT)
start_button = Button(canvas.master,
                      text="Start",
                      height=130, width=130,
                      command=start_game,
                      font=start_button_font,
                      image=egg_image, highlightthickness=0)
start_button["bg"] = "#4eab51"
start_button["border"] = "0"

start_button.pack()
start_button.place(x=180, y=300)

screen.listen()
screen.mainloop()
