"""Игра - викторина."""

import arcade

import config
import views.how_to_play_view as howtoplay
from views import general_view, knowledge_view, menu_view, quiz_view, statistics_view

"""
TODO:
    Добавить картинки в викторину.

    Изменить расположение текста и картинки во вьюшке
    "Познать" (Карнтинка слева, а справа текст).

    Изменить расположение текста и картинки во вьюшке
    викторины (Картинка слева, а справа текст).

    Сделать для всех вьюшек 1 метод создания кнопок и нажатия кнопок мыши
    (кроме вьюшки викторины)

    Изменить картинки во вьюшке "Как играть"

    Сделать количество слайдов во вьюхе познания.

    Сделать когда конец слайдов, сделать кнопки отличающимися.

    Сделать разные фоны.

    В статисктике общей:
    1) Пронумеровать строки
    2) Подписать все цифры
    3) добавить фон

    Добавить кнопки:
    Включить и выключить музыку
"""


class MyWindow(arcade.Window):
    """Класс собственного окна."""

    def __init__(self) -> None:
        """Диспетчер представлений."""
        super().__init__(fullscreen=True)
        self.sound = arcade.load_sound(config.SOUNDS_DIR / "PPK - Resurection.mp3")
        self.sound.play(0.2, loop=True)
        self.right_answers = 0
        self.wrong_answers = 0
        self.timer = 0

    def show_menu_view(self) -> None:
        """Метод показа меню."""
        view = menu_view.MenuView()
        self.show_view(view)

    def show_statistic_view(self) -> None:
        """Метод показа статистики."""
        view = statistics_view.StatisticsView(
            self.right_answers,
            self.wrong_answers,
            self.time,
            )
        self.show_view(view)

    def show_quiz_view(self) -> None:
        """Метод показа викторины."""
        view = quiz_view.QuizView(self)
        self.show_view(view)

    def show_knowledge_view(self) -> None:
        """Метод показа познавания."""
        view = knowledge_view.TeachView()
        self.show_view(view)

    def show_how_to_play_view(self) -> None:
        """Метод показа как играть."""
        view = howtoplay.HowToPlay()
        self.show_view(view)

    def show_general_view(self) -> None:
        """Метод показа как играть."""
        view = general_view.GeneralStatisticsView()
        self.show_view(view)

    def create_dark_background(self) -> arcade.sprite_list:
        """Метод создания тёмного заднего фона."""
        self.sprites = arcade.SpriteList()

        self.menu_black_sprite = arcade.SpriteSolidColor(
            self.width,
            self.height,
            center_x = self.width // 2,
            center_y = self.height * 0.5,
            color = arcade.types.Color(0, 0, 0, 200),
            )

        self.menu_sprite_texture = arcade.load_texture(
            config.ASSETS_DIR / "img" / "menu.png",
            )
        self.menu_sprite = arcade.Sprite(
            self.menu_sprite_texture,
            center_x = self.width // 2,
            center_y = self.height * 0.6,
            )
        self.sprites.append(self.menu_sprite)
        self.sprites.append(self.menu_black_sprite)
        return self.sprites


window = MyWindow()
view = menu_view.MenuView()
window.show_view(view)
arcade.run()
