# Есть некоторый текст. Реализуйте следующую функциональность:
# ■ Изменить текст таким образом, чтобы каждое предложение начиналось с большой буквы;
# ■ Посчитайте сколько раз цифры встречаются в тексте;
# ■ Посчитайте сколько раз знаки препинания встречаются в тексте;
# ■ Посчитайте количество восклицательных знаков в тексте.

import re
import string


def capitalize_first_letter(match):
    txt = match.group(0)
    char = txt[len(txt)-1]
    modified = txt.replace(char, char.capitalize())
    return modified


def capitalize_sentences(text):
    capitalized = re.sub(r'([.?!]\s\w)|^\w', capitalize_first_letter, text)
    return capitalized


def count_digits(text):
    return len(re.findall('\d', text))


def count_punctuation(text):
    punct = string.punctuation
    return len(re.findall(f'[{punct}]', text))


def count_exclamation(text):
    return len(re.findall('!', text))


def main():
    text = 'lorem: ipsum dolor! sit amet consectetur adipisicing elit? nam - neque pariatur praesentium.' \
           '\namet, sunt fugiat (13 845 - consequuntur). nulla distinctio delectus.'
    print(f"\nOriginal:\n{text}")
    print(f"\nCapitalized:\n{capitalize_sentences(text)}\n")
    print(f"Digits: {count_digits(text)}")
    print(f"Punctuations: {count_punctuation(text)}")
    print(f"Exclamations: {count_exclamation(text)}")


if __name__ == '__main__':
    main()
