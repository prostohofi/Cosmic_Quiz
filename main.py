"""Игра - викторина."""

import random

import arcade

import config
import views.how_to_play_view as howtoplay
from buttons import Button
from views import general_view, knowledge_view, menu_view, quiz_view, statistics_view

"""
TODO:
    Изменить картинки во вьюшке "Как играть"

    Сделать когда конец слайдов, сделать кнопки отличающимися.

    В статисктике общей:
    1) Пронумеровать строки
    2) Подписать все цифры

    Добавить кнопки:
    Включить и выключить музыку

    Изменить стиль кнопок(пример: элепс)
"""


class MyWindow(arcade.Window):
    """Класс собственного окна."""

    def __init__(self) -> None:
        """Инициализация класса."""
        super().__init__(fullscreen=True)
        self.sound = arcade.load_sound(config.SOUNDS_DIR / "PPK - Resurection.mp3")
        self.sound.play(0.2, loop=True)
        self.right_answers = 0
        self.wrong_answers = 0
        self.timer = 0
        self.count_bg = 17

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
        view = knowledge_view.KnowledgeView()
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
        self.texture = str(random.randint(1, self.count_bg)) + ".jpg"
        self.bg_sprite_texture = arcade.load_texture(
            config.ASSETS_DIR / "img" / "bg_images" / self.texture,
            )
        self.bg_sprite = arcade.Sprite(
            self.bg_sprite_texture,
            center_x = self.width // 2,
            center_y = self.height * 0.6,
            scale=2,
            )
        self.sprites.append(self.bg_sprite)
        self.sprites.append(self.menu_black_sprite)
        return self.sprites

    def make_buttons(self, buttons_names_list: list) -> None:
        """Метод создания кнопок."""
        buttons = arcade.SpriteList()
        button_width = window.width * 0.15
        button_height = window.height * 0.05
        spacing_vert = window.height * 0.1
        buttons_names = buttons_names_list
        button_x = window.width / (len(buttons_names) + 1)
        for button_name in buttons_names:
            button = Button(
                button_width,
                button_height,
                button_x,
                spacing_vert,
                text_str=button_name,
                )
            buttons.append(button)
            button_x += window.width / (len(buttons_names) + 1)
        return buttons



window = MyWindow()
view = menu_view.MenuView()
window.show_view(view)
arcade.run()
