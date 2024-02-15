from settings import *
from sprites import Sprite

class Level:
    def __init__(self, tmx_map):
        self.display_surface = pygame.display.get_surface()
        
        #groups
        self.all_sprites = pygame.sprite.Group()
        
        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles(): # x and y are positions inside of a grid, not pixels
           Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Objects'): # dont need .tiles at the end, cuz we are not working with tiles
            if obj.name == 'player':
                print(obj.x)
                print(obj.y)
		# groups 
		#self.all_sprites = pygame.sprite.Group()

		#self.setup(tmx_map)

	

		

    def run(self):
		#self.all_sprites.update(dt)
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)