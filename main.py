import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()
pygame.font.init()
pygame.mixer.init() 

mainDirectory = os.path.dirname(__file__)

musicDirectory = os.path.join(mainDirectory, 'sounds/music')
sfxDirectory = os.path.join(mainDirectory, 'sounds/sfx')
fontsDirectory = os.path.join(mainDirectory, 'fonts')

backgroundMusic = pygame.mixer.music
backgroundMusic.load(os.path.join(musicDirectory, 'user.mp3'))
backgroundMusic.set_volume(0.5)
backgroundMusic.play(-1)

hitSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'hit.wav'))
scoreSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'score.wav'))
wallSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'wall.wav'))
hitSFX.set_volume(0.2)
scoreSFX.set_volume(0.2)
wallSFX.set_volume(0.2)

screenWidth = 640
screenHeight = 480

player1PosY = (screenHeight/2) - 35
player2PosY = (screenHeight/2) - 35

playerPos1X = 40

ballPosX = screenWidth/2
ballPosY = screenHeight/2

ballSpeedY = 6
ballSpeedX = 6

screen = pygame.display.set_mode((screenWidth, screenHeight), RESIZABLE)

clock = pygame.time.Clock();

scorePlayer1 = 0
scorePlayer2 = 0

fontPath = os.path.join(fontsDirectory, 'ka1.ttf')
fontSize = 25
customFont = pygame.font.Font(fontPath, fontSize)

while True:
    msg1 = f"Blue {scorePlayer1}"
    msg2 = f"Red: {scorePlayer2}"
    text1 = customFont.render(msg1, True, (0, 0, 0))
    text2 = customFont.render(msg2, True, (0, 0, 0))
    
    clock.tick(60)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    if pygame.key.get_pressed()[K_w] and player1PosY > 31:
        player1PosY -= 8
    if pygame.key.get_pressed()[K_s] and player1PosY < 380:
        player1PosY += 8
    if pygame.key.get_pressed()[K_a] and playerPos1X > 31:
        playerPos1X -= 8
    if pygame.key.get_pressed()[K_d] and playerPos1X < 600:
        playerPos1X += 8
        
    if pygame.key.get_pressed()[K_UP] and player2PosY > 31:
        player2PosY -= 8
    if pygame.key.get_pressed()[K_DOWN] and player2PosY < 380:
        player2PosY += 8    
    
    background = pygame.draw.rect(screen, (129, 120, 255), (0, 20, 640, 440))
    
    ball = pygame.draw.rect(screen, (255,255,255), (ballPosX, ballPosY, 20, 20))
    
    divider = pygame.draw.rect(screen, (255,255,255), (screenWidth/2, 20, 5, 440))

    upperBoundary = pygame.draw.rect(screen, (255,255,255), (0, 20, 640, 10))
    bottomBoundary = pygame.draw.rect(screen, (255,255,255), (0, 450, 640, 10))
    leftBoundary = pygame.draw.rect(screen, (255,255,255), (0, 20, 10, 440))
    rightBoundary = pygame.draw.rect(screen, (255,255,255), (screenWidth-10, 20, 10, 440))
    
    player1 = pygame.draw.rect(screen, (0,0,255), (playerPos1X, player1PosY, 20, 70))
    player2 = pygame.draw.rect(screen, (255,0,0), (screenWidth - 60, player2PosY, 20, 70))
        
    if ball.colliderect(leftBoundary):
        scoreSFX.play()
        scorePlayer2 += 1
        ballPosX = screenWidth/2
        ballPosY = screenHeight/2
        ballSpeedX = abs(ballSpeedX)
    if ball.colliderect(rightBoundary):
        scoreSFX.play()
        scorePlayer1 += 1
        ballPosX = screenWidth/2
        ballPosY = screenHeight/2
        ballSpeedX = -abs(ballSpeedX)
        
    if ball.colliderect(upperBoundary) or ball.colliderect(bottomBoundary):
        wallSFX.play()
        ballSpeedY = -ballSpeedY

    if ball.colliderect(player1) or ball.colliderect(player2):
        hitSFX.play()
        ballSpeedX = -ballSpeedX
        
    ballPosX += ballSpeedX
    ballPosY += ballSpeedY

    screen.blit(text1, [20, 40])
    screen.blit(text2, [490, 40])
    pygame.display.flip()
