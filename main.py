"""Игра - викторина."""

import random

import arcade

import config
import views.how_to_play_view as howtoplay
from buttons import Button
from views import general_view, knowledge_view, menu_view, quiz_view, statistics_view


class MyWindow(arcade.Window):
    """Класс собственного окна."""

    def __init__(self) -> None:
        """Инициализация класса."""
        super().__init__(fullscreen=True)
        self.sound = arcade.load_sound(config.SOUNDS_DIR / "PPK - Resurection.mp3")
        self.sound_player = self.sound.play(0.1, loop=True)
        self.right_answers = 0
        self.wrong_answers = 0
        self.timer = 0
        self.count_bg = 17
        self.text_music = arcade.Text(
            "Остановить/Запустить музыку",
            self.width * 0.92,
            self.height * 0.9,
            anchor_x="center",
            anchor_y="center",
            align="center",
            font_size=14,
        )
        self.buttons_music = arcade.SpriteList()
        music_buttons = [("▶", 0.95), ("◼", 0.89)]
        for text, x_offset in music_buttons:
            button = Button(
                self.width * 0.05,
                self.height * 0.05,
                self.width * x_offset,
                self.height * 0.95,
                text,
            )
            self.buttons_music.append(button)

    def on_draw(self) -> None:
        """Метод отрисовки."""
        for button_music in self.buttons_music:
            button_music.draw()
        self.text_music.draw()

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
        button_width = self.width * 0.15
        button_height = self.height * 0.05
        spacing_vert = self.height * 0.1
        buttons_names = buttons_names_list
        button_x = self.width / (len(buttons_names) + 1)
        for button_name in buttons_names:
            button = Button(
                button_width,
                button_height,
                button_x,
                spacing_vert,
                text_str=button_name,
                )
            buttons.append(button)
            button_x += self.width / (len(buttons_names) + 1)
        return buttons

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Метод нажатия кнопок мыши."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for sprite_button in self.buttons_music:
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "▶":
                    self.sound_player = self.sound.play(0.1, loop=True)
            if sprite_button.collides_with_point(
                (x, y),
                ) and sprite_button.text_str == "◼":
                    self.sound.stop(self.sound_player)





window = MyWindow()
view = menu_view.MenuView()
window.show_view(view)
arcade.run()
