"""
Это задание продолжает практическое задание прошлого урока.
За основу возьмите свой код с классами Word и Sentence.
Выполним с ним следующие преобразования:
"""


class Word():
    def __init__(self, text: str):
        self.text = text


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
            result_parts.append(words_list[i].part())
        return list(set(result_parts))


words_array = [["собака", "сущ"],
               ["ела", "глагол"],
               ["колбасу", "сущ"],
               ["вечером", "наречие"]]


# 1. Создайте новые классы Noun (существительное) и Verb (глагол).
# 2. Настройте наследование новых классов от класса Word.
# 3. Добавьте в новые классы свойство grammar («Грамматические характеристики»).
# Для класса Noun укажите значение по умолчанию «сущ» (сокращение от существительное),
# а для Verb — «гл» (сокращение от глагол). Вспомните про инкапсуляцию и
# сделайте свойство grammar защищённым.

class Noun(Word):
    _grammar = 'сущ'


class Verb(Word):
    _grammar = 'гл'

# 4. Исправьте класс Word, чтобы указанный ниже код не вызывал ошибки.
# Подсказка: теперь в нём не нужно хранить части речи.


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))

# 5. Протестируйте работу старого метода show класса Sentence. Если
# предложения не формируются, исправьте ошибки.

sentence = Sentence([0, 1])

words = [Word(word[0]) for word in words_array]

print(sentence.show(words))

# 6. Допишите в классы Noun и Verb метод part. Данный метод должен
# возвращать строку с полным названием части речи.


class Noun(Word):
    _grammar = 'сущ'

    def part(self):
        return 'Существительное'


class Verb(Word):
    _grammar = 'гл'

    def part(self):
        return 'Глагол'


words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))

print(words[2].part())

# 7. Протестируйте работу метода show_part класса Sentence. Исправьте ошибки, чтобы метод работал.
# Подсказка: ранее part был свойством класса Word, а теперь это метод
# классов Noun и Verb.

print(sentence.show_parts(words))
