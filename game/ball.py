import pygame
import random

class Ball:
    def __init__(self, x, y, radius, speed, paddle_sound=None, wall_sound=None):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.speed = speed
        self.speed_x = speed * random.choice((1, -1))
        self.speed_y = speed * random.choice((1, -1))
        self.paddle_sound = paddle_sound
        self.wall_sound = wall_sound

    def move(self, screen_height):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off top / bottom
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.speed_y *= -1
            if self.wall_sound:
                self.wall_sound.play()

    def reset(self, screen_width, screen_height):
        self.rect.center = (screen_width // 2, screen_height // 2)
        # re-randomize direction
        self.speed_x = self.speed * random.choice((1, -1))
        self.speed_y = self.speed * random.choice((1, -1))

    def draw(self, screen, color):
        pygame.draw.ellipse(screen, color, self.rect)

    def check_collision(self, paddle):
        """Reverse X velocity on overlap and apply angled bounce."""
        if self.rect.colliderect(paddle.rect):
            # snap to paddle edge to avoid tunneling/sticking
            if self.speed_x < 0:  # moving left
                self.rect.left = paddle.rect.right
            else:                 # moving right
                self.rect.right = paddle.rect.left

            # bounce
            self.speed_x *= -1

            # angle based on where it hit the paddle (-1..+1)
            hit_pos = (self.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
            self.speed_y = self.speed * hit_pos

            if self.paddle_sound:
                self.paddle_sound.play()
