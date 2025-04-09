#mikel prodject
import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Mini Mario Style Game")

# ============================
# Step 2: Define Colors
# ============================
WHITE = (255, 255, 255)
BLUE = (66, 135, 245)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# ============================
# Step 3: Classes
# ============================

class Player:
    def __init__(self, x, y):
        super().__init__() # if contrals the data in data object. Good to have
        self.image =pygame.Surface((50,50))
        self.attack_cooldown = 0
        self.width = 40
        self.height = 60
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.vel = [0, 0]
        self.speed = 7
        self.jump_power = -20
        self.gravity = 1
        self.on_ground = False
        # self.flip = flip

    def handle_input(self, keys):
        if keys[pygame.K_a]:
            self.vel[0] = -self.speed
        elif keys[pygame.K_d]:
            self.vel[0] = self.speed
        else:
            self.vel[0] = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel[1] = self.jump_power
            self.on_ground = False
        elif keys[pygame.K_e]:
            self.attack=True
      
    def apply_physics(self, platforms):
        self.vel[1] += self.gravity
        self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]

        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel[1] > 0 and self.rect.bottom <= plat.top + self.vel[1]:
                    self.rect.bottom = plat.top
                    self.vel[1] = 0
                    self.on_ground = True

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, BLUE, (self.rect.x - scroll_x, self.rect.y, self.width, self.height))

    def attack(self):
        if self.vel[0] >= 0:
            attack_rect = pygame.Rect(self.rect.right, self.rect.y + 10, 40, self.height -20)
        else: 
            attack_rect = pygame.Rect(self.rect.left - 40 , self.rect.y + 10, 40, self.height -20)
        return attack_rect
    

class Enemy:
    def __init__(self, x, y, width=40, height=40):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface, scroll_x):
        pygame.draw.rect(surface, RED, (self.rect.x - scroll_x, self.rect.y, self.rect.width, self.rect.height))

# ============================
# Step 4: Platforms
# ============================
platforms = [
    pygame.Rect(0, HEIGHT - 40, 2000, 40),
    pygame.Rect(300, HEIGHT - 150, 100, 20),
    pygame.Rect(500, HEIGHT - 250, 100, 20),
    pygame.Rect(750, HEIGHT - 180, 150, 20),
    pygame.Rect(1000, HEIGHT - 300, 100, 20),
    ]

# ============================
# Step 5: Create Player and Enemies
# ============================
player = Player(100, HEIGHT - 150)
enemies = [Enemy(600, HEIGHT - 100), Enemy(1100, HEIGHT - 340)]

# ============================
# Step 6: Game Loop
# ============================
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    # ============================
    # Step 7: Event Handling
    # ============================
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ============================
    # Step 8: Input
    # ============================
    keys = pygame.key.get_pressed()
    player.handle_input(keys)

    attack_rect = ''
    if keys[pygame.K_e]:
        attack_rect = player.attack()

    # ============================
    # Step 9: Physics
    # ============================
    player.apply_physics(platforms)

    # ============================
    # Step 10: Enemy Collision
    # ============================
    for enemy in enemies[:]:
        if player.rect.colliderect(enemy.rect):
            if player.vel[1] > 0 and player.rect.bottom <= enemy.rect.top + player.vel[1]:
                enemies.remove(enemy)
                player.vel[1] = player.jump_power // 2  # Bounce
       
        if attack_rect:
            for enemy in enemies[:]:
                if attack_rect.colliderect(enemy.rect):
                    enemies.remove()  
    # ============================
    # Step 11: Camera Scroll
    # ============================
    scroll_x = player.rect.x - WIDTH // 2

    # ============================
    # Step 12: Drawing
    # ============================
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, (plat.x - scroll_x, plat.y, plat.width, plat.height))

    if attack_rect:
        pygame.draw.rect(screen, (0,0,0),(attack_rect.x -scroll_x, attack_rect.y, attack_rect.width, attack_rect.height),2)

    for enemy in enemies:
        enemy.draw(screen, scroll_x)

    player.draw(screen, scroll_x)

    pygame.display.flip()