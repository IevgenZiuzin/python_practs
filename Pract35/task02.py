import menu
import heapq

desc = """
Создайте класс очереди с приоритетами для работы 
с символьными значениями. 
Требуется создать реализации для операций над элементами очереди:
■ IsEmpty — проверка очереди на пустоту.
■ IsFull — проверка очереди на заполнение.
■ InsertWithPriority — добавление элемента c приоритетом в очередь.
■ PullHighestPriorityElement — удаление элемента с самым высоким приоритетом из очереди.
■ Peek — возврат самого большого по приоритету элемента. Обращаем ваше внимание, что элемент не 
удаляется из очереди.
■ Show — отображение всех элементов очереди на экран. 
При показе элемента также необходимо отображать 
приоритет.
При старте приложения нужно отобразить меню 
с помощью, которого пользователь может выбрать необходимую операцию.
"""


class PriorityQueue:
    insertion_count = 0
    limit = 0

    def __init__(self):
        self.pqueue = []

    def _is_empty(self):
        return not self.pqueue

    def is_empty(self):
        print(not self.pqueue)
        return not self.pqueue

    def is_full(self):
        print(0 < len(self.pqueue) == self.__class__.limit)
        return 0 < len(self.pqueue) == self.__class__.limit

    def insert(self):
        value = input('Value: ')
        if value == '':
            return
        priority = input('Priority: ')
        if not priority.isdigit():
            return
        heapq.heappush(self.pqueue, (int(priority), self.insertion_count, value))
        self.insertion_count += 1

    def pull(self):
        """return and remove"""
        if self._is_empty():
            return None
        print(heapq.heappop(self.pqueue)[2])
        return heapq.heappop(self.pqueue)[2]

    def peek(self):
        """return but not remove"""
        if self._is_empty():
            return None
        print(self.pqueue[0][2])
        return self.pqueue[0]

    def show(self):
        for i in self.pqueue:
            print(i, end=' => ')
        print('')


if __name__ == '__main__':
    print(f'{desc}\n----------\n')
    pqueue = PriorityQueue()
    m = menu.init(['IsFull', 'IsEmpty', 'InsertWithPriority', 'PullHighestPriorityElement', 'Peek', 'Show'],
                  [pqueue.is_full, pqueue.is_empty, pqueue.insert, pqueue.pull, pqueue.peek, pqueue.show])
    m.run()
