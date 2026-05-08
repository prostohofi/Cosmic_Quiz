"""Модуль показа меню."""

import arcade
import arcade.types

import config
from buttons import Button

FONT_SIZE = 30

class MenuView(arcade.View):
    """Представление меню."""

    def __init__(self) -> None:
        """Инициализирует представление меню."""
        super().__init__()
        self.window.background_color = arcade.color.BLACK
        self.title = arcade.Text(
            "Викторина на тему: Космос",
            self.window.width // 2,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            font_size=FONT_SIZE,
        )
        self.buttons = arcade.SpriteList()
        self.make_buttons()
        self.menu_sprites = self.window.create_dark_background()

    def make_buttons(self) -> None:
        """Метод создания кнопок."""
        button_width = self.window.width * 0.2
        button_height = self.window.height * 0.1
        spacing_hor = (self.window.width * 0.2 - button_width * 2) / 2
        spacing_vert = self.window.height * 0.1
        buttons_names = ["Выйти", "Начать", "Познать", "Как играть"]
        for button_name in buttons_names:
            button = Button(
                button_width,
                button_height,
                spacing_hor + button_width * 1.4,
                spacing_vert,
                text_str=button_name,
                )
            self.buttons.append(button)
            spacing_hor += self.window.width * 0.21

    def on_draw(self) -> None:
        """Отрисовывает спрайты и текст на экране."""
        self.clear()
        self.menu_sprites.draw()
        for button in self.buttons:
            button.draw()
        self.title.draw()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопок."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons:
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Выйти":
                arcade.exit()
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Начать":
                self.window.show_quiz_view()
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Познать":
                self.window.show_knowledge_view()
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Как играть":
                self.window.show_how_to_play_view()
