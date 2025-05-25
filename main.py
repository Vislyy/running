import pygame

class BaseSprite:
    def __init__(self, x, y, width, height, speed, texture):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, [width, height])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.texture, self.hitbox)

class Hero(BaseSprite):
    def update(self, window):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        self.draw(window)
    
    def check_coordinates(self):
        print(self.hitbox)
    
class Wall:
    def __init__(self, x, y, width, height, color):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.hitbox.x = x
        self.hitbox.y = y
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)

class Gold:
    def __init__(self, x, y, width, height, texture):
        self.texture = pygame.image.load("images/treasure.png")
        self.texture = pygame.transform.scale(self.texture, [50, 50])
        self.hitbox = self.texture.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def draw(self):
        window.blit(self.texture, self.hitbox)

class Cyborg(BaseSprite):
    def __init__(self, x, y, width, height, speed, texture, target_x, target_y):
        super().__init__(x, y, width, height, speed, texture)
        self.x = x
        self.direction = "forward"
        self.target_x = target_x
        self.target_x = target_y
    def update(self):
        if self.direction == "forward":
            self.hitbox.x += self.speed
            if self.hitbox.x >= self.target_x:
                self.direction = "backward"
        else:
            self.hitbox.x -= self.speed
            if self.hitbox.x <= self.x:
                self.direction = "forward"

pygame.init()

window = pygame.display.set_mode([1080, 640])
fps = pygame.time.Clock()
background_img = pygame.image.load("images/background.jpg")
background_img = pygame.transform.scale(background_img, [1080, 640])
hero = Hero(15, 30, 50, 50, 5, "images/hero.png")
cyborg = Cyborg(200, 200, 50, 50, 5, "images/cyborg.png", 220, 200)
walls = [
    Wall(0, 0, 250, 30, [35, 117, 2]),
    Wall(0, 90, 130, 30, [35, 117, 2]),
    Wall(130, 90, 30, 700, [35, 117, 2]),
    Wall(250, 0, 30, 550, [35, 117, 2]),
    Wall(250, 550, 200, 30, [35, 117, 2]),
    Wall(420, 0, 30, 550, [35, 117, 2])
]

pygame.mixer.init()
pygame.mixer.music.load("images/jungles.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.7)
kick_sound = pygame.mixer.Sound("images/kick.ogg")
treasure_sound = pygame.mixer.Sound("images/money.ogg")

running = True

while running:
    window.blit(background_img, [0, 0])
    for wall in walls:
        wall.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for wall in walls:
        if hero.hitbox.colliderect(wall.hitbox):
            hero.hitbox.x, hero.hitbox.y = 15, 25
            kick_sound.play()
    if hero.hitbox.colliderect(cyborg.hitbox):
        break
    hero.update(window)
    cyborg.update()
    hero.check_coordinates()
    cyborg.draw(window)
    pygame.display.flip()
    fps.tick(60)

