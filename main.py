import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
my_font = pygame.font.SysFont('Comic Sans MS', 10)

playerLeft = 0
playerTop = 0
playerWidth = 50
playerHeight = 50
ballLeft = 100
ballTop = 200
ballWidth = 20
ballHeight = 20
obsLeft = 100
obsTop = 300
obsWidth = 10
obsHeight = 10
score = 0

def create_text(text,position1, position2):
    text_surface = new_font.render(text , False, (0, 0, 0))
    screen.blit(text_surface, (position1,position2))
    pygame.display.flip()
    time.sleep(10)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
              # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    speed = 5
    obsLeft = obsLeft + speed
    if obsLeft > 640:
       obsLeft = 0

    # speed2 = 4  
    # playerTop = playerTop + speed2
    # if playerTop > 480:
    #   playerTop = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        playerTop = playerTop-1
    if keys[pygame.K_RIGHT]:
        playerLeft = playerLeft+1
    if keys[pygame.K_LEFT]:
        playerLeft = playerLeft-1
    if keys[pygame.K_DOWN]:
        playerTop = playerTop+1

    # check if player and ball touched
    if (playerLeft + playerWidth > ballLeft and playerLeft < ballLeft + ballWidth and
        playerTop + playerHeight > ballTop and playerTop < ballTop + ballHeight):
        playerTop= 0
        a = 50
        b = 400
        ballTop = random.randint(a,b)
        ballLeft = random.randint(a,b)
        score = score + 10

    if (playerLeft + playerWidth > obsLeft and playerLeft < obsLeft + obsWidth and
        playerTop + playerHeight > obsTop and playerTop < obsTop + obsHeight):
        
    

        create_text("Game over",200, 400)
        break

    pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(playerLeft, playerTop, playerWidth, playerHeight))
    pygame.draw.rect(screen, pygame.Color(0, 255, 0), pygame.Rect(ballLeft, ballTop, ballWidth, ballHeight))
    pygame.draw.rect(screen, pygame.Color(0, 0, 150), pygame.Rect(obsLeft, obsTop, obsWidth, obsHeight))

    text_surface = my_font.render('your score = %i' % score, False, (0, 0, 0))
    screen.blit(text_surface, (540,5))

    new_font = pygame.font.SysFont('Comic Sans MS', 50)


    if (playerTop > 480 - playerHeight or playerTop < 0 or playerLeft > 640 - playerWidth or playerLeft <0):
      create_text("Game over",200, 400)
      break

    if score == 100:
      create_text("You win",400,10)
      break

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()