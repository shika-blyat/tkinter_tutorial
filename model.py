class TodoElement:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class TodoList:
    def __init__(self, todo_list=None):
        if todo_list == None:
            todo_list = [TodoElement("Delete this todo")]
        self.todo_list = todo_list

    def add_element(self, todo):
        self.todo_list.append(todo)

    def remove(self, idx):
        self.todo_list.pop(idx)


todo_list = TodoList()
