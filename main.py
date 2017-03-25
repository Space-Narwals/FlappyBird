import pygame;
import os;
import random;


version = "1.0.0 BETA"

clock = pygame.time.Clock()

debug = True
SCREEN_WIDTH = 144
SCEREN_HEIGHT = 256;
SCALE = 3;

TICKS_TO_SPAWN = 120;

spriteimage = pygame.image.load('res/sprites.png')


class Pipe(pygame.sprite.Sprite):
    def __init__(self, side, y):

        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        pipeImage = pygame.Surface((26, 159));
        if side == "bottom":
            pipeImage.blit(spriteimage, (0, 0), (84, 323, 26, 159))
        else:
            pipeImage.blit(spriteimage, (0, 0), (56, 323, 26, 159))
        pipeImage = pygame.transform.scale(pipeImage, (26 * SCALE, 159 * SCALE));

        self.image = pipeImage;
        self.rect = self.image.get_rect()
        self.rect.x = 144 * SCALE + 50;
        self.rect.y = y;

    def update(self):
        self.rect.x = self.rect.x - 3
        if(self.rect.x < 0 - (26 * SCALE)):
            self.kill()

class ScrollingBackground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        scrollingBackground = pygame.Surface((168, 56));
        scrollingBackground.blit(spriteimage, (0, 0), (292, 0, 168, 56))
        scrollingBackground = pygame.transform.scale(scrollingBackground, (168 * SCALE, 56 * SCALE));
        self.image = scrollingBackground;
        self.rect = self.image.get_rect();
        self.rect.x = 0;
        self.rect.y = 200 * SCALE;


def main():
    counter = 0;
    running = True
    print "Starting version", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Flappy Bird " + version)
    screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCEREN_HEIGHT * SCALE))

    backgroundcrop = pygame.Surface((SCREEN_WIDTH, SCEREN_HEIGHT))
    backgroundcrop.blit(spriteimage, (0, 0), (0, 0, SCREEN_WIDTH, SCEREN_HEIGHT))
    backgroundcrop = pygame.transform.scale(backgroundcrop, (SCREEN_WIDTH * SCALE, SCEREN_HEIGHT * SCALE));

    pipe_list = pygame.sprite.Group();
    background_list = pygame.sprite.Group();

    scrollingBackground = ScrollingBackground()
    background_list.add(scrollingBackground);

    while running:
        clock.tick(60);

        counter = counter + 1;

        if counter == TICKS_TO_SPAWN:
            counter = 0;
            start = random.randint(5 * SCALE, 140 * SCALE) - (159 * SCALE);
            topPipe = Pipe("top", start)
            bottomPipe = Pipe("bottom", start + (159 * SCALE) + (50 * SCALE));
            pipe_list.add(topPipe)
            pipe_list.add(bottomPipe)

        screen.fill((0, 0, 0))
        screen.blit(backgroundcrop, backgroundcrop.get_rect())
        pipe_list.draw(screen)
        background_list.draw(screen)
        pygame.display.flip()

        background_list.update();
        pipe_list.update();


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(event)


if __name__ == "__main__": main()
