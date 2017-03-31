import pygame
import os
import random
import ctypes

version = "1.0.2 PRE-RELEASE"

clock = pygame.time.Clock()

debug = True
SCREEN_WIDTH = 144
SCREEN_HEIGHT = 256
SCALE = 3

#How many ticks should we wait before spawnning another pair of pipes?
TICKS_TO_SPAWN = 120

PIPE_HEIGHT = 159
PIPE_WIDTH = 26

BACKGROUND_WIDTH = 168
BACKROUND_HEIGHT = 56

BIRD_HEIGHT = 12
BIRD_WIDTH = 17
#Represents the Y cordinate of where the scrolling background begins.
BACKGROUND_Y_START = 200

spriteimage = pygame.image.load('res/sprites.png')

i_icon = os.getcwd() + '\\res\\flappy_bird_icon.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption("Flappy Bird")

myappid = 'my_otc.flappy_bird.v1_2' # icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Pipe(pygame.sprite.Sprite):
    def __init__(self, side, y):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        pipeImage = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT), pygame.SRCALPHA, 32)
        if side == "bottom":
            pipeImage.blit(spriteimage, (0, 0), (84, 323, PIPE_WIDTH, PIPE_HEIGHT))
        else:
            pipeImage.blit(spriteimage, (0, 0), (56, 323, PIPE_WIDTH, PIPE_HEIGHT))
        pipeImage = pygame.transform.scale(pipeImage, (PIPE_WIDTH * SCALE, PIPE_HEIGHT * SCALE))

        self.image = pipeImage.convert_alpha()
        self.rect = self.image.get_rect()
        #Spawn the pipes 50 pixels to the right of the
        self.rect.x = 144 * SCALE + 50
        self.rect.y = y

    def update(self):
        self.rect.x = self.rect.x - 3
        #If the sprite goes off the screen, destroy it.
        if (self.rect.x < 0 - (PIPE_WIDTH * SCALE)):
            self.kill()

class ScrollingBackground(pygame.sprite.Sprite):
    def __init__(self, startX):
        pygame.sprite.Sprite.__init__(self)
        scrollingBackground = pygame.Surface((BACKGROUND_WIDTH, BACKROUND_HEIGHT))
        scrollingBackground.blit(spriteimage, (0, 0), (292, 0, BACKGROUND_WIDTH, BACKROUND_HEIGHT))
        scrollingBackground = pygame.transform.scale(scrollingBackground, (BACKGROUND_WIDTH * SCALE, BACKROUND_HEIGHT * SCALE))
        self.image = scrollingBackground
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = BACKGROUND_Y_START * SCALE
    def update(self):
        self.rect.x = self.rect.x - 3
        #Get the right point so we can calculate when the image is fully off the screen. Then we need to set it back to its original position.
        right = self.rect.x + (BACKGROUND_WIDTH * SCALE)
        if right == 0:
            self.rect.x = (BACKGROUND_WIDTH * SCALE)

class Bird(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        firstBird = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT), pygame.SRCALPHA, 32)
        firstBird.blit(spriteimage, (0, 0), (3, 491, BIRD_WIDTH, BIRD_HEIGHT))
        firstBird = pygame.transform.scale(firstBird, (BIRD_WIDTH * SCALE, BIRD_HEIGHT * SCALE))
        self.image = firstBird.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH / 4) * SCALE
        self.rect.y = (SCREEN_HEIGHT / 2) * SCALE
        self.ANIMATION_COUNTER = 0

    def update(self):
        self.ANIMATION_COUNTER += 1

        if self.ANIMATION_COUNTER == 5:
            firstBird = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT), pygame.SRCALPHA, 32)
            firstBird.blit(spriteimage, (0, 0), (3, 491, BIRD_WIDTH, BIRD_HEIGHT))
            firstBird = pygame.transform.scale(firstBird, (BIRD_WIDTH * SCALE, BIRD_HEIGHT * SCALE))
            self.image = firstBird.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = (SCREEN_WIDTH / 4) * SCALE
            self.rect.y = (SCREEN_HEIGHT / 2) * SCALE

        if self.ANIMATION_COUNTER == 10:
            firstBird = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT), pygame.SRCALPHA, 32)
            firstBird.blit(spriteimage, (0, 0), (31, 491, BIRD_WIDTH, BIRD_HEIGHT))
            firstBird = pygame.transform.scale(firstBird, (BIRD_WIDTH * SCALE, BIRD_HEIGHT * SCALE))
            self.image = firstBird.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = (SCREEN_WIDTH / 4) * SCALE
            self.rect.y = (SCREEN_HEIGHT / 2) * SCALE

        if self.ANIMATION_COUNTER == 15:
            firstBird = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT), pygame.SRCALPHA, 32)
            firstBird.blit(spriteimage, (0, 0), (59, 491, BIRD_WIDTH, BIRD_HEIGHT))
            firstBird = pygame.transform.scale(firstBird, (BIRD_WIDTH * SCALE, BIRD_HEIGHT * SCALE))
            self.image = firstBird.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = (SCREEN_WIDTH / 4) * SCALE
            self.rect.y = (SCREEN_HEIGHT / 2) * SCALE

            self.ANIMATION_COUNTER = 0

def main():
    counter = 0
    running = True
    print "Starting version", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Flappy Bird " + version)
    screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

    backgroundcrop = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    backgroundcrop.blit(spriteimage, (0, 0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    backgroundcrop = pygame.transform.scale(backgroundcrop, (SCREEN_WIDTH * SCALE, SCREEN_HEIGHT * SCALE))

    pipe_list = pygame.sprite.Group()
    background_list = pygame.sprite.Group()
    bird_list = pygame.sprite.Group()


    #Start one background at 0, start another right at the end of the other one.
    #The X of the right point is BACKGROUND_WIDTH * SCALE
    bg1 = ScrollingBackground(0)
    bg2 = ScrollingBackground(BACKGROUND_WIDTH * SCALE)
    background_list.add(bg1)
    background_list.add(bg2)


    bird = Bird();
    bird_list.add(bird)
    while running:
        clock.tick(60)

        counter = counter + 1

        if counter == TICKS_TO_SPAWN:
            counter = 0
            #Generate a random number between 5 and 140.
            #Adjust for SCALE
            #Subtract the length of the pipe so so we get the "Top" pipe.
            start = random.randint(5 * SCALE, 140 * SCALE) - (PIPE_HEIGHT * SCALE)
            topPipe = Pipe("top", start)
            #Add at least 50 pixels of clearence for the player to navigate through.
            bottomPipe = Pipe("bottom", start + (PIPE_HEIGHT * SCALE) + (50 * SCALE))
            pipe_list.add(topPipe)
            pipe_list.add(bottomPipe)

        screen.blit(backgroundcrop, backgroundcrop.get_rect())
        pipe_list.draw(screen)
        bird_list.draw(screen)
        background_list.draw(screen)
        pygame.display.flip()

        background_list.update()
        pipe_list.update()
        bird_list.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(event)


if __name__ == "__main__": main()
