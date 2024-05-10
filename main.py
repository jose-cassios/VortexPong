import pygame
from pygame.locals import *
from sys import exit
import os


class VectorPosition():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pass


class ButtonUpDown():
    def __init__(self, up, dawn) -> None:
        self.up = up
        self.dawn = dawn
        pass


class Player():
    def __init__(self, score: int,
                 speed: int,
                 position: VectorPosition,
                 controls: ButtonUpDown,
                 pyGame: pygame) -> None:
        self.score = score
        self.speed = speed
        self.position = position
        self.controls = controls
        self.pyGame = pyGame
        pass

    def move(self) -> None:
        if self.pyGame.key.get_pressed()[self.controls.up] and self.position.y > 31:
            self.position.y -= self.speed
        if self.pyGame.key.get_pressed()[self.controls.dawn] and self.position.y < 380:
            self.position.y += self.speed
        pass


# Initializing the basic pygame modules
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Setting the path to resource directories
mainDirectory = os.path.dirname(__file__)
musicDirectory = os.path.join(mainDirectory, 'sounds/music')
sfxDirectory = os.path.join(mainDirectory, 'sounds/sfx')
fontsDirectory = os.path.join(mainDirectory, 'fonts')

# Setting the background music
backgroundMusic = pygame.mixer.music
backgroundMusic.load(os.path.join(musicDirectory, 'user.mp3'))
backgroundMusic.set_volume(0.5)
backgroundMusic.play(-1)

# Setting the sound effects
hitSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'hit.wav'))
scoreSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'score.wav'))
wallSFX = pygame.mixer.Sound(os.path.join(sfxDirectory, 'wall.wav'))
hitSFX.set_volume(0.2)
scoreSFX.set_volume(0.2)
wallSFX.set_volume(0.2)

# Setting the game screen dimensions
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode((screenWidth, screenHeight), RESIZABLE)

# Construindo os players
playerClass1 = Player(0, 8, VectorPosition(40, (screenHeight/2) - 35),
                      ButtonUpDown(K_w, K_s),
                      pygame)
playerClass2 = Player(0, 8, VectorPosition(40, (screenHeight/2) - 35),
                      ButtonUpDown(K_UP, K_DOWN),
                      pygame)

# Setting the initial ball position
ballPosX = screenWidth/2
ballPosY = screenHeight/2

# Setting the initial ball speed
ballSpeedY = 6
ballSpeedX = 6

# Variable that defines the game's fps
clock = pygame.time.Clock()

# Loading and setting the game font
fontPath = os.path.join(fontsDirectory, 'ka1.ttf')
fontSize = 25
customFont = pygame.font.Font(fontPath, fontSize)

# 1. Criação das Classes Player e VetorPosition
# 2. Utilizando Player para contabilizar o score
# 3. Movimentação foi colocada na classes player

while True:
    # Prepare the score display strings
    msg1 = f"Blue {playerClass1.score}"
    msg2 = f"Red: {playerClass2.score}"
    text1 = customFont.render(msg1, True, (0, 0, 0))
    text2 = customFont.render(msg2, True, (0, 0, 0))

    # Set the frame rate
    clock.tick(60)
    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Event handling loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Player 1 movement controls
    playerClass1.move()

    # Player 2 movement controls
    playerClass2.move()

    # Draw game area and boundary lines
    background = pygame.draw.rect(screen, (129, 120, 255), (0, 20, 640, 440))
    divider = pygame.draw.rect(
        screen, (255, 255, 255), (screenWidth/2, 20, 5, 440))
    upperBoundary = pygame.draw.rect(screen, (255, 255, 255), (0, 20, 640, 10))
    bottomBoundary = pygame.draw.rect(
        screen, (255, 255, 255), (0, 450, 640, 10))
    leftBoundary = pygame.draw.rect(screen, (255, 255, 255), (0, 20, 10, 440))
    rightBoundary = pygame.draw.rect(
        screen, (255, 255, 255), (screenWidth-10, 20, 10, 440))

    # Draw players and the ball
    player1 = pygame.draw.rect(
        screen, (0, 0, 255), (40, playerClass1.position.y, 20, 70))
    player2 = pygame.draw.rect(
        screen, (255, 0, 0), (screenWidth - 60, playerClass2.position.y, 20, 70))
    ball = pygame.draw.rect(screen, (255, 255, 255),
                            (ballPosX, ballPosY, 20, 20))

    # Collision detection and handling
    if ball.colliderect(leftBoundary):
        scoreSFX.play()
        playerClass2.score += 1
        ballPosX = screenWidth/2
        ballPosY = screenHeight/2
        ballSpeedX = abs(ballSpeedX)
    if ball.colliderect(rightBoundary):
        scoreSFX.play()
        playerClass1.score += 1
        ballPosX = screenWidth/2
        ballPosY = screenHeight/2
        ballSpeedX = -abs(ballSpeedX)
    if ball.colliderect(upperBoundary) or ball.colliderect(bottomBoundary):
        wallSFX.play()
        ballSpeedY = -ballSpeedY

    if ball.colliderect(player1) or ball.colliderect(player2):
        hitSFX.play()
        ballSpeedX = -ballSpeedX

    # Update ball position
    ballPosX += ballSpeedX
    ballPosY += ballSpeedY

    # Display score and update the screen
    screen.blit(text1, [20, 40])
    screen.blit(text2, [490, 40])
    pygame.display.flip()
