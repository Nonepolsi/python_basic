navigation_bar = [
    {"verbose_name": "Пользователи", "url_name": "users"},
    {"verbose_name": "Тесты", "url_name": "quiz_list"},
    {"verbose_name": "Результаты", "url_name": "results"},
    {"verbose_name": "Вопросы", "url_name": "questions"}
]


def get_postfix(in_str: str) -> str:

    return str(hash(in_str))[:4]


def convert_ru_chars(in_str: str) -> str:
    d = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d",
         "е": "e", "ё": "yo", "ж": "zh", "з": "z", "и": "i", "к": "k",
         "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
         "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch",
         "ш": "sh", "щ": "shch", "ь": "", "ы": "y", "ъ": "", "э": "e", "ю": "yu", "я": "ya"}

    return "".join([d[ch] if d.get(ch, False) else ch for ch in in_str])

