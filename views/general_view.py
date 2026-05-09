"""Модуль общей статистики."""
import arcade

import config


class GeneralStatisticsView(arcade.View):
    """Представление  общей статистики."""

    def __init__(self) -> None:
        """Инициализирует представление статистики:правильные и неправильные ответы."""
        super().__init__()
        self.content = ""
        self.number_string = 0
        self.menu_sprites = self.window.create_dark_background()
        self.read()
        self.text_obj = arcade.Text(
            f"{self.number_string}. {self.content}",
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
        """Метод, который берёт из файла статистики текст."""
        self.number_string += 1
        file_wrapper = open(
            config.BASE_DIR / "statistics.txt",
            mode="r",
            encoding="utf-8",
            ) # Если не найдёт, то подавится
        self.content = file_wrapper.read()

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
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Меню":
                self.window.show_menu_view()
