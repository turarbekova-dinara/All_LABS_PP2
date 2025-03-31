import pygame, sys
from pygame.locals import *
import random

# Pygame инициализациясы
pygame.init()

# FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Экран параметрлері
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ROAD_LEFT = 50  # Жолдың сол жақ шегі
ROAD_RIGHT = 350  # Жолдың оң жақ шегі
SPEED = 3
SCORE = 0
COINS = 0

# Шрифтер
font = pygame.font.SysFont("Verdana", 20)

# Фон
background = pygame.image.load("AnimatedStreet.png")
background_y = 0  # Фонның Y координатасы

# Экранды орнату
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")


# Жаудың классы (көлік)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/dinaraturarbekova/Documents/All_LABS_PP2-main/LAB8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)  # Төмен қарай жылжиды
        if (self.rect.top > 600):  # Егер экраннан шықса
            SCORE += 1  # Ұпай қосылады
            self.rect.top = 0  # Қайта жоғарыдан пайда болады
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Жаңа кездейсоқ орында

# Монетаның классы
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomize_coin()

    def randomize_coin(self):
        """Монетаның өлшемін және орнын кездейсоқ қояды"""
        if random.choice([True, False]):
            self.size = (50, 50)  # Үлкен монета
            self.value = 3
        else:
            self.size = (30, 30)  # Кіші монета
            self.value = 1

        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        """Монета төмен қарай сырғиды"""
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()  # Егер экраннан шықса, қайта пайда болады

    def respawn(self):
        """Монета жаңа орынға пайда болады"""
        self.randomize_coin()


# Ойыншының классы (көлік)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)  # Орталықта басталады

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > ROAD_LEFT and pressed_keys[K_LEFT]:  # Солға қозғалыс
            self.rect.move_ip(-5, 0)
        if self.rect.right < ROAD_RIGHT and pressed_keys[K_RIGHT]:  # Оңға қозғалыс
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:  # Жоғары қозғалыс
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:  # Төмен қозғалыс
            self.rect.move_ip(0, 5)


# Объекттерді жасау
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Топтар
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Ойын циклі
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Егер ойыншы жаумен соқтығысса, ойын тоқтайды
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.quit()
        sys.exit()

    # Фонды жылжыту (артқа қозғалыс эффекті)
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Ұпайларды көрсету
    scores = font.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))

    coins_text = font.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coins_text, (300, 10))

    # Жау көліктерін жылжыту
    for enemy in enemies:
        enemy.move()

    # Барлық объектілерді экранға шығару
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()  # Барлық объектілер қозғалады

    # Егер ойыншы монетаны жесе, жаңа монета пайда болады
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.value  # Монетаның өлшеміне байланысты ұпай қосу
        C1.respawn()  # Монета қайта пайда болады

        # **Монета саны белгілі бір мәнге жеткенде жылдамдықты арттыру**
        if COINS % 5 == 0:  # Әр 5 монета сайын жылдамдық артады
            SPEED += 1
            print(f"Speed increased! New SPEED: {SPEED}")  # Консольге шығару (опционалды)

    pygame.display.update()
    FramePerSec.tick(FPS)
