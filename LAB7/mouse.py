import pygame  # type: ignore
from math import pi, cos, sin 
import datetime

WIDTH, HEIGHT = 800, 800 
center = (WIDTH / 2, HEIGHT / 2) 
clock_radius = 400

pygame.init() 

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Digital Clock") 
clock = pygame.time.Clock() 
FPS = 60 

WHITE = (255, 255, 255)  # Ақ түс
BLACK = (0, 0, 0)
BLUE = (17, 37, 145)
F = (21, 32, 91)

# Суретті жүктеу
background = pygame.image.load("/Users/dinaraturarbekova/Documents/All_LABS_PP2-main/LAB7/img/miki.png")  # Файлдың дұрыс жолын қолдану
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Экран өлшеміне сәйкестендіру

# Мики Маустың қолының суретін жүктеу
minute_hand = pygame.image.load("/Users/dinaraturarbekova/Documents/All_LABS_PP2-main/LAB7/img/minute_hand.png")  # Файл атауын өзіңе сай өзгерту

fon = pygame.image.load("/Users/dinaraturarbekova/Documents/All_LABS_PP2-main/LAB7/img/fon.png")

def numbers (number, size, position): 
    font = pygame.font.SysFont("Arial", size, True, False) 
    text = font.render (number, True, F) 
    text_rect = text.get_rect(center=(position)) 
    screen.blit(text, text_rect) 
def polar_to_cartesian (r, theta): 
    x = r * sin (pi * theta / 180) 
    y = r * cos (pi * theta / 180) 
    return x + WIDTH / 2, -(y - HEIGHT / 2)

def main(): 
    run = True 
    while run: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 

        current_time = datetime.datetime.now() 
        second = current_time.second 
        minute = current_time.minute 
        hour = current_time.hour

        # Фонға суретті қою
        screen.blit(fon, (0, 0)) 
        screen.blit(background, (0, 0))
        pygame.draw.circle(screen, F, center, clock_radius -10, 10) 
        pygame.draw.circle(screen, BLACK, center, 12)

        for number in range(1, 13): 
            numbers(str(number), 80, polar_to_cartesian(clock_radius - 80, number * 30))

        for number in range(0, 360, 6): 
            if number % 5: 
                pygame.draw.line(screen, BLUE, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 30, number), 2) 
            else: 
                pygame.draw.line(screen, BLUE, polar_to_cartesian(clock_radius - 15, number), polar_to_cartesian(clock_radius - 35, number), 6)

        # Минут тілі (таяқ сол қалпында)
        r = 280 
        theta = (minute + second / 60) * (360 / 60) 

        offset = 15  # Таяқ пен қолды бірге жылжыту үшін түзету мәні

        end_pos = polar_to_cartesian(r - offset, theta)  # Таяқтың бас нүктесі
        pygame.draw.line(screen, BLACK, center, end_pos, 20)

        # Мики Маустың қолын қою
        hand_size = (100, 100)  # Қолдың өлшемі
        minute_hand_img = pygame.transform.scale(minute_hand, hand_size)  # Қолды кішірейту
        rotated_hand = pygame.transform.rotate(minute_hand_img, -theta)  # Бұрышқа айналдыру

        hand_rect = rotated_hand.get_rect(center=end_pos)  # Қолды таяқтың басына қою
        screen.blit(rotated_hand, hand_rect.topleft)

        r = 180  # Сағат тілі қысқалау
        theta = (hour % 12 + minute / 60) * (360 / 12)
        end_pos = polar_to_cartesian(r, theta)  
        pygame.draw.line(screen, BLACK, center, end_pos, 20)

        hand_size = (100, 100)  
        hour_hand_img = pygame.transform.scale(minute_hand, hand_size)  
        rotated_hand = pygame.transform.rotate(hour_hand_img, -theta)  
        hand_rect = rotated_hand.get_rect(center=end_pos)  
        screen.blit(rotated_hand, hand_rect.topleft)

        # Second 
        r = 340 
        theta = second * (360 / 60) 
        pygame.draw.line(screen, BLUE, center, polar_to_cartesian(r, theta), 4)

        pygame.display.update() 

        clock.tick(FPS)

    pygame.quit()

main()
