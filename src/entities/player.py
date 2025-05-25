import pygame
import os

class Player:
    def __init__(self, x, y, width, height, speed, image_path=None, sprite_rect=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

        self.sprite = None
        if image_path and sprite_rect:
            sprite_sheet = pygame.image.load(image_path).convert_alpha()
            raw_sprite = sprite_sheet.subsurface(sprite_rect)

            # Redimensiona para o tamanho do paddle
            scaled_sprite = pygame.transform.scale(raw_sprite, (width, height))

            # Cria uma superfície com transparência
            self.sprite = pygame.Surface((width, height), pygame.SRCALPHA)

            # Cria uma máscara retangular com cantos arredondados
            mask = pygame.Surface((width, height), pygame.SRCALPHA)
            pygame.draw.rect(mask, (255, 255, 255, 255), mask.get_rect(), border_radius=12)

            # Aplica a imagem sobre a máscara com blending
            self.sprite.blit(mask, (0, 0))
            self.sprite.blit(scaled_sprite, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)


    def move(self, up, down, screen_height):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > -20:
            self.rect.y -= self.speed
        if keys[down] and self.rect.bottom < screen_height + 20:
            self.rect.y += self.speed

    def draw(self, screen):
        if self.sprite:
            screen.blit(self.sprite, self.rect)
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.rect)
