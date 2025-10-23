import pygame, sys
from game.ball import Ball
from game.paddle import Paddle

pygame.init()
pygame.mixer.init()

# Screen
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Colors & font
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 50)

# Sounds
paddle_sound = pygame.mixer.Sound("sounds/paddle.wav")
wall_sound   = pygame.mixer.Sound("sounds/wall.wav")
score_sound  = pygame.mixer.Sound("sounds/score.wav")

def draw_window(paddle_left, paddle_right, ball, left_score, right_score):
    WIN.fill(BLACK)
    paddle_left.draw(WIN, WHITE)
    paddle_right.draw(WIN, WHITE)
    ball.draw(WIN, WHITE)
    score_text = font.render(f"{left_score} - {right_score}", True, WHITE)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))
    pygame.display.update()

def game_over_and_menu(winner_text):
    """Show winner + replay options. Return new WINNING_SCORE or None to exit."""
    WIN.fill(BLACK)

    title = font.render(f"{winner_text} Wins!", True, WHITE)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 120))

    over  = font.render("Game Over", True, WHITE)
    WIN.blit(over, (WIDTH//2 - over.get_width()//2, HEIGHT//2 - 70))

    opt1 = font.render("Press 3 for Best of 3", True, WHITE)
    opt2 = font.render("Press 5 for Best of 5", True, WHITE)
    opt3 = font.render("Press 7 for Best of 7", True, WHITE)
    opt4 = font.render("Press ESC to Exit",   True, WHITE)

    WIN.blit(opt1, (WIDTH//2 - opt1.get_width()//2, HEIGHT//2 + 10))
    WIN.blit(opt2, (WIDTH//2 - opt2.get_width()//2, HEIGHT//2 + 60))
    WIN.blit(opt3, (WIDTH//2 - opt3.get_width()//2, HEIGHT//2 + 110))
    WIN.blit(opt4, (WIDTH//2 - opt4.get_width()//2, HEIGHT//2 + 160))
    pygame.display.update()

    # Wait for selection
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_3:
                    return 2   # best of 3 -> first to 2
                if event.key == pygame.K_5:
                    return 3   # best of 5 -> first to 3
                if event.key == pygame.K_7:
                    return 4   # best of 7 -> first to 4

def main(WINNING_SCORE=5):
    clock = pygame.time.Clock()

    paddle_left  = Paddle(30,             HEIGHT//2 - 60, 20, 120, 6)
    paddle_right = Paddle(WIDTH - 50,     HEIGHT//2 - 60, 20, 120, 6)
    ball = Ball(WIDTH//2 - 10, HEIGHT//2 - 10, 10, 6, paddle_sound, wall_sound)

    left_score = 0
    right_score = 0

    run = True
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Controls & AI
        paddle_left.move(pygame.K_w, pygame.K_s, HEIGHT)
        paddle_right.ai_move(ball, HEIGHT)

        # Ball
        ball.move(HEIGHT)
        ball.check_collision(paddle_left)
        ball.check_collision(paddle_right)

        # Scoring
        if ball.rect.left <= 0:
            right_score += 1
            score_sound.play()
            ball.reset(WIDTH, HEIGHT)
        elif ball.rect.right >= WIDTH:
            left_score += 1
            score_sound.play()
            ball.reset(WIDTH, HEIGHT)

        # Draw
        draw_window(paddle_left, paddle_right, ball, left_score, right_score)

        # Game Over
        if left_score == WINNING_SCORE:
            return game_over_and_menu("Player")
        if right_score == WINNING_SCORE:
            return game_over_and_menu("AI")

    return None  # window closed

if __name__ == "__main__":
    target = 5  # default first-to score
    while True:
        new_target = main(target)
        if new_target is None:
            break
        target = new_target  # update to 2/3/4 for best-of 3/5/7
    pygame.quit()
    sys.exit()
