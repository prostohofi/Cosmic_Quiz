"""Модуль статистики."""
from pathlib import Path

import arcade

import config
from buttons import Button


class StatisticsView(arcade.View):
    """Представление статистики после викторины."""

    def __init__(self, right_answers: int, wrong_answers: int, time: str) -> None:
        """Инициализирует представление статистики:правильные и неправильные ответы."""
        super().__init__()
        self.text_obj = arcade.Text(
            f"Викторина окончена!\nверных: {right_answers}\nошибок: {
                wrong_answers}",
            self.window.width // 2,
            self.window.height // 2,
            multiline=True,
            width=500,
            anchor_x="center",
            anchor_y="center",
            align="center",
            font_size=config.FONT_SIZE_M,
        )

        self.right_answers = right_answers
        self.wrong_answers = wrong_answers
        self.time = time

        self.menu_sprites = self.window.create_dark_background()

        spacing_vert = self.window.height * 0.1
        button_width = self.window.width * 0.33
        button_height = self.window.height * 0.1
        button_x = self.window.width // 2
        button_y = (
            self.window.height // 2
            - self.text_obj.content_height // 2
            - button_height // 2
            - spacing_vert
        )
        self.menu_button = Button(
            button_width, button_height, button_x, button_y, "в меню",
        )
        self.write_statistics()

    def write_statistics(self) -> None:
        """Метод записи статистики в файл."""
        file_wrapper = Path.open(
            config.BASE_DIR / "statistics.txt",
            mode="a",
            encoding="utf-8",
            )
        text = f"{self.right_answers}, {self.wrong_answers}, {self.time}\n"
        file_wrapper.write(text)

    def on_draw(self) -> None:
        """Метод отрисовки."""
        self.clear()
        self.menu_sprites.draw()
        self.text_obj.draw()
        self.menu_button.draw()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопки 'в меню'."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return

        if self.menu_button.collides_with_point((x, y)):
            self.window.show_menu_view()
