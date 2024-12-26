# Example file showing a basic pygame "game loop"
import pygame
import random
screen_width, screen_height = 1000, 500

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
x, y = 100, 100
score = 0
food_coordinates = (random.randint(50, 950),random.randint(50, 450)) # set

def eat_food():
    global x, y, food_coordinates, score
    
    if x+20 > food_coordinates[0] > x-20 and y+20 > food_coordinates[1] > y-20:
        food_coordinates = (random.randint(50, 950),random.randint(50, 450))
        score += 10
font = pygame.font.SysFont('Arial', 46)
text = font.render('Game Over', True, (255,0,0))
text2 = font.render('Press Q to quit the game', True, (255,0,0))
game_over = False
while running:
    # poll for events
    score_text = font.render(f'Score: {score} ', True, (255,0,0))
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_RIGHT]:
            x = x + 5
        if keys[pygame.K_LEFT]:
            x = x - 5
        if keys[pygame.K_UP]:
            y = y - 5
        if keys[pygame.K_DOWN]:
            y = y + 5


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    if x<0 or y<0 or x>screen_width or y>screen_height :
        game_over=True
        screen.blit(text, (300,250))
        screen.blit(text2, (300,350))

    if game_over and keys[pygame.K_q]:
        running = False
    # RENDER YOUR GAME HERE  
    # snake                    
    pygame.draw.rect(screen,"green", pygame.Rect(x, y, 20, 20))
    pygame.draw.circle(screen, "purple", food_coordinates, 10, 10)
    
    eat_food()
    screen.blit(score_text, (10,10))
    # flip() the display to put your work on screen

    pygame.display.update()

    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()