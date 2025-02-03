import random  # импортируем модуль random для генерации случайных чисел
import string  # импортируем модуль string для работы со строками

def generate_username(length=8):  # определяем функцию с параметром длины имени по умолчанию 8
    letters = string.ascii_letters  # получаем все английские буквы (маленькие и большие)
    all_chars = letters
    username = ''.join(random.choice(all_chars) for _ in range(length))  # генерируем случайное имя нужной длины
    return username  # возвращаем сгенерированное имя пользователя

def generate_email():  # определяем функцию generate_random_email
    username = generate_username()  # генерируем случайное имя пользователя с помощью функции generate_username
    digits = ''.join(random.choices(string.digits, k=3))  # генерируем три случайных цифры
    email = f"{username}{digits}@yandex.ru"  # формируем полный email адрес
    return email  # возвращаем сгенерированный email

def generate_incorrect_email():  # определяем функцию generate_random_email
    username = generate_username()  # генерируем случайное имя пользователя с помощью функции generate_username
    digits = ''.join(random.choices(string.digits, k=3))  # генерируем три случайных цифры
    incorrect_email = f"{username}{digits}yandex.ru"  # формируем полный email адрес
    return incorrect_email  # возвращаем сгенерированный email

def generate_incorrect_password():  # определяем функцию generate_password
    characters = string.ascii_letters + string.digits  # создаем строку из всех букв и цифр
    incorrect_password = ''.join(random.choice(characters) for _ in range(5))  # выбираем случайные 6 символов и объединяет их в строку
    return incorrect_password  # возвращаем сгенерированный пароль

def generate_password():  # определяем функцию generate_password
    characters = string.ascii_letters + string.digits  # создаем строку из всех букв и цифр
    password = ''.join(random.choice(characters) for _ in range(6))  # выбираем случайные 6 символов и объединяет их в строку
    return password  # возвращаем сгенерированный пароль

username = generate_username(8)
incorrect_email = generate_incorrect_email()
email = generate_email()
incorrect_password = generate_incorrect_password()
password = generate_password()