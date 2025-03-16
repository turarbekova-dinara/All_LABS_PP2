import pygame # type: ignore

# Инициализация
pygame.init()

# Экран параметрлері
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Түстер
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Шардың параметрлері
radius = 25
x, y = WIDTH // 2, HEIGHT // 2
step = 20

# Ойын циклі
running = True
while running:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Пернетақта арқылы басқару
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y - radius - step >= 0:
        y -= step
    if keys[pygame.K_DOWN] and y + radius + step <= HEIGHT:
        y += step
    if keys[pygame.K_LEFT] and x - radius - step >= 0:
        x -= step
    if keys[pygame.K_RIGHT] and x + radius + step <= WIDTH:
        x += step

    # Экранды жаңарту
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.update()

pygame.quit()
