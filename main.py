import pygame;
import os;

version = "1.0.0 BETA"

clock = pygame.time.Clock()

debug = True
SCREEN_WIDTH = 144
SCEREN_HEIGHT = 256;
SCALE = 3;

def main():
    running = True
    print "Starting version", version
    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("Flappy Bird " + version)
    screen = pygame.display.set_mode((SCREEN_WIDTH * SCALE, SCEREN_HEIGHT * SCALE))

    spriteimage = pygame.image.load('res/sprites.png')

    backgroundcrop = pygame.Surface((SCREEN_WIDTH, SCEREN_HEIGHT))
    backgroundcrop.blit(spriteimage, (0,0), (0, 0, SCREEN_WIDTH, SCEREN_HEIGHT))
    backgroundcrop = pygame.transform.scale(backgroundcrop, (SCREEN_WIDTH * SCALE, SCEREN_HEIGHT * SCALE));

    scrollingBackground = pygame.Surface((168, 56));
    scrollingBackground.blit(spriteimage, (0, 0), (292, 0, 168, 56))
    scrollingBackground = pygame.transform.scale(scrollingBackground, (168 * SCALE, 56 * SCALE));

    x = 0;
    y = 200 * SCALE;


    while running:
        clock.tick(60);
        screen.fill((0, 0, 0))
        screen.blit(backgroundcrop, backgroundcrop.get_rect())
        screen.blit(scrollingBackground, (x, y))
        pygame.display.flip()


        x = x + 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print(event)

if __name__ == "__main__": main()
