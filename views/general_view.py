"""Модуль общей статистики."""
from pathlib import Path

import arcade

import config
from utils import get_formated_time


class GeneralStatisticsView(arcade.View):
    """Представление общей статистики."""

    def __init__(self) -> None:
        """Инициализирует представление статистики: правильные и неправильные ответы."""
        super().__init__()
        self.content = ""
        self.number_parts_string = 3
        self.menu_sprites = self.window.create_dark_background()
        self.read()
        self.text_obj = arcade.Text(
            self.content,
            self.window.width // 2,
            self.window.height * 0.8,
            font_size=config.FONT_SIZE_S,
            multiline=True,
            width=self.window.width * 0.9,
            anchor_x="center",
            anchor_y="center",
            align="center",
        )
        self.buttons = arcade.SpriteList()
        self.buttons = self.window.make_buttons(["Меню"])

    def read(self) -> None:
        """Метод, который берёт из файла статистики текст и форматирует с иконками."""
        try:
            with Path.open(
                config.BASE_DIR / "statistics.txt",
                encoding="utf-8",
            ) as file_wrapper:
                lines = file_wrapper.readlines()
                numbered_lines = []
                for i, line in enumerate(lines, start=1):
                    rs_line = line.rstrip("\n\r")
                    if rs_line.strip():
                        parts = rs_line.split()
                        if len(parts) >= self.number_parts_string:
                            correct = parts[0]
                            incorrect = parts[1]
                            time = get_formated_time(float(parts[2]))
                            formatted_line = f"{i}. ✅{correct} ❌{incorrect} 🕔{time}"
                        else:
                            formatted_line = f"{i}. {rs_line}"
                        numbered_lines.append(formatted_line)
                    else:
                        numbered_lines.append(f"{i}. (пустая строка)")
                self.content = "\n".join(numbered_lines)
        except FileNotFoundError:
            self.content = "Файл статистики не найден"

    def on_draw(self) -> None:
        """Метод отрисовки."""
        self.clear()
        self.menu_sprites.draw()
        self.text_obj.draw()
        self.buttons.draw()
        for button in self.buttons:
            button.draw()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопок."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons:
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "Меню":
                self.window.show_menu_view()
