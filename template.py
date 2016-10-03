import pygame
import random


KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Character(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = -5

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        # if self.x  > width:
        #     self.speed_x = -10
        # if self.y > height:
        #     self.speed_y = -1
        # if self.x < 0:
        #     self.speed_x = 13
        # if self.y < 0:
        #     self.speed_y = 18

class Monster(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 5
        self.speed_y = 0

class Hero(Character):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0



def main():
    # declare the size of the canvas
    width = 512
    height = 480
    # screen.fill((0,0,0))
    # initialize the pygame framework
    pygame.init()


    # create screen
    screen = pygame.display.set_mode((width, height))
    monster = Monster(340, 30)
    hero = Hero(240, 240)
    change_dir_countdown = 120
    # # set window caption
    # pygame.display.set_caption('Simple Example')
    #
    # # create a clock
    # clock = pygame.time.Clock()

    ################################
    # PUT INITIALIZATION CODE HERE #
    ################################
    background_image = pygame.image.load('images/background.png').convert_alpha()
    monster_img = pygame.image.load('images/monster.png').convert_alpha()
    hero_img = pygame.image.load('images/hero.png').convert_alpha()
    # background_image = pygame.image.load('images/background.png').convert_alpha()
    # game loop

    stop_game = False
    while not stop_game:
        # look through user events fired



        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            if event.type == pygame.KEYDOWN:
                # activate the cooresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 5
                elif event.key == KEY_UP:
                    hero.speed_y = -5
                elif event.key == KEY_LEFT:
                    hero.speed_x = -5
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        monster.update(width, height)
        # monster.x += 5
        if monster.x >= width:
            monster.x = 0
        if monster.y >= height:
            monster.y = 0
        if monster.x < 0:
            monster.x = width
        if monster.y < 0:
            monster.y = height

        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            print "change_dir_countdown"
            ran = random.randint(0, 3)
            if ran == 0:
                monster.speed_x = 0
                monster.speed_y = -random.randint(0, 9)
            elif ran == 1:
                monster.speed_x = 5
                monster.speed_y = 0
            elif ran == 2:
                monster.speed_x = 0
                monster.speed_y = 5
            else:
                monster.speed_x = -random.randint(0, 9)
                monster.speed_y = 0








        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################

        screen.blit(background_image, (0, 0))

        screen.blit(monster_img, (monster.x, monster.y))

        screen.blit(hero_img, (240, 240))
        # fill background color
        # screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        # clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
