import pygame
import time
import random

class Monster(object):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed_x = 5
        self.speed_y = 0
        self.image = pygame.image.load('images/monster.png')
        self.time_till_dir_change = None

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height

        self.maybe_change_direction()

    def maybe_change_direction(self):
        if self.time_till_dir_change is None:
            now = time.time()
            self.time_till_dir_change = now + 1
            return

        now = time.time()

        if now >= self.time_till_dir_change:
            self.time_till_dir_change = now + 1
            # perform direction change
            print 'perform direction change'
            num = random.randint(0, 3)
            if num == 0:
                self.speed_x = 0
                self.speed_y = -5
            elif num == 1:
                self.speed_x = 5
                self.speed_y = 0
            elif num == 2:
                self.speed_x = 0
                self.speed_y = 5
            else:
                self.speed_x = -5
                self.speed_y = 0

def main():
    # declare the size of the canvas
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # initialize the pygame framework
    pygame.init()

    # create screen
    screen = pygame.display.set_mode((width, height))

    # set window caption
    pygame.display.set_caption('Simple Example')

    # create a clock
    clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load('images/background.png')
    hero_image = pygame.image.load('images/hero.png')

    monster = Monster()



    # game loop
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        monster.update(width, height)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(background_image, (0, 0))

        screen.blit(hero_image, (250, 240))
        screen.blit(monster.image, (monster.x, monster.y))

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
