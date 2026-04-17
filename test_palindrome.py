import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    
    def test_simple_palindromes(self):
        """Проверка простых палиндромов без пробелов"""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("ротор"))
        self.assertTrue(is_palindrome("топот"))
    
    def test_phrases_with_spaces(self):
        """Проверка фраз с пробелами и разным регистром"""
        self.assertTrue(is_palindrome("А роза упала на лапу Азора"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Never odd or even"))
        self.assertTrue(is_palindrome("Я иду с мечем судия"))
    
    def test_non_palindromes(self):
        """Проверка строк, которые НЕ являются палиндромами"""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("программирование"))
        self.assertFalse(is_palindrome("просто текст"))
    
    def test_edge_cases(self):
        """Проверка особых случаев"""
        self.assertTrue(is_palindrome(""))          # пустая строка
        self.assertTrue(is_palindrome("a"))         # один символ
        self.assertTrue(is_palindrome("   "))       # только пробелы
        self.assertTrue(is_palindrome("  А  "))     # буква с пробелами
    
    def test_numbers(self):
        """Проверка палиндромов из цифр"""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("12 3 21"))
        self.assertTrue(is_palindrome("123321"))
        self.assertFalse(is_palindrome("12345"))


if __name__ == "__main__":
    unittest.main()
