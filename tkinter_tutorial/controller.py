import tkinter as tk
from . import model
from . import view
import json

state = {
    "todo_list": model.TodoList(),
    "new_todo_content": tk.StringVar(),
}


def setup():
    bind_buttons()
    bind_variables()


def save_list_in_json():
    """
    Save the current state of the todo list in a json file and setup another save for 5 seconds later
    """
    with open("todo_list.json", "w+") as f:
        json_content = json.dumps(
            {"todo_list": [i.content for i in state["todo_list"]]}, indent=4
        )
        f.write(json_content)
    view.root.after(5000, save_list_in_json)


def mainloop():
    update_view()
    view.root.geometry("")
    view.root.after(0, save_list_in_json)
    view.root.minsize(500, 300)
    view.root.mainloop()


def create_new_item():
    """
    Create a new item in the global todo list
    """
    content = state["new_todo_content"].get().strip()
    if content:
        todo = model.TodoElement(content)
        state["todo_list"].append(todo)
        update_view()


def delete_selected_item():
    """
    Delete the currently selected item in the global todo_list
    """
    active = view.todo_list.curselection()
    if len(active) != 0:
        todo_index = active[0]
        del state["todo_list"][todo_index]
        update_view()


def update_view():
    view.todo_list.delete(0, tk.END)
    for todo in state["todo_list"]:
        view.todo_list.insert(tk.END, todo.content)


def bind_buttons():
    """
    Bind the related function to create and delete button
    """
    view.del_item_button.config(command=delete_selected_item)
    view.add_item_button.config(command=create_new_item)


def bind_variables():
    """
    Bind the TkString global variable to the textbox
    """
    view.todo_textbox.config(textvariable=state["new_todo_content"])
