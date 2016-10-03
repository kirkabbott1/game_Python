import pygame

class Ball(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.speed_x = 100
        self.speed_y = 100
        self.radius = radius
        self.color = color

    def update(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x + self.radius > width:
            self.speed_x = -20
        if self.y + self.radius > height:
            self.speed_y = -20
        if self.x - self.radius < 0:
            self.speed_x = 30
        if self.y - self.radius < 0:
            self.speed_y = 50

    def render(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def main():
    # declare the size of the canvas
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    ball_list = [
        Ball(20, 20, 20, (20, 0, 200)),
        Ball(40, 25, 40, (200, 200, 0)),
        Ball(30, 17, 90, (20, 89, 100)),
        Ball(10, 5, 30, (20, 89, 100)),
        Ball(80, 50, 50, (20, 200, 0)),
        Ball(67, 90, 10, (20, 0, 100))
    ]
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
        for ball in ball_list:
            ball.update(width, height)
        #######################################

        # fill background color
        screen.fill(blue_color)

        ################################
        # PUT CUSTOM DISPLAY CODE HERE #
        ################################
        for ball in ball_list:
            ball.render(screen)
        # update the canvas display with the currently drawn frame
        pygame.display.update()

        # tick the clock to enforce a max framerate
        clock.tick(60)

    # quit pygame properly to clean up resources
    pygame.quit()

if __name__ == '__main__':
    main()
