# Импортируем необходимые модули
import pygame  # Импортируем библиотеку Pygame для работы с графикой и звуком
import random  # Импортируем модуль random для генерации случайных чисел
from . import dino, cactus, utils  # Импортируем классы Dino и Cactus, а также утилиты из текущего пакета


def main():
    pygame.init()  # Инициализация всех модулей Pygame, необходимых для работы игры
    screen = pygame.display.set_mode((utils.WIDTH, utils.HEIGHT))  # Устанавливаем размеры окна игры
    pygame.display.set_caption("Динозавр против кактусов")  # Устанавливаем заголовок окна игры
    dino_obj = dino.Dino()  # Создаем экземпляр класса Dino, представляющий игрока
    cacti = []  # Создаем пустой список для хранения кактусов
    score = 0  # Инициализируем счет игрока
    font = pygame.font.Font(None, 36)  # Создаем объект шрифта для отображения текста счета
    clock = pygame.time.Clock()  # Создаем объект Clock для управления частотой кадров

    run = True  # Переменная для управления основным циклом игры
    while run:  # Основной цикл игры
        clock.tick(30)  # Ограничиваем количество кадров в секунду до 30
        screen.fill(utils.WHITE)  # Заполняем экран белым цветом

        for event in pygame.event.get():  # Обрабатываем события в игре
            if event.type == pygame.QUIT:  # Если событие - закрытие окна
                run = False  # Выходим из основного цикла
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_SPACE and not dino_obj.is_jumping:  # Если нажата пробел и динозавр не прыгает
                    dino_obj.is_jumping = True  # Начинаем прыжок

        dino_obj.jump()  # Обновляем состояние прыжка динозавра
        dino_obj.draw(screen)  # Рисуем динозавра на экране

        # Генерация кактусов с вероятностью 1 из 60
        if random.randint(1, 60) == 1:  # Генерируем случайное число от 1 до 60
            cacti.append(cactus.Cactus())  # Если число равно 1, добавляем новый кактус в список

        for cactus_obj in cacti:  # Проходим по всем кактусам в списке
            cactus_obj.move()  # Двигаем кактус влево
            cactus_obj.draw(screen)  # Рисуем кактус на экране

            # Проверка на столкновение между динозавром и кактусом
            if dino_obj.rect.colliderect(cactus_obj.rect):  # Если прямоугольники пересекаются
                print("Игра окончена! Вы столкнулись с кактусом.")  # Выводим сообщение о конце игры
                run = False  # Выходим из основного цикла

        # Удаление кактусов, которые вышли за пределы экрана
        cacti = [cactus_obj for cactus_obj in cacti if cactus_obj.rect.x > -utils.CACTUS_WIDTH]  # Оставляем только видимые кактусы

        # Увеличение счета
        score += utils.SCROLL_SPEED  # Увеличиваем счет на скорость движения кактусов

        # Отображение счета на экране
        score_text = font.render(f"Счет: {score}", True, utils.BLACK)  # Создаем текст для отображения счета
        screen.blit(score_text, (utils.WIDTH - 150, 10))  # Рисуем текст счета в верхнем правом углу экрана

        pygame.display.flip()  # Обновляем экран, чтобы отобразить все изменения

    pygame.quit()  # Завершаем работу Pygame