import pgzrun, random as r

#Global / game wide variables
WIDTH = 800
HEIGHT = 800
score = 0
timer = 5
lives = 3

snake = Actor("snake_picture")
snake.x = 400
snake.y = 400

mouse = Actor("mouse_picture")

ghost = Actor("ghost_picture")
ghost.x = 0
ghost.y= 0 

def reset_mouse():
    mouse.x = r.randint(50,750)
    mouse.y = r.randint(50,750)
reset_mouse()

def update():
    global score, mouse, timer, lives, ghost
    timer -= 1/60
    if timer <0:
        reset_mouse()
        score -= 1
        if score < 5:
            timer = 5
        elif score >= 5:
            timer = 4
        elif score >= 10:
            timer = 3
        elif score >= 15:
            timer = 2
        elif score >= 20:
            timer = 1
    if keyboard.right and snake.x < 790:
        snake.x += 10
    if keyboard.left and snake.x > 0:
        snake.x -= 10
    if keyboard.up and snake.y > 0:
        snake.y -= 10
    if keyboard.down and snake.y < 790:
        snake.y += 10
    #Code on how to move enermy found from github
    if ghost.x < snake.x:
        ghost.x = ghost.x + 2
    if ghost.x > snake.x:
        ghost.x = ghost.x - 2
    if ghost.y < snake.y:
        ghost.y = ghost.y + 2
    if ghost.y > snake.y:
        ghost.y = ghost.y - 2
    if ghost.colliderect(snake):
        lives -= 1
    if mouse.colliderect(snake):
        score += 1
        reset_mouse()

def draw():
    global lives
    if lives > 0:
        draw_game()
    if lives == 0:
        game_over()

def draw_game():
    screen.fill((0,0,0))
    screen.draw.text("Score:" + str(score), 
                     (720, 10))
    snake.draw()
    mouse.draw()
    ghost.draw()

def game_over():
    screen.fill((0,0,0))
    screen.draw.text("Game Over", (400,300))

pgzrun.go()
