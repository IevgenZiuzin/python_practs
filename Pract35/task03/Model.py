class User:
    def __init__(self):
        self._login = None
        self._password = None

    def __str__(self):
        return self._login

    def __repr__(self):
        return self._login

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)


class Users:
    def __init__(self):
        self.head = None

    def as_list(self):
        items = []
        i = self.head
        while i is not None:
            items.append(i.item)
            i = i.next
        return items

    def append(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            i = self.head
            while i.next is not None:
                i = i.next
            i.next = node

    def append_coll(self, coll):
        for i in coll:
            self.append(i)

    def remove(self, key):
        cur = self.head
        cur_pre = None
        while cur is not None:
            if str(cur.item) == key:
                if cur_pre is None:
                    self.head = None
                else:
                    cur_pre.next = cur.next
            cur_pre = cur
            cur = cur.next

    def exist(self, item):
        i = self.head
        while i.next is not None:
            if i.next.item == item:
                return True
            i = i.next
        return False

    def replace(self, old, new):
        if old == new:
            return
        current = self.head
        while current is not None:
            if current.item == old:
                current.item = new
                return
            current = current.next
        # raise ValueError(f'Item not found: {old}')

    def find(self, key):
        current = self.head
        while current is not None:
            if str(current.item) == key:
                return current.item
            current = current.next
