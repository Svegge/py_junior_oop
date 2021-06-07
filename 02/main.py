"""
Используя навыки работы с текстом, получите количество студентов GeekBrains со
стартовой страницы сайта geekbrains.ru. Решите задачу двумя способами: a)
используя регулярные выражения (библиотеку re), b) используя библиотеку
BeautifulSoup. Примечание: Чтобы увидеть количество учеников, вам надо зайти на
главную страницу сайта без залогинивания (нажмите 3 точки в правом верхнем углу
экрана рядом с вашей фотографией и выберите пункт меню «Выход»). Вы окажетесь на
главной странице, где вверху увидите логотип, количество человек (то, что нам
нужно) и кнопку «Войти».
"""
import re
from bs4 import BeautifulSoup as BS

'<span class="gb-header__counter">Нас&nbsp;уже&nbsp;6 335 863&nbsp;человек</span>'

task = 'Task 1'
with open('index.html', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = '<span class="gb-header__counter">Нас&nbsp;уже&nbsp;([\\d\\s]+)&nbsp;человек</span>'
sudents_qty = re.findall(pattern, text)[0].replace(' ', '')
print('=' * 50, task, '=' * 50)
print('extracted students qty re:', sudents_qty)

task = 'Task 2'

with open('index.html', 'r', encoding='utf-8') as file:
    text = file.read()
soup = BS(text, "html.parser")
tag = soup.span
qty_list = tag.string.replace('\xa0', ' ').split()[2:5]
sudents_qty = int(''.join(i for i in qty_list))
print('=' * 50, task, '=' * 50)
print('extracted students qty bs4:', sudents_qty)
