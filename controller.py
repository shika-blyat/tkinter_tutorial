from model import todo_list


def add_a_todo_element(todo):
    global todo_list
    todo_list.append(todo)


def delete_a_todo_element(idx):
    global todo_list
    todo_list.pop(idx)
