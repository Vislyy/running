import pygame

pygame.init()

window = pygame.display.set_mode([1080, 640])
fps = pygame.time.Clock()
background_img = pygame.image.load("images/background.png")
background_img = pygame.transform.scale(background_img, [1080, 640])
text = pygame.font.Font(None, 30).render("Text", True, [0, 0, 0])
class Player:
    def __init__(self, texture_path):
        self.x, self.y = 120, 60
        self.texture_size = [50, 50]
        self.texture_path = texture_path
        self.texture_load = pygame.image.load(f"images/{self.texture_path}")
        self.texture = pygame.transform.scale(self.texture_load, self.texture_size)

    def draw(self):
        window.blit(self.texture, [self.x, self.y])
        if self.x >= 1040:
            self.x = 1040
        if self.x <= 0:
            self.x = 0
        if self.y >= 600:
            self.y = 600
        if self.y <= 0:
            self.y = 0

running = True
player1 = Player("sprite1.png")
player2 = Player("sprite2.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player1.x += 5
    if keys[pygame.K_a]:
        player1.x -= 5
    if keys[pygame.K_w]:
        player1.y -= 5
    if keys[pygame.K_s]:
        player1.y += 5
    if keys[pygame.K_RIGHT]:
        player2.x += 5
    if keys[pygame.K_LEFT]:
        player2.x -= 5
    if keys[pygame.K_UP]:
        player2.y -= 5
    if keys[pygame.K_DOWN]:
        player2.y += 5
    window.blit(background_img, [0, 0])
    window.blit(text, [20, 20])
    player1.draw()
    player2.draw()
    print(player1.y)
    pygame.display.flip()
    fps.tick(60)