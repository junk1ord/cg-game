import pygame

pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("CG Mini Project")

walkRight = [
    pygame.image.load("gameSprites/R1.png"),
    pygame.image.load("gameSprites/R2.png"),
    pygame.image.load("gameSprites/R3.png"),
    pygame.image.load("gameSprites/R4.png"),
    pygame.image.load("gameSprites/R5.png"),
    pygame.image.load("gameSprites/R6.png"),
    pygame.image.load("gameSprites/R7.png"),
    pygame.image.load("gameSprites/R8.png"),
    pygame.image.load("gameSprites/R9.png"),
]
walkLeft = [
    pygame.image.load("gameSprites/L1.png"),
    pygame.image.load("gameSprites/L2.png"),
    pygame.image.load("gameSprites/L3.png"),
    pygame.image.load("gameSprites/L4.png"),
    pygame.image.load("gameSprites/L5.png"),
    pygame.image.load("gameSprites/L6.png"),
    pygame.image.load("gameSprites/L7.png"),
    pygame.image.load("gameSprites/L8.png"),
    pygame.image.load("gameSprites/L9.png"),
]
bg = pygame.image.load("gameSprites/bg.jpg")

char = pygame.image.load("gameSprites/standing.png")

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound

score = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.walkCount = 0
        self.standing = True
        self.health = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        # pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
        # pygame.draw.rect(win, (0,0,255), (self.hitbox[0], self.hitbox[1] - 20, 50 - ((50/10)*(10 - self.health)), 10))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont("comicsans", 100)
        text = font1.render("HIT -5", 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width() / 2), 200))
        pygame.display.update()

        i = 0
        while i < 300:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [
        pygame.image.load("gameSprites/R1E.png"),
        pygame.image.load("gameSprites/R2E.png"),
        pygame.image.load("gameSprites/R3E.png"),
        pygame.image.load("gameSprites/R4E.png"),
        pygame.image.load("gameSprites/R5E.png"),
        pygame.image.load("gameSprites/R6E.png"),
        pygame.image.load("gameSprites/R7E.png"),
        pygame.image.load("gameSprites/R8E.png"),
        pygame.image.load("gameSprites/R9E.png"),
        pygame.image.load("gameSprites/R10E.png"),
        pygame.image.load("gameSprites/R11E.png"),
    ]
    walkLeft = [
        pygame.image.load("gameSprites/L1E.png"),
        pygame.image.load("gameSprites/L2E.png"),
        pygame.image.load("gameSprites/L3E.png"),
        pygame.image.load("gameSprites/L4E.png"),
        pygame.image.load("gameSprites/L5E.png"),
        pygame.image.load("gameSprites/L6E.png"),
        pygame.image.load("gameSprites/L7E.png"),
        pygame.image.load("gameSprites/L8E.png"),
        pygame.image.load("gameSprites/L9E.png"),
        pygame.image.load("gameSprites/L10E.png"),
        pygame.image.load("gameSprites/L11E.png"),
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True
        self.right = True
        self.left = False

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
        if self.vel > 0:
            self.right = True
            self.left = False
            win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            self.right = False
            self.left = True
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        pygame.draw.rect(
            win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10)
        )
        pygame.draw.rect(
            win,
            (0, 0, 255),
            (
                self.hitbox[0],
                self.hitbox[1] - 20,
                50 - ((50 / 10) * (10 - self.health)),
                10,
            ),
        )
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False
            # print('Hit!')


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = font.render("SCORE: " + str(score), 1, (0, 0, 0))
    win.blit(text, (310, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# main loop
font = pygame.font.SysFont("timesnewroman", 30, True)

man = player(300, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450)
shootLoop = 0
bullets = []
oppBullets = []
run = True

while run:
    clock.tick(27)
    if goblin.visible == True:
        if (
            man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3]
            and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]
        ):
            if (
                man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0]
                and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]
            ):
                man.hit()
                score -= 5

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if (
            bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]
            and bullet.y + bullet.radius > goblin.hitbox[1]
        ):
            if (
                bullet.x + bullet.radius > goblin.hitbox[0]
                and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]
            ):
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(
                    round(man.x + man.width // 2),
                    round(man.y + man.height // 2),
                    6,
                    (0, 0, 0),
                    facing,
                )
            )
        shootLoop = 1

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_d] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not (man.isJump):
        if keys[pygame.K_w]:
            man.isJump = True
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()
pygame.QUIT()
