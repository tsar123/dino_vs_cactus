# dino_game/cactus.py
# Импортируем необходимые модули
import pygame
import random
from . import utils  # Импортируем утилиты из текущего пакета


class Cactus:
    def __init__(self):
        # Инициализируем прямоугольник кактуса с заданными размерами и положением
        self.rect = pygame.Rect(utils.WIDTH, utils.HEIGHT - utils.CACTUS_HEIGHT, utils.CACTUS_WIDTH, utils.CACTUS_HEIGHT)
        
        # pygame.Rect — это класс из библиотеки Pygame, который представляет прямоугольную область. 
        # Он используется для работы с 2D-объектами, такими как спрайты, и позволяет легко управлять их положением и размерами.
        # utils.WIDTH - это значение ширины игрового окна или экрана

        # Генерируем случайную высоту кактуса в диапазоне от 20 до 60
        self.height = random.randint(20, 60)
        
        # Устанавливаем высоту прямоугольника кактуса
        self.rect.height = self.height
        
        # Устанавливаем вертикальное положение кактуса
        self.rect.y = utils.HEIGHT - self.height
        # Эта операция вычисляет вертикальную позицию нижней границы кактуса. 
        # Мы вычитаем высоту кактуса из общей высоты окна, чтобы установить его основание на уровне земли.
        
        # Масштабируем изображение кактуса до новой высоты
        self.image = pygame.transform.scale(utils.cactus_image, (utils.CACTUS_WIDTH, self.height))
        # Это функция из библиотеки Pygame, которая изменяет размер изображения. 
        # Она принимает два аргумента: изображение, которое нужно масштабировать, и кортеж, содержащий новые размеры (ширину и высоту).


    def move(self):
        # Двигаем кактус влево с заданной скоростью
        self.rect.x -= utils.SCROLL_SPEED


    def draw(self, surface):
        # Отображаем кактус на переданной поверхности
        surface.blit(self.image, self.rect)
