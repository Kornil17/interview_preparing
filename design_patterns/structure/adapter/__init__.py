# Целевой интерфейс (ожидаемый системой)
class TextProcessor:
    def process_text(self, text):
        pass


# Адаптируемый класс (сторонняя библиотека)
class WordCounter:
    def count_words(self, text):
        self.words = {}
        for word in text.split():
            self.words[word] = self.words.get(word, 0) + 1

    def get_all_words(self):
        return self.words

    def get_count(self, word):
        return self.words.get(word, 0)


# Адаптер
class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words()
        # Сортируем слова по частоте (убывание)
        return sorted(words.keys(), key=lambda x: self.adaptee.get_count(x), reverse=True)


# Использование
system_text = "Привет мир привет"
processor = WordCounterAdapter(WordCounter())
result = processor.process_text(system_text)
print(result)  # ['привет', 'мир']
