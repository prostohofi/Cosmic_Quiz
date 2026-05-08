"""Модуль форматированного времени."""


def get_formated_time(sec: float) -> str:
    """Преобразует секунды во время в формате: 'ЧЧ:ММ:СС'."""
    hours = int(sec // 3600)
    minutes = int((sec % 3600) // 60)
    secs = int(sec % 60)
    return f"{hours:02}:{minutes:02}:{secs:02}"
