import pygame

class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up, down, screen_height):
        keys = pygame.key.get_pressed()
        if keys[up] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def ai_move(self, ball, screen_height):
        if self.rect.centery < ball.rect.centery and self.rect.bottom < screen_height:
            self.rect.y += self.speed
        if self.rect.centery > ball.rect.centery and self.rect.top > 0:
            self.rect.y -= self.speed

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)
