import pygame, sys
from settings import *
from player import Player

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/player/ball.png")
        self.rect = self.image.get_rect(center=(screen_width // 2, 650))
        self.speed = 9
        self.is_hit = False  #initially set to false, meaning the ball has not yet been hit. Once hit, this turns to true which means that line 30 is activated
        self.hit_time = None  #keeps track of time since last ball was hit.
        #self.ball_slowdown_factor = 0.99

        self.offset = (-60, -60) #reduce hitbox size by 60 pixels width and height
        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])

    def update(self): #checks if it hits any of the walls and then reverses speed to make it bounce off
        self.rect.x += self.speed
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed = -self.speed
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.hitbox.bottom > screen_height:
            self.hitbox.bottom = screen_height
            if self.rect.y + self.rect.height > screen_height:
                self.rect.y = screen_height - self.rect.height
        else:
            if self.is_hit:
                elapsed_time = pygame.time.get_ticks() - self.hit_time
                if elapsed_time < 700:  # Wait for x seconds before applying gravity
                    self.rect.y -= 5  # Move the ball up IF the elapsed time which is calculated above is below x miliseconds
                else: #only applys if the elapsed time is over x seconds, because then gravity needs to be applied
                    self.rect.y += 5  # increase y position which actually makes it go down, simulates the idea of gravity

        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])

    def draw(self, screen):
        #pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 1)
        screen.blit(self.image, self.rect)

class Goal(pygame.sprite.Sprite):
    def __init__(self, position, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=position)

"""
#got this from sample test and applied it to work for my code
        if abs(self.speed) > 0.04:
            self.speed *= self.ball_slowdown_factor
        else:
            self.speed = 0
"""

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player_sprite1 = Player((600,350), 1) #spawn point
player_sprite2 = Player((200,200), 2)

#sprite 1
player_group1 = pygame.sprite.GroupSingle()
player_group1.add(player_sprite1)

#sprite 2
player_group2 = pygame.sprite.GroupSingle()
player_group2.add(player_sprite2)

#ball
ball_sprite = Ball()
ball_group = pygame.sprite.GroupSingle()
ball_group.add(ball_sprite)

#goal
goal_sprite1 = Goal((50, 575), "graphics/background/leftgoal.png")  # Example position for the first goal
goal_sprite2 = Goal((screen_width - 50, 575), "graphics/background/rightgoal.png")  # Example position for the second goal

background_image = pygame.image.load("graphics/player/ghetto.png").convert()

#music below
pygame.mixer.music.load("sounds/music/champion.mp3")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    screen.blit(background_image, (0, 0))

    player_group1.update()
    player_group2.update()
    ball_group.update()

    # see if there r collisions between ball and players
    if pygame.Rect.colliderect(ball_sprite.hitbox, player_group1.sprite.hitbox) or \
       pygame.Rect.colliderect(ball_sprite.hitbox, player_group2.sprite.hitbox):
        ball_sprite.is_hit = True
        ball_sprite.hit_time = pygame.time.get_ticks()
        ball_sprite.speed = -ball_sprite.speed

    if pygame.Rect.colliderect(ball_sprite.hitbox, goal_sprite1.rect): # this line of code checks if the ball has entered
# the goal by comparing their rectangular shapes. If they overlap, it means the ball has scored a goal.
        # Ball entered the left goal
        print("Goal for player 1!")
        ball_sprite.rect.center = (screen_width // 2, 650)
        ball_sprite.is_hit = False
        ball_sprite.hit_time = None

    if pygame.Rect.colliderect(ball_sprite.hitbox, goal_sprite2.rect):
        # Ball entered the right goal
        print("Goal for player 2!")
        ball_sprite.rect.center = (screen_width // 2, 650) #just reset ball to center
        ball_sprite.is_hit = False
        ball_sprite.hit_time = None

    player_group1.draw(screen) #draws all sprites
    player_group2.draw(screen)
    player_group1.sprite.draw(screen)
    player_group2.sprite.draw(screen)
    ball_group.draw(screen)
    ball_group.sprite.draw(screen)
    screen.blit(goal_sprite1.image, goal_sprite1.rect)  # Draw the first goal
    screen.blit(goal_sprite2.image, goal_sprite2.rect)  # Draw the second goal


    pygame.display.update()
    clock.tick(fps)
