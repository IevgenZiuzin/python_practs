import os
from pathlib import Path


layout = """desc = \"\"\"

\"\"\"


def foo():
    pass


if __name__ == '__main__':
    print(f'{desc}\\n----------\\n')\n"""


# for i in range(23, 48):
#     Path(f'./Pract{i}').mkdir()
#     for k in range(1, 11):
#         file = open(f'./Pract{i}/task0{k}.py', 'w')
#         file.write(layout)
#         file.close()
