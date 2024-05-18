import os

# Setting the path to resource directories
ASSETS_BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets')

assets = {
    "ASSETS_DIR": ASSETS_BASE_DIR,
    "FONTS_DIR": os.path.join(ASSETS_BASE_DIR, 'fonts'),
    "SOUNDS_DIR": os.path.join(ASSETS_BASE_DIR, 'sounds'),
    "MUSIC_DIR": os.path.join(ASSETS_BASE_DIR, 'sounds/music'),
    "SFX_DIR": os.path.join(ASSETS_BASE_DIR, 'sounds/sfx'),
    "IMAGES_DIR": os.path.join(ASSETS_BASE_DIR, 'images')
}
