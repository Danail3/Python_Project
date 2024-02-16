from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups): # pos we want to place it, surface to dispaly on
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill('white')
        self.rect = self.image.get_frect(topleft = pos) # floating point rectangle (more precise) -> used to
        # create an object for the sprite, whicj represents the positions and size of the sprite
        self.old_rect = self.rect.copy()