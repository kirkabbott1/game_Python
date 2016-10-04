import pygame
import time
import random
import math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
ENTER = 13

def sqr(x):
    return x * x

def distance(thing1, thing2):
    return math.sqrt(sqr(thing1.x - thing2.x) + sqr(thing1.y - thing2.y))

class Character(object):
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Hero(Character):
    def __init__(self):
        self.x = 250
        self.y = 240
        self.speed_x = 0
        self.speed_y = 0
        self.image = pygame.image.load('images/hero.png')

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y

        padding = 32
        if self.x > width - 2 * padding:
            self.x = width - 2 * padding
        if self.x < padding:
            self.x = padding
        if self.y < padding:
            self.y = padding
        if self.y > height - 2 * padding:
            self.y = height - 2 * padding

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == KEY_UP:
                self.speed_y = -4
            elif event.key == KEY_DOWN:
                self.speed_y = 4
            elif event.key == KEY_LEFT:
                self.speed_x = -4
            elif event.key == KEY_RIGHT:
                self.speed_x = 4
        if event.type == pygame.KEYUP:
            if event.key == KEY_UP:
                self.speed_y = 0
            elif event.key == KEY_DOWN:
                self.speed_y = 0
            elif event.key == KEY_LEFT:
                self.speed_x = 0
            elif event.key == KEY_RIGHT:
                self.speed_x = 0

    def collides(self, monster):
        return distance(self, monster) < 32

class Monster(Character):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.speed_x = 5
        self.speed_y = 0
        self.image = pygame.image.load('images/monster.png')
        self.direction_change_countdown = 120

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

        self.maybe_direction_change()

    def maybe_direction_change(self):
        self.direction_change_countdown -= 1
        if self.direction_change_countdown <= 0:
            self.direction_change_countdown = 120
            self.change_direction()

    def change_direction(self):
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

    def respawn(self, width, height):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)

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
    pygame.mixer.init()
    background_image = pygame.image.load('images/background.png')
    win_sound = pygame.mixer.Sound('sounds/win.wav')

    monster = Monster()
    hero = Hero()

    # game loop
    game_over = False
    stop_game = False
    while not stop_game:
        # look through user events fired
        for event in pygame.event.get():
            ################################
            # PUT EVENT HANDLING CODE HERE #
            ################################
            hero.process_event(event)
            if event.type == pygame.KEYDOWN:
                if event.key == ENTER:
                    game_over = False
                    print "restarting game"
            if event.type == pygame.QUIT:
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        #######################################
        # PUT LOGIC TO UPDATE GAME STATE HERE #
        #######################################
        if not game_over:
            monster.update(width, height)
            hero.update(width, height)
            if hero.collides(monster):
                win_sound.play()
                game_over = True
                monster.respawn(width, height)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        screen.blit(background_image, (0, 0))

        hero.render(screen)
        if game_over:
            font = pygame.font.Font(None, 40)
            text = font.render('Hit ENTER to play again!', True, (0, 0, 0))
            screen.blit(text, (80, 230))
        else:
            monster.render(screen)

        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
