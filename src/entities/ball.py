import pygame
import os

class Ball:
    def __init__(self, x, y, speed_x, speed_y, image_path, sprite_rect):
        self.rect = pygame.Rect(x, y, sprite_rect.width, sprite_rect.height)
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.image = pygame.image.load(image_path).convert_alpha()
        self.sprite = self.image.subsurface(sprite_rect)

    def move(self, screen_width, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Colisão com as bordas superior/inferior
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.speed_x *= -1

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
