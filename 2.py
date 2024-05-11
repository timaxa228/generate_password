from random import *


def proverka_na_zifri(num):
    if num.isdigit():
        return True
    else:
        print('Введены некорректные данные, ошибка ввода, повторите ввод...')
        return False


'''
def da_or_net(otvet):
    if otvet == 'да' or otvet == 'нет':
        return True
    else:
        print('Введены некорректные данные, ошибка ввода, повторите ввод...')
        return False
'''


def kol_vo_paroley():
    while True:
        kol_vo_paroley1 = input('Сколько паролей вам нужно сгенерировать? ')
        if proverka_na_zifri(kol_vo_paroley1):
            return int(kol_vo_paroley1)
        else:
            continue


def dlina_parola():
    while True:
        dlina_parola1 = input('Какой длины должен быть пароль? ')
        if proverka_na_zifri(dlina_parola1):
            return int(dlina_parola1)
        else:
            continue


def vkl_digits():
    global chars
    while True:
        vkl_digits1 = input('Включать ли в пароль цифры от 0 до 9? ')
        vkl_digits1 = vkl_digits1.lower()
        if vkl_digits1 == 'да':
            chars += '0123456789'
            return chars
        elif vkl_digits1 == 'нет':
            return chars
        else:
            print('Введены некорректные данные, ошибка ввода, повторите ввод...')
            continue


def vkl_uppercase():
    global chars
    while True:
        vkl_uppercase1 = input('Включать ли прописные буквы? ')
        vkl_uppercase1 = vkl_uppercase1.lower()
        if vkl_uppercase1 == 'да':
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            return chars
        elif vkl_uppercase1 == 'нет':
            return chars
        else:
            print('Введены некорректные данные, ошибка ввода, повторите ввод...')
            continue


def vkl_lowercase():
    global chars
    while True:
        vkl_lowercase1 = input('Включать ли строчные буквы? ')
        vkl_lowercase1 = vkl_lowercase1.lower()
        if vkl_lowercase1 == 'да':
            chars += 'abcdefghijklmnopqrstuvwxyz'
            return chars
        elif vkl_lowercase1 == 'нет':
            return chars
        else:
            print('Введены некорректные данные, ошибка ввода, повторите ввод...')
            continue


def vkl_punctuation():
    global chars
    while True:
        vkl_punctuation1 = input('Включать ли символы? ')
        vkl_punctuation1 = vkl_punctuation1.lower()
        if vkl_punctuation1 == 'да':
            chars += '!#$%&*+-=?@^_'
            return chars
        elif vkl_punctuation1 == 'нет':
            return chars
        else:
            print('Введены некорректные данные, ошибка ввода, повторите ввод...')
            continue


def remove_badsymbols():
    global chars
    while True:
        remove_badsymbols1 = input('Исключить символы il1Lo0O? ')
        remove_badsymbols1 = remove_badsymbols1.lower()
        if remove_badsymbols1 == 'да':
            for j in 'il1Lo0O':
                chars = chars.replace(j, '')
            return chars
        elif remove_badsymbols1 == 'нет':
            return chars
        else:
            print('Введены некорректные данные, ошибка ввода, повторите ввод...')
            continue


def summa_char():
    global chars
    print('Генератор паролей готов!')

    vkl_digits()
    vkl_uppercase()
    vkl_lowercase()
    vkl_punctuation()
    remove_badsymbols()

    return chars


chars = ''
kol_vo_paroley = kol_vo_paroley()
dlina_parola = dlina_parola()
chars1 = summa_char()


def generate_password(lengh, chars1):
    password = ''
    if chars1 == '':
        return False
    else:
        for k in range(lengh):
            password += choice(chars1)
        return password


if not generate_password(dlina_parola, chars1):
    print('Не получилось сгенерировать пароль!')
else:
    for i in range(kol_vo_paroley):
        paroli = generate_password(dlina_parola, chars1)
        print(paroli)
