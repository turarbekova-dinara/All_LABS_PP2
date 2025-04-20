import pygame
import sys
import random
import psycopg2

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK, WHITE, GREEN, RED, ORANGE = (0, 0, 0), (255, 255, 255), (0, 255, 0), (255, 0, 0), (255, 165, 0)

snake_pos = [[100, 50], [90, 50], [80, 50]]
snake_speed = [10, 0]
food = {'pos': [0, 0], 'weight': 1, 'spawn_time': 0}
food_spawn = True
score = 0
level = 1
food_counter = 0
paused = False

walls = {
    2: [[200, y] for y in range(100, 300, 10)],
    3: [[x, 200] for x in range(100, 500, 10)],
}

fps = pygame.time.Clock()

# Database functions
def connect_db():
    return psycopg2.connect(dbname='lab10', user='postgres', password='181124', host='localhost', port='5432')

def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    if user:
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    cur.close()
    conn.close()
    return user_id

def get_last_progress(user_id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT score, level FROM user_scores WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result if result else (0, 1)

def save_progress(user_id, score, level):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()

# Game logic
def check_collision(pos):
    if pos[0] < 0 or pos[0] > SCREEN_WIDTH - 10 or pos[1] < 0 or pos[1] > SCREEN_HEIGHT - 10:
        return True
    if pos in snake_pos[1:]:
        return True
    if level in walls:
        if pos in walls[level]:
            return True
    return False

def get_random_food():
    global food_counter
    while True:
        pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        if pos not in snake_pos and (level not in walls or pos not in walls[level]):
            weight = 2 if food_counter >= 2 else 1
            food_counter = 0 if weight == 2 else food_counter + 1
            return {'pos': pos, 'weight': weight, 'spawn_time': pygame.time.get_ticks()}

# --- Main ---
player_name = input("Enter your name: ").strip()
player_id = get_or_create_user(player_name)
score, level = get_last_progress(player_id)
print(f"Welcome back, {player_name}! Continuing from Level {level} with score {score}.")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_progress(player_id, score, level)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_speed[1] == 0:
                    snake_speed = [0, -10]
                elif event.key == pygame.K_DOWN and snake_speed[1] == 0:
                    snake_speed = [0, 10]
                elif event.key == pygame.K_LEFT and snake_speed[0] == 0:
                    snake_speed = [-10, 0]
                elif event.key == pygame.K_RIGHT and snake_speed[0] == 0:
                    snake_speed = [10, 0]
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_progress(player_id, score, level)

        if not paused:
            snake_pos.insert(0, [snake_pos[0][0] + snake_speed[0], snake_pos[0][1] + snake_speed[1]])
            if check_collision(snake_pos[0]):
                save_progress(player_id, score, level)
                pygame.quit()
                sys.exit()

            if snake_pos[0] == food['pos']:
                score += food['weight']
                if score % 5 == 0:
                    level += 1
                food_spawn = True
            else:
                snake_pos.pop()

            if food_spawn:
                food = get_random_food()
                food_spawn = False

            if pygame.time.get_ticks() - food['spawn_time'] > 10000:
                food_spawn = True

        screen.fill(BLACK)
        for pos in snake_pos:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

        food_color = RED if food['weight'] == 1 else ORANGE
        pygame.draw.rect(screen, food_color, pygame.Rect(food['pos'][0], food['pos'][1], 10, 10))

        if level in walls:
            for block in walls[level]:
                pygame.draw.rect(screen, WHITE, pygame.Rect(block[0], block[1], 10, 10))

        font = pygame.font.SysFont('arial', 20)
        screen.blit(font.render(f"Score: {score} Level: {level}", True, WHITE), [0, 0])

        if paused:
            screen.blit(font.render("Paused", True, WHITE), [SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2])

        pygame.display.flip()
        fps.tick(10 + level * 0.5)

except SystemExit:
    pygame.quit()
