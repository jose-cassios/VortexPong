import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed
            
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
