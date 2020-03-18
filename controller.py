import tkinter as tk

from model import TodoList, TodoElement, todo_list
from view import todo_textbox, del_item_button, add_item_button, view_list


def create_new_item():
    content = todo_textbox.get()
    if content.strip() != "":
        todo_list.add_element(TodoElement(content))
    update_view()


def delete_selected_item():
    active = view_list.curselection()
    if len(active) != 0:
        todo_list.delete_element(active[0])
        update_view()


def update_view():
    view_list.delete(0, tk.END)
    for item in todo_list.todo_list:
        view_list.insert(tk.END, item)


del_item_button.config(command=delete_selected_item)
add_item_button.config(command=create_new_item)
