import menu

desc = """
Пользователь вводит с клавиатуры набор строк. Полученные строки необходимо сохранить в двусвязный 
список. После чего нужно показать меню, в котором 
предложить пользователю набор пунктов: 
1. Добавить элемент в список
2. Удалить элемент из списка
3. Показать содержимое списка
4. Проверить есть ли значение в списке
5. Заменить значение в списке
В зависимости от выбора пользователя выполняется 
действие, после чего меню отображается снова.
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.item)


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        i = self.head
        while i is not None:
            print(i.item, end=' => ')
            i = i.next
        print('None')

    def is_empty(self):
        return self.head is None

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

    def append_coll(self, coll):
        for i in coll:
            self.append(i)

    def remove(self, key):
        if self.is_empty():
            print('List empty')
            return
        cur = self.head
        while cur is not None and cur.item != key:
            cur = cur.next
        if cur is None:
            print(f'{key} does not exist in the list')
            return

        prev = cur.previous
        if cur.next is None:
            self.tail = prev

        if prev is None:
            self.head = cur.next
            if self.head is not None:
                self.head.prev = None
        else:
            prev.next = cur.next
            cur.prev = None
            if prev.next is not None:
                prev.next.prev = prev

    def exist(self, item):
        i = self.head
        while i.next is not None:
            if i.next.item == item:
                return True
            i = i.next
        return False

    def replace(self, old, new, all_occ=False):
        if old == new:
            return
        cur = self.head
        while cur is not None:
            if cur.item == old:
                cur.item = new
                if not all_occ:
                    return
            cur = cur.next


class MenuLL:
    def __init__(self, ll=None):
        self.ll = ll

    def get_input(self):
        return input('Item: ')

    def add(self):
        self.ll.append(self.get_input())

    def remove(self):
        self.ll.remove(self.get_input())

    def display(self):
        self.ll.display()

    def is_present(self):
        print(self.ll.exist(self.get_input()))

    def replace(self):
        self.ll.replace(self.get_input(), self.get_input())

    def edit(self):
        m = menu.init(['Add', 'Remove', 'Display', 'Is present', 'Replace'],
                      [self.add, self.remove, self.display, self.is_present, self. replace])
        m.run()


def user_collection():
    coll = []
    while True:
        item = input(f'Item: ')
        if item == '':
            break
        coll.append(item)
    return coll


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    linked = DoubleLinkedList()
    linked.append_coll(user_collection())
    linked_interface = MenuLL(linked)
    linked_interface.edit()
