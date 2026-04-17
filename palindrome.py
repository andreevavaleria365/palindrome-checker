def is_palindrome(text):
    """
    Проверяет, является ли строка палиндромом.
    Игнорирует пробелы и регистр букв.
    """
    # Удаляем все пробелы и переводим в нижний регистр
    cleaned = ""
    for char in text:
        if char != " ":
            cleaned = cleaned + char.lower()
    
    # Проверяем, читается ли одинаково слева направо и справа налево
    reversed_text = cleaned[::-1]
    return cleaned == reversed_text


# Простая проверка работы функции (можно удалить, это просто для примера)
if __name__ == "__main__":
    test_phrases = [
        "А роза упала на лапу Азора",
        "hello",
        "racecar",
        "мадам",
        "просто текст"
    ]
    
    for phrase in test_phrases:
        result = is_palindrome(phrase)
        print(f"'{phrase}' -> {result}")
