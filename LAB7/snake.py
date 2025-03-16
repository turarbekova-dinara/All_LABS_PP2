import pygame # type: ignore
import time
import random

#Түстер
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Терезе өлшемдері
width = 600
height = 400

# Жылдамдық
snake_block = 10
snake_speed = 7

pygame.init()

# Ойын терезесі
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Құрт ойыны")

# 🎨 Фонды жүктеу
try:
    background = pygame.image.load("fon.jpg")  # Файл атауын тексер!
    background = pygame.transform.scale(background, (width, height))  # Экранға сай өзгерту
except pygame.error as e:
    print("Сурет жүктеу қатесі:", e)
    exit()  # Бағдарламаны тоқтату

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [x, y])

def game_loop():
    game_over = False
    game_close = False

    x, y = width // 2, height // 2
    x_change, y_change = 0, 0
    snake_body = []
    length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            win.fill(black)
            message("Ойын аяқталды! Қайта бастау үшін Q, шығу үшін C басыңыз", white, 50, height // 2)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_loop()
                    if event.key == pygame.K_c:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width:
            x = 0  # Оң жақ шеттен шықса, сол жақтан кіреді
        elif x < 0:
            x = width - snake_block  # Сол жақ шеттен шықса, оң жақтан кіреді

        if y >= height:
            y = 0  # Төменгі жақ шеттен шықса, жоғарыдан кіреді
        elif y < 0:
            y = height - snake_block  # Жоғары жақ шеттен шықса, төменнен кіреді


        x += x_change
        y += y_change
        
        # 🎨 Фонды экранға шығару (win.fill(black) орнына)
        win.blit(background, (0, 0))

        # Тамақты салу
        pygame.draw.circle(win, red, (food_x + snake_block // 2, food_y + snake_block // 2), snake_block // 2)

        snake_head = [x, y]
        snake_body.append(snake_head)
        if len(snake_body) > length:
            del snake_body[0]

        for segment in snake_body[:-1]:
            if segment == snake_head:
                game_close = True

        for part in snake_body:
            pygame.draw.rect(win, blue, [part[0], part[1], snake_block, snake_block])

        pygame.display.update()

        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()

game_loop()