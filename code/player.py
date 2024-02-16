from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites): # pos of the player and groups that the player should be in
        super().__init__(groups)
        self.image = pygame.Surface((48, 56)) # image is for visual purposes
        self.image.fill('red')
        
        #rects
        self.rect = self.image.get_frect(topleft = pos) # for technical purposes -> collisions, positioning etc.
        self.old_rect = self.rect.copy()
        
        # movement
        self.direction = vector()
        self.speed = 200
        self.gravity = 400 # when we fall
        
        # collistion
        self.collistion_sprites = collision_sprites
        
    def input(self):
        keys = pygame.key.get_pressed() # all of the currently pressed keys
        input_vector = vector() # on every frame of the game the input_vector start with 0, 0
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        
        #normalize, cuz we want only the speed to determine how fast we are moving, this way we will always have a vector with length 1
        self.direction.x = input_vector.normalize().x if input_vector else input_vector.x# change the directions the player is looking to

    def move(self, dt):
        #horizontal
        #dt gives as a consistency of how fast the game will be independently from the computer the customer is using
        self.rect.x += self.direction.x * self.speed * dt # taking the current position and increasing it with certain speed at a current direction
        self.collision('horizontal')
        
        
        #vertical
        self.direction.y += self.gravity / 2 * dt # the more we fall, the faster we fall
        self.rect.y += self.direction.y * dt
        self.direction.y += self.gravity / 2 * dt # to make it frame rate independant
        self.collision('vertical')
        
        
    def collision(self, axis):
        for sprite in self.collistion_sprites:
            if sprite.rect.colliderect(self.rect): # checking for overlapping
                if axis == 'horizontal':
                    #left and the second condition tells us if the moving sprite comes from right or left
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                    
                    #right
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                else:
                    #top
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        
                    # bottom
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                            
                
    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()
        self.move(dt)
        