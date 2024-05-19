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
        # Initialize players, ball, scoreboard, etc.
        self.player1 = Player(x=20, y=350, width=10, height=30, speed=5)
        self.player2 = Player(x=600, y=350, width=10, height=30, speed=5)


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

    def update_game_state(self):
        # Update positions of players, ball, check collisions, etc.
        self.player1.move(pygame.K_w, pygame.K_UP)
        self.player2.move(pygame.K_u, pygame.K_DOWN)

    def render(self):
        self.clock.tick(60)
        self.screen.fill((0, 0, 0))
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        pygame.display.flip()
