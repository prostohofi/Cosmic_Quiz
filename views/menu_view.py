"""Модуль показа меню."""

import arcade

import config


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
            font_size=config.FONT_SIZE_S,
        )
        self.buttons = self.window.make_buttons(
            ["Выйти",
             "Начать",
             "Познать",
             "Как играть",
             "Статистика",
             ])
        self.menu_sprites = self.window.create_dark_background()

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
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Выйти":
                arcade.exit()
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Начать":
                self.window.show_quiz_view()
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Познать":
                self.window.show_knowledge_view()
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Как играть":
                self.window.show_how_to_play_view()
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Статистика":
                self.window.show_general_view()
