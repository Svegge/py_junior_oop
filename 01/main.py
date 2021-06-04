import re


def count_list_items(custom_list: list):
    counter_list = []
    for i in set(custom_list):
        counter_list.append((i, custom_list.count(i)))
    counter_list_sorted = sorted(
        counter_list, key=lambda i: i[1], reverse=True)
    return counter_list_sorted


# 1. Получите текст из файла. Примечание: Можете взять свой текст или
#    воспользоваться готовым из материалов к уроку. Вспомните операции с чтением
# файлов и не забудьте сохранить текст в переменную по аналогии с
# видеоуроками.
task = 'Task 1'
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print('=' * 50, task, '=' * 50)
print(text)

# 2. Разбейте полученные текст на предложения. Примечание: Напоминаем, что в
#    русском языке предложения заканчиваются на ., ! или ?.
task = 'Task 2'
pattern = '[\.!?]\s'
sentence_list = re.split(pattern, text)
print('=' * 50, task, '=' * 50)
print(sentence_list)

# 3. Найдите слова, состоящие из 4 букв и более. Выведите на экран 10 самых часто
# используемых слов. Пример вывода: [(“привет”, 3), (“люди”, 3), (“город”,
# 2)].
task = 'Task 3'
pattern = '[\w^\d]{4,}'
words_list = re.findall(pattern, text)
print('=' * 50, task, '=' * 50)
print(count_list_items(words_list)[:10])
# 4. Отберите все ссылки. Примечание: Для поиска воспользуйтесь методом compile, в
#    который вы вставите свой шаблон для поиска ссылок в тексте.
task = 'Task 4'
pattern = '\w+\.[\w+\./]+'
links_finder = re.compile(pattern)
links_list = links_finder.findall(text)
print('=' * 50, task, '=' * 50)
print(links_list)
# 5. Ссылки на страницы какого домена встречаются чаще всего? Напоминаем, что
#    доменное имя — часть ссылки до первого символа «слеш». Например в ссылке вида
#    travel.mail.ru/travel?id=5 доменным именем является travel.mail.ru. Подсчет
#    частоты сделайте по аналогии с заданием 3, но верните только одну самую
#    частую ссылку.
task = 'Task 5'
pattern = '(\w+\.[\w+\.]+)/'
domain_list = re.compile(pattern).findall(text)
print('=' * 50, task, '=' * 50)
print(count_list_items(domain_list)[:1])
# 6. Замените все ссылки на текст «Ссылка отобразится после регистрации».
task = 'Task 6'
pattern = '\w+\.[\w+\./]+'
sub_str = 'Ссылка отобразится после регистрации'
text = re.sub(pattern, sub_str, text)
print('=' * 50, task, '=' * 50)
print(text)
