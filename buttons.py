"""Модуль кнопок."""
import arcade
import arcade.types

FONT_SIZE = 30

class Button(arcade.SpriteSolidColor):
    """Кнопка варианта ответа."""

    def __init__(self,
                 width: int,
                 height: int,
                 x: int,
                 y: int,
                 text_str: str) -> None:
        """Инициализирует кнопку."""
        super().__init__(
            width, height,
            x,
            y,
            color=arcade.types.Color(255, 255, 255, 255),
            )
        self.text_str = text_str
        self.text_obj = arcade.Text(
            text_str,
            x,
            y,
            arcade.color.VIOLET_BLUE,
            anchor_x="center",
            anchor_y="center",
            font_size=FONT_SIZE,
        )

    def draw(self) -> None:
        """Отрисовка."""
        arcade.draw_sprite(self)
        self.text_obj.draw()
