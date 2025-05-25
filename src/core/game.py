import pygame
import os
from entities import *
class Game:
    def __init__(self, assets: dict):
        self.assets = assets
        self.screen_width = 640
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.init_music()
        self.load_sounds()
        self.load_fonts()
        self.init_game_objects()

    def init_music(self):
        self.background_music = pygame.mixer.music
        self.background_music.load(os.path.join(self.assets['MUSIC_DIR'], 'user.mp3'))
        self.background_music.set_volume(0.5)
        self.background_music.play(-1)

    def load_sounds(self):
        self.hit_sfx = pygame.mixer.Sound(os.path.join(self.assets['SFX_DIR'], 'hit.wav'))
        self.score_sfx = pygame.mixer.Sound(os.path.join(self.assets['SFX_DIR'], 'score.wav'))
        self.wall_sfx = pygame.mixer.Sound(os.path.join(self.assets['SFX_DIR'], 'wall.wav'))
        self.hit_sfx.set_volume(0.2)
        self.score_sfx.set_volume(0.2)
        self.wall_sfx.set_volume(0.2)

    def load_fonts(self):
        font_path = os.path.join(self.assets['FONTS_DIR'], 'ka1.ttf')
        font_size = 25
        self.custom_font = pygame.font.Font(font_path, font_size)

    def init_game_objects(self):
        sprite_path = os.path.join(self.assets['IMAGES_DIR'], 'paddles', 'sprites.png')
        bg_path = os.path.join(self.assets['IMAGES_DIR'], 'backgrounds', 'bg.png')
        self.background = pygame.image.load(bg_path).convert()
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
            
        paddle_width = self.screen_width // 64
        paddle_height = self.screen_height // 6
        ball_size = self.screen_height // 12
        speed = self.screen_height // 96

        # Corrigido: regiões dos sprites
        sprite_vermelho = pygame.Rect(0, 0, 45, 150)
        sprite_azul = pygame.Rect(45, 0, 45, 150)
        sprite_bola = pygame.Rect(100, 0, 50, 50)

        self.player1 = Player(
            x=self.screen_width // 32,
            y=self.screen_height // 2 - paddle_height // 2,
            width=paddle_width,
            height=paddle_height,
            speed=speed,
            image_path=sprite_path,
            sprite_rect=sprite_vermelho
        )

        self.player2 = Player(
            x=self.screen_width - self.screen_width // 32 - paddle_width,
            y=self.screen_height // 2 - paddle_height // 2,
            width=paddle_width,
            height=paddle_height,
            speed=speed,
            image_path=sprite_path,
            sprite_rect=sprite_azul
        )

        self.ball = Ball(
            x=self.screen_width // 2 - ball_size // 2,
            y=self.screen_height // 2 - ball_size // 2,
            speed_x=speed,
            speed_y=speed,
            image_path=sprite_path,
            sprite_rect=sprite_bola
        )

        
    def run(self):
        while True:
            self.handle_events()
            self.update_game_state()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.screen_width, self.screen_height = event.w, event.h
                self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))

    def update_game_state(self):
        # Update positions of players, ball, check collisions, etc.
        self.player1.move(pygame.K_w, pygame.K_s, self.screen_height)
        self.player2.move(pygame.K_UP, pygame.K_DOWN, self.screen_height)
        self.ball.move(self.screen_width, self.screen_height)
        # Movimento e colisão da bola
        self.ball.move(self.screen_width, self.screen_height)

        # Colisão com jogadores
        if self.ball.rect.colliderect(self.player1.rect) or self.ball.rect.colliderect(self.player2.rect):
            self.ball.speed_x *= -1

    def render(self):
        self.clock.tick(60)
        # Inverter o background abaixo
        self.screen.blit(pygame.transform.flip(self.background, True, False), (0, 0))
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()
