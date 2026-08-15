from PPlay.window import*
from PPlay.sprite import*

import random

#Tamanho da tela
res = 70
width = 16 * res
height = 9 * res

#Gerando a janela
window = Window(width, height)
window.set_title("João Vitor Gusmão de Souza")
background_color = [0, 120, 255]
window.set_background_color(background_color)

keyboard = window.get_keyboard()

#Variáveis globais
speed = 500
game_state = 0
ps, ias = 0, 0
tempo, counter = 0, 0
tempo_max = random.randint(25, 45)
spawned = False

#Bola
ball = Sprite("ball.png")
ball.set_position((window.width - ball.width)/2, (window.height - ball.height)/2)
xspeed = speed
yspeed = speed

#Player
player = Sprite("bar.png")
player.set_position(player.width * 0.5, (window.height - player.height)/2)
pspeed = speed - 50

#Inimigo
bar = Sprite("bar.png")
bar.set_position(window.width - bar.width * 1.5, (window.height - player.height)/2)

middle_bar = Sprite("bar.png")
middle_bar.set_position((window.width - middle_bar.width)/2, random.randint(0, window.height - middle_bar.height))


def player_movement():
    if keyboard.key_pressed("up") and player.y >= 0:
        player.move_y(-pspeed * window.delta_time())
    elif keyboard.key_pressed("down") and player.y <= window.height - player.height:
        player.move_y(pspeed * window.delta_time())

def bar_movement():
    if ball.x >= window.width/2:
        if bar.y > ball.y and bar.y >= 0:
            bar.move_y(-pspeed * window.delta_time())
        elif bar.y < ball.y and bar.y <= window.height - player.height:
            bar.move_y(pspeed * window.delta_time())

def middle_bar_spawn():
    global spawned, counter, tempo, tempo_max
    if counter >= 3:
        spawned = True
        tempo += window.delta_time()

    if tempo >= float(tempo_max)/10:
        middle_bar.set_position((window.width - middle_bar.width)/2, random.randint(0, window.height - middle_bar.height))
        tempo_max = random.randint(25, 45)
        spawned = False
        counter, tempo = 0, 0

def ball_wall_collision():
    global counter, yspeed
    if ball.y + ball.height >= window.height:
        ball.set_position(ball.x, window.height - ball.height)
        counter += 1
        yspeed *= -1

    elif ball.y <= 0:
        ball.set_position(ball.x, 0)
        counter += 1
        yspeed *= -1

def ball_bar_collision():
    global xspeed
    if ball.collided(player):
        ball.set_position(player.x + player.width, ball.y)
        xspeed *= -1
    
    elif ball.collided(bar):
        ball.set_position(bar.x - ball.width, ball.y)
        xspeed *= -1

    elif ball.collided(middle_bar):
        if spawned:
            if xspeed < 0:
                ball.set_position(middle_bar.x + middle_bar.width, ball.y)
                xspeed -= 50
            elif xspeed > 0:
                ball.set_position(middle_bar.x - ball.width, ball.y)
                xspeed += 50
            xspeed *= -1

def score():
    global game_state, ps, ias
    if ball.x + ball.width >= window.width or ball.x <= 0:
        game_state = 0
        if xspeed > 0:
            ps += 1
        elif xspeed < 0:
            ias += 1

def ball_movement():
    ball.move_x(xspeed * window.delta_time())
    ball.move_y(yspeed * window.delta_time())

    ball_wall_collision()

    ball_bar_collision()

    score()    

def draw():
    player.draw()
    ball.draw()
    bar.draw()
    if spawned:
        middle_bar.draw()

    #Imprimir os placares na tela
    window.draw_text(f"{ps}", 0, 0, 48)
    window.draw_text(f"{ias}", window.width - 30, 0, 48)

while True:
    if keyboard.key_pressed("esc") or ps == 10 or ias == 10:
        window.close()

    if keyboard.key_pressed("space"):
        game_state = 1
    
    window.set_background_color(background_color)

    if game_state == 1:
        ball_movement()
        player_movement()
        bar_movement()
        middle_bar_spawn()

    elif game_state == 0:
        player.set_position(player.width * 0.5, (window.height - player.height) / 2)
        ball.set_position((window.width - ball.width) / 2, (window.height - ball.height) / 2)
        bar.set_position(window.width - bar.width * 1.5, (window.height - player.height) / 2)
        xspeed = 500

    draw()  
    window.update()