from collections import UserList


class TodoElement:
    content: str

    def __init__(self, content: str):
        self.content = content

    def __str__(self):
        return self.content


class TodoList(UserList):
    def __init__(self, todo_list=None):
        super().__init__(self)

        if todo_list is None:
            todo_list = [TodoElement("Delete this todo")]

        self.data.extend(todo_list)

    def append(self, todo: TodoElement):
        self.data.append(todo)

    def remove(self, todo: TodoElement):
        self.data.remove(todo)

    def pop(self):
        self.data.pop()

    def __iter__(self):
        return iter(self.data)
