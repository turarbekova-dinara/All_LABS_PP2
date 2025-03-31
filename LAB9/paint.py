'''
P → pen,
E → eraser, 
R → rect, 
C → circle,  
1 - red, 2 - green, 3 - blue, 4 - black
'''
''''
S → Квадрат, 
T → Равносторонний треугольник, 
Y → Прямоугольный треугольник, 
D → Ромб
'''

import pygame

pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE, BLACK, RED, GREEN, BLUE = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)

# Создаем экран
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")
screen.fill(WHITE)

# Переменные состояния
painting = False
last_pos = None
color = BLACK
mode = "pen"  # Режим: pen, rect, square, triangle, rhombus, eraser
start_pos = None
eraser_size = 10  # Размер ластика

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши
                painting = True
                last_pos = event.pos
                start_pos = event.pos
            
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Отпускаем кнопку мыши
                painting = False
                end_pos = event.pos

                # Прямоугольник
                if mode == "rect":
                    pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 2)

                # Квадрат (равные стороны)
                elif mode == "square":
                    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], size, size), 2)

                elif mode == "circle":
                    end_pos = event.pos
                    radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2) ** 0.5)
                    pygame.draw.circle(screen, color, start_pos, radius, 2)

                # Равносторонний треугольник
                elif mode == "triangle":
                    height = (3 ** 0.5 / 2) * abs(end_pos[0] - start_pos[0])
                    pygame.draw.polygon(screen, color, [(start_pos[0], start_pos[1] + height), 
                                                         (start_pos[0] + (end_pos[0] - start_pos[0]) // 2, start_pos[1]), 
                                                         (start_pos[0] + (end_pos[0] - start_pos[0]), start_pos[1] + height)], 2)

                # Прямоугольный треугольник
                elif mode == "right_triangle":
                    pygame.draw.polygon(screen, color, [start_pos, (start_pos[0], end_pos[1]), (end_pos[0], end_pos[1])], 2)

                # Ромб
                elif mode == "rhombus":
                    dx = (end_pos[0] - start_pos[0]) // 2
                    dy = (end_pos[1] - start_pos[1]) // 2
                    pygame.draw.polygon(screen, color, [(start_pos[0] + dx, start_pos[1]), 
                                                         (end_pos[0], start_pos[1] + dy), 
                                                         (start_pos[0] + dx, end_pos[1]), 
                                                         (start_pos[0], start_pos[1] + dy)], 2)
            
        elif event.type == pygame.MOUSEMOTION:
            if painting:
                if mode == "pen":
                    pygame.draw.line(screen, color, last_pos, event.pos, 3)
                    last_pos = event.pos
                elif mode == "eraser":
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, eraser_size)
                    last_pos = event.pos
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "triangle"
            elif event.key == pygame.K_y:
                mode = "right_triangle"
            elif event.key == pygame.K_d:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                color = RED
            elif event.key == pygame.K_2:
                color = GREEN
            elif event.key == pygame.K_3:
                color = BLUE
            elif event.key == pygame.K_4:
                color = BLACK
            elif event.key == pygame.K_LEFTBRACKET:
                eraser_size = max(5, eraser_size - 5)
            elif event.key == pygame.K_RIGHTBRACKET:
                eraser_size += 5
    
    pygame.display.flip()
    
pygame.quit()
