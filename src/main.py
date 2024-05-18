import pygame
from core import *

def main():
    # Initializing the basic pygame modules
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    
    game = Game(assets)
    game.run()
    
if __name__ == "__main__":
    main()
