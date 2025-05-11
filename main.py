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

pygame.init()

window = pygame.display.set_mode([1080, 640])
fps = pygame.time.Clock()
background_img = pygame.image.load("images/background.jpg")
background_img = pygame.transform.scale(background_img, [1080, 640])
hero = Hero(15, 35, 50, 50, 5, "images/hero.png")
walls = [
    Wall(0, 0, 210, 30, [35, 117, 2]),
    Wall(0, 80, 130, 700, [35, 117, 2])
]
window.blit(background_img, [0, 0])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    for wall in walls:
        wall.draw(window)
    hero.update(window)
    hero.check_coordinates()
    pygame.display.flip()
    fps.tick(60)