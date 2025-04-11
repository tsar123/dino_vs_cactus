# Импортируем необходимые модули
import pygame  # Импортируем библиотеку Pygame для работы с графикой и звуком
from . import utils  # Импортируем утилиты из текущего пакета, которые содержат общие константы и функции
from .utils import DINO_WIDTH, DINO_HEIGHT  # Импортируем ширину и высоту динозавра из модуля utils


class Dino:
    def __init__(self):
        # Инициализируем прямоугольник, представляющий динозавра, с заданными размерами и положением
        self.rect = pygame.Rect(50, utils.HEIGHT - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)
        
        # Переменная, указывающая, находится ли динозавр в прыжке
        self.is_jumping = False
        
        # Счетчик для отслеживания силы прыжка
        self.jump_count = utils.JUMP_STRENGTH  # Инициализируем счетчик прыжка значением, определенным в utils

    def jump(self):
        # Метод для обработки прыжка динозавра
        if self.is_jumping:  # Проверяем, находится ли динозавр в прыжке
            if self.jump_count >= -utils.JUMP_STRENGTH:  # Проверяем, не достиг ли счетчик нижней границы прыжка
                if self.jump_count >= 0:
                    neg = 1
                else:
                    neg = -1
                # Определяем направление движения (вверх или вниз)
                
                # Обновляем вертикальную позицию динозавра в зависимости от силы прыжка
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                
                # Уменьшаем счетчик прыжка
                self.jump_count -= 1

                # Проверяем, не вышел ли динозавр за верхнюю границу экрана
                if self.rect.y < 0:
                    self.rect.y = 0  # Устанавливаем позицию динозавра на верхней границе экрана
            else:
                # Если прыжок завершен
                self.is_jumping = False  # Устанавливаем флаг, что динозавр больше не прыгает
                self.jump_count = utils.JUMP_STRENGTH  # Сбрасываем счетчик прыжка
                self.rect.y = utils.HEIGHT - DINO_HEIGHT  # Устанавливаем позицию динозавра на уровне земли

    def draw(self, surface):
        # Метод для рисования динозавра на переданной поверхности
        surface.blit(utils.dino_image, self.rect)  # Отображаем изображение динозавра в его прямоугольнике