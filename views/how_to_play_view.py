"""Модуль представления, как играть."""

import arcade

import config


class HowToPlay(arcade.View):
    """Представление меню."""

    def __init__(self) -> None:
        """Инициализирует представление меню."""
        super().__init__()
        self.sprite_quiz = arcade.Sprite(
            config.ASSETS_DIR / "img" / "how_to_play_img" / "1.png",
            center_x=self.window.width * 0.2,
            center_y=self.window.height * 0.6,
            scale=0.4,
            )
        self.sprite_statistic = arcade.Sprite(
            config.ASSETS_DIR / "img" / "how_to_play_img" / "2.png",
            center_x=self.window.width * 0.8,
            center_y=self.window.height * 0.6,
            scale=0.4,
            )
        self.menu_sprites = self.window.create_dark_background()
        self.text = arcade.Text(
            ("Надо отвечать на вопросы за время и видеть "
            "количество своих верных и неверных ответов в конце в статистике"),
            x=self.window.width // 2,
            y=self.window.height * 0.2,
            font_size=config.FONT_SIZE_S,
            align="center",
            anchor_x="center",
            anchor_y="center",
            )
        self.buttons = arcade.SpriteList()
        self.sprites = arcade.SpriteList()
        self.buttons = self.window.make_buttons(["В меню"])
        self.sprites.append(self.sprite_quiz)
        self.sprites.append(self.sprite_statistic)

    def on_draw(self) -> None:
        """Отрисовывает спрайты и текст на экране."""
        self.clear()
        self.menu_sprites.draw()
        for button in self.buttons:
            button.draw()
        self.sprites.draw()
        self.text.draw()


    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопок."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons:
            if sprite_button.collides_with_point(
                 (x, y),
                 ) and sprite_button.text_str == "В меню":
                    self.window.show_menu_view()
