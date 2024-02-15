from settings import * 
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Super Mario World')
        self.clock = pygame.time.Clock() # the clock object can control the frame rate
        
        self.tmx_maps = {0: load_pygame('data/levels/omni.tmx')}
        print(self.tmx_maps)
        self.current_stage = Level(self.tmx_maps[0])
        

    def run(self):
        while True:
            # self.clock.tick() -> miliseconds to draw 1 frame
            dt = self.clock.tick() / 1000 # we want this in seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)
            pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()