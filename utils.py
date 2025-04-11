# dino_game/utils.py
import pygame

# Константы
WIDTH, HEIGHT = 800, 400
DINO_WIDTH, DINO_HEIGHT = 40, 40
CACTUS_WIDTH, CACTUS_HEIGHT = 20, 60
GRAVITY = 1
JUMP_STRENGTH = 10
SCROLL_SPEED = 5

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
dino_image = pygame.image.load('dino.png')
dino_image = pygame.transform.scale(dino_image, (DINO_WIDTH, DINO_HEIGHT))
cactus_image = pygame.image.load('cactus.png')
cactus_image = pygame.transform.scale(cactus_image, (CACTUS_WIDTH, CACTUS_HEIGHT))
