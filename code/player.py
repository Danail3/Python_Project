from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups): # pos of the player and groups that the player should be in
        super().__init__(groups)
        self.image = pygame.Surface((48, 56)) # image is for visual purposes
        self.image.fill('red')
        self.rect = self.image.get_frect(topleft = pos) # for technical purposes -> collisions, positioning etc.
        
        # movement
        self.direction = vector()
        self.speed = 200
        
    def input(self):
        keys = pygame.key.get_pressed() # all of the currently pressed keys
        input_vector = vector() # on every frame of the game the input_vector start with 0, 0
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        
        #normalize, cuz we want only the speed to determine how fast we are moving, this way we will always have a vector with length 1
        self.direction = input_vector.normalize() if input_vector else input_vector# change the directions the player is looking to

    def move(self, dt):
        #dt gives as a consistency of how fast the game will be independently from the computer the customer is using
        self.rect.topleft += self.direction * self.speed * dt # taking the current position and increasing it with certain speed at a current direction
    
    def update(self, dt):
        self.input()
        self.move(dt)
        