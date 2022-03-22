import pygame
import random
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 900))
# https://opengameart.org/content/pixel-race-cars-with-missiles
playerSprite0 = pygame.image.load('pixel_racecar_green_missiles_0.png')
playerSprite = pygame.transform.scale(playerSprite0, (80, 80))

enemySprite0 = pygame.image.load('pixel_racecar_red_missiles.png')
enemySprite = pygame.transform.scale(enemySprite0, (80, 80))

Jet0 = pygame.image.load('pixel_racecar_blue_missiles.png')
JetSprite = pygame.transform.scale(Jet0, (80, 80))

Kart0 = pygame.image.load('pixel_racecar_yellow_missiles.png')
kartSprite = pygame.transform.scale(Kart0, (80, 80))

road = pygame.image.load('background-1_0.png')
roadBG = pygame.transform.scale(road, (600, 900))
wallSprite1 = pygame.image.load('brick_wall-red.png')
wallSprite = pygame.transform.scale(wallSprite1, (80, 80))

enemySprite1 = pygame.image.load('pixel_racecar_green_missiles_0.png')
# https://opengameart.org/content/rocket
missleSprite0 = pygame.image.load('cohete_off_0.png')
missleSprite = pygame.transform.scale(missleSprite0, (40, 40))

# https://opengameart.org/content/blue-star-1616
starSprite0 = pygame.image.load('star_6.png')
starSprite = pygame.transform.scale(starSprite0, (80, 80))
# https://www.pngfind.com/mpng/hJhwRTR_green-shells-png-super-mario-turtle-shell-png/

# turtleSprite0 = pygame.image.load(
#     '593-5934886_green-shells-png-super-mario-turtle-shell-png.png')
# turtleSprite = pygame.transform.scale(turtleSprite0, (20, 20))
# https://static.wikia.nocookie.net/mariokart/images/3/39/BananaMK8.png/revision/latest?cb=20140520034128
banana0 = pygame.image.load(
    'BananaMK8.png')
bananaSprite = pygame.transform.scale(banana0, (40, 40))


class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = starSprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.rect.y = self.rect.y + 2
        self.y = self.y + 2


class Rocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = missleSprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.rect.y = self.rect.y - 10
        self.y = self.y - 10


class Banana:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = bananaSprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.rect.y = self.rect.y + 10
        self.y = self.y + 10


class Wall:
    def __init__(self, x, y, png):
        self.x = x
        self.y = y
        self.image = png
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def incoming(self, speed):
        self.rect.y = self.rect.y + speed
        self.y = self.y + speed


class Car:

    def __init__(self, x, y, item, png):
        self.x = x
        self.y = y
        self.item = item
        self.image = png
        self.itemList = []
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def useItem(self):
        self.itemList.append(self.item)

    # def update(self):
    #     """ Update the player's position. """
    #     # Get the current mouse position. This returns the position
    #     # as a list of two numbers.
    #     pos = pygame.mouse.get_pos()

    #     # Set the player x position to the mouse x position
    #     self.rect.x = pos[0]

    # def update(self):
    #     """ Update the player's position. """
    #     # Get the current mouse position. This returns the position
    #     # as a list of two numbers.
    #     pos = pygame.mouse.get_pos()

    #     # Set the player x position to the mouse x position
    #     self.rect.x = pos[0]


class Racer(Car):

    def __init__(self, x, y, png):
        self.x = x
        self.y = y
        self.image = png
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def useItem(self):
        self.itemList.append(self.item)

    def move(self, speed):
        self.y = self.y - speed*2
        self.x += random.randrange(-4, 4)


class Jet(Car):

    def __init__(self, x, y, png):
        self.x = x
        self.y = y
        self.image = png
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def useItem(self):
        self.itemList.append(self.item)

    def move(self, speed):
        self.y = self.y - speed*2
        self.x -= random.randrange(-4, 4)


class Kart(Car):

    def __init__(self, x, y, png):
        self.x = x
        self.y = y
        self.image = png
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def useItem(self):
        self.itemList.append(self.item)

    def move(self, speed):
        self.y = self.y + speed
        self.x -= random.randrange(-3, 3)


def touch(a, b):

    if a.mask.overlap(b.mask, (b.x - a.x, b.y - a.y)) == None:  # second value diff left
        return False
    else:
        return True


def main():
    score = 10000
    level = 1
    speed = 3
    floor = 0
    player = Car(299, 800, 'a', playerSprite)
    run = True

    walls = []
    # enemy1 = Racer(299, 900, 'a', playerSprite)
    cars = []
    karts = []
    itemList = []
    bulletList = []
    bananaList = []

    def update():
        screen.blit(roadBG, (0, 0))
        scoreCount = pygame.font.SysFont("arial", 36).render(
            f"Distance: {score}", 1, (255, 255, 255))
        levelCount = pygame.font.SysFont("arial", 36).render(
            f"Lap: {floor}", 1, (0, 255, 0))
        screen.blit(scoreCount, (50, 850))
        screen.blit(levelCount, (400, 850))
        speedCount = pygame.font.SysFont("arial", 36).render(
            f"Speed: {level}", 1, (0, 255, 0))
        screen.blit(speedCount, (250, 50))
        player.draw()
        # print(player.y)
        for w in walls:
            # print(w.y)
            w.draw()
            # if w.rect.x - player.rect.x < 20:
            #     print('same x')
            # if w.rect.y - player.rect.y < 20:
            #     print('same y')
            # if int(w.y) == player.y:
            #     print('adsad')
        for c in cars:
            # print(w.y)
            c.draw()

        for k in karts:
            # print(w.y)
            k.draw()
        for i in itemList:
            i.draw()

        for b in bulletList:
            b.draw()
        for a in bananaList:
            a.draw()
        pygame.display.update()

    while run == True:
        # print('a')
        update()
        score -= 1

        if score % 200 == 0:
            level += 0.5
            incomingItem = Item(random.randrange(50, 500),
                                random.randrange(-500, -100))
            itemList.append(incomingItem)
        if score % 200 == 0:
            level += 0.5
            incomingWall = Wall(random.randrange(50, 500),
                                random.randrange(-500, -100), wallSprite)
            walls.append(incomingWall)

        if score % 100 == 0:
            incomingCar = Racer(random.randrange(400, 500),
                                random.randrange(1000, 1200), enemySprite)
            cars.append(incomingCar)

        if score % 100 == 0:
            incomingJet = Jet(random.randrange(50, 150),
                              random.randrange(1000, 1200), JetSprite)
            cars.append(incomingJet)

        if score % 100 == 0:
            incomingKart = Kart(random.randrange(0, 350),
                                random.randrange(-100, -50), kartSprite)
            karts.append(incomingKart)
        if score < 10:
            score = 9999
            floor += 1
            level += 1

        # for w in walls:
        #     col = w.rect.colliderect(player.rect)
        #     if col:
        #         print("GAME OVER!")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - speed - 100 > 0:  # left
            player.x -= speed * level
            player.rect.x -= speed * level

        if keys[pygame.K_d] and player.x + speed + 160 < 600:  # right
            player.x += speed * level
            player.rect.x -= speed * level
        if keys[pygame.K_w] and player.y - speed > 0:  # up
            player.y -= speed * level
            player.rect.x -= speed * level
        if keys[pygame.K_s] and player.y + speed + 50 < 899:  # down
            player.y += speed * level
            player.rect.x -= speed * level
        if keys[pygame.K_SPACE]:
            nana = Banana(player.x + 10, player.y + 100)
            bananaList.append(nana)

        for w in walls:
            w.incoming(level+0.5)

            if w.y > 900:
                walls.remove(w)
                print('wall removed')

            if touch(w, player):
                print('hit')
                run = False

            # if ((w.y - player.y < 5) & (w.y - player.y > -5)):

            #     print('same y ')
            #     if ((w.x - player.x < 5) & (w.x - player.x > -5)):
            #         print('same x')
        for k in karts:
            k.move(level)

            if k.y < -300:
                karts.remove(k)

            if touch(k, player):
                print('hit')
                run = False
        for c in cars:
            c.move(level)

            if c.y < -300:
                cars.remove(c)

            if touch(c, player):
                print('hit')
                run = False
            for w in walls:
                if touch(c, w):
                    walls.remove(w)
                    cars.remove(c)

            for k in karts:
                if touch(c, k):
                    karts.remove(k)

        for i in itemList:
            i.move()
            if touch(i, player):
                print('touched item')
                itemList.remove(i)
                missle = Rocket(player.x + 10, player.y - 20)
                bulletList.append(missle)
            for k in karts:
                if touch(i, k):

                    itemList.remove(i)
                    nana = Banana(k.x+10, k.y+50)
                    bananaList.append(nana)

            for c in cars:
                if touch(i, c):

                    itemList.remove(i)
                    nana = Banana(k.x+10, k.y+50)
                    bananaList.append(nana)
        for b in bulletList:
            b.move()
            if b.y < -300:
                bulletList.remove(b)
            if touch(b, player):
                run = False
            for w in walls:
                if touch(b, w):
                    walls.remove(w)
                    bulletList.remove(b)
            for k in karts:
                if touch(b, k):
                    karts.remove(k)
                    bulletList.remove(b)

            for c in cars:
                if touch(b, c):
                    cars.remove(c)
                    bulletList.remove(b)

        for a in bananaList:
            a.move()
            if a.y > 1300:
                bananaList.remove(a)
            if touch(a, player):
                run = False

            for k in karts:
                if touch(a, k):
                    karts.remove(k)

            for c in cars:
                if touch(a, c):
                    cars.remove(c)
                    bananaList.remove(a)
# class Game:
#     def __init__(self):
#         self.level = 0


def main_menu():
    running = True
    while running == True:
        screen.blit(roadBG, (0, 0))
        header = pygame.font.SysFont("arial", 50).render(
            "Click to Race \n ", 1, (0, 210, 0))
        instruc = pygame.font.SysFont("arial", 50).render(
            "Spacebar for banana \n ", 1, (0, 210, 0))
        instruc2 = pygame.font.SysFont("arial", 50).render(
            "Get stars for rocket \n ", 1, (0, 210, 0))
        screen.blit(header, (150, 150))
        screen.blit(instruc, (150, 550))
        screen.blit(instruc2, (150, 750))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
print('Game started, WASD controls')
