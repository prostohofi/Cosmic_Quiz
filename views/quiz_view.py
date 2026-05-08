"""Модуль представления викторины."""
import random
import time

import arcade

import config
import questions
from buttons import Button
from utils import get_formated_time


class QuizView(arcade.View):
    """Викторина."""

    def __init__(self, window: arcade.Window) -> None:
        """Инициализирует викторину."""
        super().__init__()
        self.window = window
        self.question_idx = 0
        self.right_answers = 0
        self.wrong_answers = 0
        self.start_time = time.time()
        self.total_time = 0.0
        self.buttons = arcade.SpriteList()
        self.questions = questions.questions
        random.shuffle(self.questions)
        self.sprites = arcade.SpriteList()
        self.question = self.questions[self.question_idx]
        self.question_text = arcade.Text(
            self.question["текст"],
            self.width // 2,
            self.height // 2,
            anchor_x="center",
            anchor_y="center",
            align="center",
            font_size=config.FONT_SIZE_S,
            multiline=True,
            width=self.window.width * 0.8,
        )

        self.bg_sprites = self.window.create_dark_background()
        self.current_question = arcade.Text(
            f"{self.question_idx + 1}/{len(self.questions)}",
            self.window.width // 2,
            self.window.height,
            font_size=config.FONT_SIZE_S,
            anchor_x="center",
            anchor_y="top",
        )
        self.make_buttons()
        self.time_left_sec = 300
        self.timer = arcade.Text(
            "0",
            0,
            self.window.height,
            font_size=config.FONT_SIZE_S,
            anchor_x="left",
            anchor_y="top",
        )
        if self.question["картинка"]:
            texture = arcade.load_texture(
                config.IMG_DIR / "knowledge_slides" / self.question["картинка"],
                )
            self.question_picture = arcade.Sprite(
                texture, center_x=self.window.width * 0.1,
                    center_y=self.window.height // 2,
                    )
            self.sprites.append(self.question_picture)

    def make_buttons(self) -> None:
        """Создает кнопки с ответами."""
        for num, option in enumerate(self.question["варианты"], 1):
            button = Button(
                len(self.question_text.text) * 7,
                50,
                self.width // 2,
                self.height // 2 - (num * 100),
                option,
            )
            self.buttons.append(button)
        self.buttons.shuffle()

    def on_update(self, delta_time: float) -> None:
        """Обновление игровых объектов."""
        self.time_left_sec -= delta_time
        self.timer.text = get_formated_time(self.time_left_sec)

    def on_draw(self) -> None:
        """Отрисовка игровых объектов."""
        self.clear()
        self.bg_sprites.draw()
        self.sprites.draw()
        self.question_text.draw()
        for button in self.buttons:
            button.draw()
        self.current_question.draw()
        self.timer.draw()

    def on_key_press(self, symbol: int, _: int) -> None:
        """Обработка клавиш."""
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_mouse_press(self, x: int, y: int, button: int, _: int) -> None:
        """Обработка кликов мышью."""
        if button != arcade.MOUSE_BUTTON_LEFT:
            return
        for button_sprite in self.buttons:
            if not button_sprite.collides_with_point((x, y)):
                continue
            if button_sprite.text_str == self.question["ответ"]:
                self.right_answers += 1
            else:
                self.wrong_answers += 1
            break
        self.load_question()

    def load_question(self) -> None:
        """Загружает след. вопрос - новый текст и новые кнопки."""
        self.sprites.clear()
        self.question_idx += 1
        if self.question_idx >= len(self.questions):
            self.window.right_answers = self.right_answers
            self.window.wrong_answers = self.wrong_answers
            self.window.timer = self.timer.text
            self.window.show_statistic_view()
            return
        self.current_question.text = f"{self.question_idx + 1}/{len(self.questions,)}"
        self.question = self.questions[self.question_idx]
        self.question_text.text = self.question["текст"]
        if self.question["картинка"]:
            texture = arcade.load_texture(
                config.IMG_DIR / "knowledge_slides" / self.question["картинка"],
                )
            self.question_picture = arcade.Sprite(
                texture, center_x=self.window.width * 0.1,
                    center_y=self.window.height // 2,
                    )
            self.sprites.append(self.question_picture)
        self.buttons.clear()
        self.make_buttons()
