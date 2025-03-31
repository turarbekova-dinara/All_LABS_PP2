import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
WHITE, GREEN, RED, YELLOW, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 0, 0)
SPEED = 10

# Экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Arial", 20)

# Змейка и еда
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
level, score = 1, 0

# Функция генерации еды в безопасном месте
def generate_food():
    while True:
        food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if food not in snake:
            return food

food = generate_food()

# Переменные для дополнительной еды (жёлтой)
special_food = None
special_food_timer = None  # Таймер для исчезновения еды
next_special_food_time = random.randint(5, 15) * 1000  # Через сколько мс появится еда

# Часы
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Время старта игры

# Игровой цикл
running = True
while running:
    clock.tick(7 + level * 2)  # Скорость игры

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление змейкой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Проверка на выход за границы (телепорт с другой стороны)
    if new_head[0] < 0:
        new_head = (WIDTH - CELL_SIZE, new_head[1])
    elif new_head[0] >= WIDTH:
        new_head = (0, new_head[1])
    if new_head[1] < 0:
        new_head = (new_head[0], HEIGHT - CELL_SIZE)
    elif new_head[1] >= HEIGHT:
        new_head = (new_head[0], 0)

    # Проверка на столкновение с собой
    if new_head in snake:
        running = False
        continue

    snake.insert(0, new_head)

    # Проверка на съедение обычной еды (красной)
    if new_head == food:
        score += 1
        food = generate_food()
        if score % 4 == 0:
            level += 1  # Повышение уровня каждые 4 еды
    else:
        snake.pop()

    # Проверка появления дополнительной еды (жёлтой)
    current_time = pygame.time.get_ticks()
    if special_food is None and current_time - start_time >= next_special_food_time:
        special_food = generate_food()
        special_food_timer = current_time  # Засекаем время появления
        next_special_food_time = current_time + random.randint(5, 15) * 1000  # Следующее появление

    # Проверка на съедение специальной еды
    if special_food and new_head == special_food:
        score += 3  # Специальная еда даёт 3 очка
        special_food = None  # Еда исчезает
        next_special_food_time = current_time + random.randint(5, 15) * 1000  # Следующее появление

    # Проверка на исчезновение специальной еды через 7 секунд
    if special_food and current_time - special_food_timer > 7000:
        special_food = None  # Удаляем еду

    # Отрисовка
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))  # Обычная еда
    if special_food:
        pygame.draw.rect(screen, YELLOW, (*special_food, CELL_SIZE, CELL_SIZE))  # Специальная еда

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Отображение счёта и уровня
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
