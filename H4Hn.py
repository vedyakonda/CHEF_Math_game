import pygame, sys
import random
import time
import test
from pygame.locals import *

pygame.init()
pygame.font.init()
window_width = 700
window_height = 400
screen = pygame.display.set_mode((650, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms",80)
font1 = pygame.font.SysFont("comicsansms",45)
# textImage = font.render('Hello ',True,(255,255,255))
textinput = test.TextInput()  # used for text input from test.py

difficulty = 1
question_number = 0
correct = False
score = 0
light_blue = (147,237,237)
light_pink = (245,164,191)
light_green = (196,245,164)
light_purple = (223,181,255)
light_red = (252,189,189)
color_num = 0;


def get_n(difficulty):
    # create a question here
    var1 = random.randint(difficulty*10 - 10, difficulty * 10)
    var2 = random.randint(difficulty*10 - 10, difficulty * 10)

    return (var1, var2, var1+var2)


n1, n2, n3 = get_n(difficulty)
score = 0
score_text = font1.render("Score: "+str(score),True,(255,255,255))
message_time = 0
message = 'hi';
color_ = light_blue

while True:
    screen.fill(color_)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    # screen.blit(textImage,(100,100))
    user_input = textinput.get_text()

    answer = font.render((str(n1) + " + " + str(n2) + " = ?"), True, (255, 255, 255))
    screen.blit(answer, (160, 215))
    pygame.display.flip()
    screen.blit(score_text, (20, 20))
    pygame.display.flip()

    # addition

    # # sublevel #1
    # # Ex: 0+6, 5+3, 4+2, etc.
    #
    # a = str(X) + "+" + str(Y) + "=?"
    # question = font.render(a, True, (225, 225, 255))
    # screen.blit(question, (200, 350))
    # pygame.display.flip()

    textinput.update(events)
    screen.blit(textinput.get_surface(), (175, 300))

    message_time = message_time - 1
    if message_time > 0:
        screen.blit(b, (160, 400))
        # show the message

    # check if pressed the enter key
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == K_RETURN:
                if user_input == str(n3):
                    # User got it correct
                    score += 1
                    score_text = font1.render("Score: " + str(score), True, (255, 255, 255))
                    b = font.render("Correct!!!", True, (255, 255, 255))
                    difficulty = difficulty + 1
                    color_num = random.randint(0,4)
                    if(color_num == 0):
                        color_ = light_blue
                        # screen.fill(light_blue)
                    elif(color_num == 1):
                        color_ = light_pink
                        # screen.fill(light_pink)
                    elif(color_num == 2):
                        color_ = light_purple
                    elif(color_num == 3):
                        color_ = light_red
                    else:
                        color_ = light_green
                        # screen.fill(light_green)

                else:
                    # User got it incorrect
                    b = font1.render("Oops, try again! " +str(n3), True, (255, 255, 255))

                # User submitted a answer
                message_time = 20
                pygame.display.update()
                n1, n2, n3 = get_n(difficulty)
                textinput.clear_text()

    pygame.display.update()
    clock.tick(60)