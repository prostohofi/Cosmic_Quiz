"""Модуль представления познавания."""
import arcade
import arcade.types

import config
from buttons import Button
from knowledge import slide_texts_str


class KnowledgeView(arcade.View):
    """Представление меню."""

    def __init__(self) -> None:
        """Инициализирует представление меню."""
        super().__init__()
        self.slide_num = 1
        self.buttons = arcade.SpriteList()
        self.sprites = arcade.SpriteList()
        self.texts = []
        self.total_slides = len(slide_texts_str)
        self.current_slide = arcade.Text(
            f"{self.slide_num}/{self.total_slides}",
            self.window.width // 2,
            self.window.height,
            font_size=config.FONT_SIZE_S,
            anchor_x="center",
            anchor_y="top",
        )
        self.load_slide()
        self.menu_sprites = self.window.create_dark_background()
        self.buttons = self.window.make_buttons(["Предыдущий",
              "Следующий",
              "В меню"],
              )

    def load_slide(self) -> None:
        """Метод загрузки слайда."""
        self.sprites.clear()
        self.texts.clear()
        num_texture = str(self.slide_num) + ".jpg"
        self.sprite_texture = arcade.load_texture(
            config.ASSETS_DIR / "img" / "knowledge_slides" / num_texture,
            )
        slide_image = arcade.Sprite(
            self.sprite_texture,
            center_x=self.window.width * 0.14,
            center_y=self.height // 2,
            )
        self.sprites.append(slide_image)
        self.current_slide.text = f"{self.slide_num}/{self.total_slides}"

        slide_text_obj = arcade.Text(
            slide_texts_str[self.slide_num - 1],
            self.window.width * 0.63,
            self.window.height // 2,
            anchor_x="center",
            anchor_y="center",
            align="center",
            font_size=config.FONT_SIZE_S,
            multiline=True,
            width=self.window.width * 0.7,
            )

        self.texts.append(slide_text_obj)

    def on_draw(self) -> None:
        """Отрисовывает спрайты и текст на экране."""
        self.clear()
        self.menu_sprites.draw()
        self.current_slide.draw()
        for button in self.buttons:
            button.draw()
        self.sprites.draw()
        for text in self.texts:
            text.draw()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Нажатие кнопок."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons:
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Следующий" and self.slide_num < self.total_slides:
                    self.slide_num += 1
                    self.load_slide()
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "Предыдущий" and self.slide_num > 1:
                    self.slide_num -= 1
                    self.load_slide()
            if sprite_button.collides_with_point((x, y)) and sprite_button.text_str == "В меню":
                    self.window.show_menu_view()
