import pygame
from settings import *

class Goal(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)

goal_sprite1 = Goal((50, screen_height // 2), "graphics/background/leftgoal.png")  # Example position for the first goal
goal_sprite2 = Goal((screen_width - 50, screen_height // 2), "graphics/background/rightgoal.png")  # Example position for the second goal
