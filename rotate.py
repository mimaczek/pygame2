"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""
import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

WSPOLCZYNNIK_PREDKOSCI = 0.01


# This class represents the ball
# It derives from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
    # READ BEFORE USING:
    # This constructor lets you use any graphic:
    # my_sprite = Block("any_graphic.png")
    # But if you DON'T want any graphic, use the following instead:
    '''
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("my_graphic.png").convert()

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
    '''

    def __init__(self, filename, colorkey):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.original_image = pygame.image.load(filename).convert()
        self.image = self.original_image

        # Set background color to be transparent. Adjust to WHITE if your
        # background is WHITE.
        self.image.set_colorkey(colorkey)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.angle = 90
        self.angle_change = 10

    def update_org(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.angle += self.angle_change
        self.angle = self.angle % 360

    def update(self, pos):
        print("Klik:", pos[0], pos[1])
        #print("Klik:", pos[0], pos[1])
        self.angle = math.atan2((self.rect.x-pos[0]), (self.rect.y-pos[1]))/math.pi*180
        l = ((self.rect.x - pos[0])**2 + (self.rect.y - pos[1])**2)**0.5
        print("K??t:", self.angle)
        print("odl:", l)
        #self.angle = self.angle + 1
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        predkosc = [self.rect.x - pos[0], self.rect.y - pos[1]]
        self.rect.x = self.rect.x - predkosc[0] * WSPOLCZYNNIK_PREDKOSCI
        self.rect.y = self.rect.y - predkosc[1] * WSPOLCZYNNIK_PREDKOSCI




        # self.angle += self.angle_change
        # self.angle = self.angle % 360
        # elf.angle = kat


    # Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 1500
screen_height = 1000
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(1):
    # This represents a block
    block = Block("Enemy.png", BLACK)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    block.rect.x = 100
    block.rect.y = 100
    block.angle = random.randrange(360)
    block.angle = 0
    block.angle_change = random.randrange(-1, 2)
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create a RED player block
player = Block("playerHEAD.png", BLACK)
player.angle_change = 0
#all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(WHITE)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()

    # Fetch the x and y out of the list,
    # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    #all_sprites_list.update()
    all_sprites_list.update(pos)

    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    #pygame.time.delay(1000)

pygame.quit()