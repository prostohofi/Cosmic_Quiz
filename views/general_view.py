"""Модуль общей статистики."""
import arcade

import config
from buttons import Button


class GeneralStatisticsView(arcade.View):
    """Представление  общей статистики."""

    def __init__(self) -> None:
        """Инициализирует представление статистики:правильные и неправильные ответы."""
        super().__init__()
        self.content = ""
        self.read()
        self.text_obj = arcade.Text(
            self.content, self.window.width // 2,
            self.window.height * 0.8,
            font_size=config.FONT_SIZE_S,
            multiline=True,
            width=self.window.width * 0.9,
            anchor_x="center",
            anchor_y="center",
            align="center",
            )
        self.buttons = arcade.SpriteList()
        self.make_buttons()

    def read(self):
        file_wrapper = open(
            config.BASE_DIR / "statistics.txt",
            mode="r",
            encoding="utf-8",
            ) # Если не найдёт, то подавится
        self.content = file_wrapper.read()

    def on_draw(self):
        self.clear()
        self.text_obj.draw()
        self.buttons.draw()
        for button in self.buttons:
            button.draw()

    def make_buttons(self) -> None:
        """Метод создания кнопок."""
        button_width = self.window.width * 0.15
        button_height = self.window.height * 0.05
        spacing_vert = self.window.height * 0.1
        buttons_names = ["Меню"]
        button_x = self.window.width / (len(buttons_names) + 1)
        for button_name in buttons_names:
            button = Button(
                button_width,
                button_height,
                button_x,
                spacing_vert,
                text_str=button_name,
                )
            self.buttons.append(button)
            button_x += self.window.width / (len(buttons_names) + 1)

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопок."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons:
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Меню":
                self.window.show_menu_view()
