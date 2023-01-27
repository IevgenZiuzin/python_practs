desc = """Напишите функцию, которая отображает на экран 
форматированный текст, указанный ниже:

“Don't let the noise of others' opinions 
drown out your own inner voice.”
                              Steve Jobs"""


def display_quotation(quotation):
    print(quotation)


if __name__ == '__main__':
    print(f'{desc}\n----------')
    quotation = """
“Don't let the noise of others' opinions 
drown out your own inner voice.”
                              Steve Jobs"""
    display_quotation(quotation)
