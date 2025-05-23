import pygame
import os

class Player:
    def __init__(self, x, y, width, height, speed, image_path=None, sprite_rect=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

        self.sprite = None
        if image_path and sprite_rect:
            sprite_sheet = pygame.image.load(image_path).convert_alpha()
            self.sprite = sprite_sheet.subsurface(sprite_rect)
            self.sprite = pygame.transform.scale(self.sprite, (width, height))

    def move(self, up, down):
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.rect.y -= self.speed
        if keys[down]:
            self.rect.y += self.speed

    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
