# Example file showing a basic pygame "game loop"
import pygame

screen_width, screen_height = 1000, 500

# pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
x, y = 100, 100
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x = x + 5
    if keys[pygame.K_LEFT]:
        x = x - 5
    if keys[pygame.K_UP]:
        y = y - 5
    if keys[pygame.K_DOWN]:
        y = y + 5

    if x<0 or y<0 or x>screen_width or y>screen_height :
        running=False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE                      x    y
    pygame.draw.rect(screen,"green", pygame.Rect(x, y, 20, 20))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()