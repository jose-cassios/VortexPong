import pygame
import os

class Ball:
    def __init__(self, x, y, speed_x, speed_y, image_path, sprite_rect):
        self.rect = pygame.Rect(x, y, sprite_rect.width, sprite_rect.height)
        self.speed_x = speed_x
        self.speed_y = speed_y

        # Carrega o sprite completo da imagem
        full_image = pygame.image.load(image_path).convert_alpha()
        ball_sprite = full_image.subsurface(sprite_rect)

        # Cria uma superfície circular com fundo transparente
        self.sprite = pygame.Surface((sprite_rect.width, sprite_rect.height), pygame.SRCALPHA)
        radius = sprite_rect.width // 2

        # Cria uma máscara circular e aplica à sprite original
        pygame.draw.circle(self.sprite, (255, 255, 255, 255), (radius, radius), radius)
        self.sprite.blit(ball_sprite, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)


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
