import pygame
from settings import *
import random


class Player(pygame.sprite.Sprite): #gives the player attrivutes
    def __init__(self, pos, player_number):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 4
        self.jump_speed = -4
        self.jump_sound = pygame.mixer.Sound("sounds/effects/jump.wav")
        self.player_number = player_number
        if self.player_number == 1:
            self.image = pygame.image.load("graphics/player/bad_sprite.png")
        elif self.player_number == 2:
            self.image = pygame.image.load("graphics/player/happy_sprite.png")
        self.offset = (-80, -50)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])


#new method. create keys for player
    def get_input(self):
        keys = pygame.key.get_pressed()
        if self.player_number == 1:
            if keys[pygame.K_RIGHT] and self.hitbox.x < 950:
                self.direction.x = 1
            elif keys[pygame.K_LEFT] and self.hitbox.x > 40:
                self.direction.x = -1
            else:
                self.direction.x = 0
            if keys[pygame.K_UP]:
                self.jump()
        elif self.player_number == 2:
            if keys[pygame.K_d] and self.hitbox.x < 950:
                self.direction.x = 1
            elif keys[pygame.K_a] and self.hitbox.x > 40:
                self.direction.x = -1
            elif keys[pygame.K_w]:
                self.jump()
            else:
                self.direction.x = 0

    def jump(self):
        self.direction.y = self.jump_speed
        pygame.mixer.Sound.play(self.jump_sound)

    def vertical_movement_collision(self): #gravity
        self.apply_gravity()
        if self.hitbox.top < 0:
            self.hitbox.top = 0
            self.direction.y = 0

    def apply_gravity(self):
        self.direction.y += gravity
        self.hitbox.y += self.direction.y
        if self.hitbox.bottom > 700:
            self.hitbox.bottom = 700

    def update(self):
        self.get_input()
        self.hitbox.x += self.direction.x * self.speed
        self.vertical_movement_collision()
        self.rect = self.hitbox.inflate(self.offset[0] * -1, self.offset[1] * -1)
        self.rect.y -= 15

    def draw (self, screen):
        #Wpygame.draw.rect(screen, (0, 255, 0), self.hitbox, 1)
        screen.blit(self.image, self.rect)



