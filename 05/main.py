"""
В упражнении мы потренируемся в создании объектно-ориентированной
среды и создадим приложение, проводящее лингвистический анализ.
Следуйте алгоритму и выполняйте действия последовательно,
чтобы получить полноценный класс:
"""

# 1. Создайте класс Word. (Вспомните, какое зарезервированное слово используется для создания класса).
# 2. Добавьте свойства text (класс будет хранить слово) и part (часть
# речи, которой является слово. Например, существительное, прилагательное
# и т.п.). Для добавления свойств воспользуйтесь методом __init__.


class Word():
    def __init__(self, text: str, part: str):
        self.text = text
        self.part = part

# 3. Создайте экземпляр класса Word, передав в качестве параметров любое
# слово и указав его часть речи.


word = Word('Машина', 'Существительное')

# 4. Создайте класс Sentence. (по аналогии с п. 1).
# 5. Добавьте свойство content. (по аналогии с п. 2).


class Sentence():
    def __init__(self, numbers: list):
        self.content = numbers

# 6. Создайте из массива (можете взять приведённый выше или придумать
# свой) список, каждый элемент которого является экземпляром класса Word.
# Примечание: список list (назовём его words) — отдельная переменная, не
# относящаяся к классам Word и Sentence.


words_array = [["собака", "сущ"],
               ["ела", "глагол"],
               ["колбасу", "сущ"],
               ["вечером", "наречие"]]

words = [Word(word[0], word[1]) for word in words_array]

# 7. Добавьте в класс Sentence метод show, составляющий предложение. Метод
# должен перебирать числа из свойства content и подставлять
# соответствующие слова, которые хранятся в свойстве text экземпляров
# класса Word. Данные извлекаем из списка words, который получили на
# прошлом шаге. При соединении слов в предложение не забудьте добавить
# пробел между словами.


class Sentence():

    def __init__(self, numbers: list):
        self.content = numbers

    def show(self, words_list):
        result = ''
        for i in self.content:
            result = result + words_list[i].text + ' '
        return result


sentence = Sentence([1, 3])

print(sentence.show(words))

# 8. Добавьте в класс Sentence метод show_parts, отображающий, какие части
# речи входят в предложение. По аналогии с п. 7 перебирайте в цикле числа
# из свойства content и сохраняйте результат в отдельный список. Учтите,
# что части речи могут повторяться, но список не должен содержать
# дубликаты.


class Sentence():

    def __init__(self, numbers: list):
        self.content = numbers

    def show(self, words_list):
        result = ''
        for i in self.content:
            result = result + words_list[i].text + ' '
        return result

    def show_parts(self, words_list):
        result_parts = []
        for i in self.content:
            result_parts.append(words_list[i].part)
        return list(set(result_parts))


sentence = Sentence([1, 3])

print(sentence.show_parts(words))
