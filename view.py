import tkinter as tk
from tkinter import font
from tkinter import ttk
from model import todo_list
from controller import add_a_todo_element

root = tk.Tk()

FONT = font.Font(family="Arial", size=20)
root.option_add("*Listbox*Font", FONT)


list_todo = tk.Listbox(root)

scrollbarY = tk.Scrollbar(root, orient="vertical")

scrollbarY.pack(fill=tk.Y, side=tk.RIGHT)
list_todo.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=list_todo.yview)


scrollbarX = tk.Scrollbar(root, orient="horizontal")

scrollbarX.pack(fill=tk.X, side=tk.BOTTOM)
list_todo.config(xscrollcommand=scrollbarX.set)
scrollbarX.config(command=list_todo.xview)

list_todo.pack()


todo_content = tk.StringVar()
todo_textbox = ttk.Entry(root, width=15, textvariable=todo_content)
todo_textbox.pack(side=tk.RIGHT, fill=tk.Y)


def create_new_item():
    content = todo_textbox.get()
    if content.strip() != "":
        add_a_todo_element(content)
    update_view()


def delete_selected_item():
    active = list_todo.curselection()
    if len(active) != 0:
        todo_list.pop(active[0])
        update_view()


add_item_button = tk.Button(root, text="Add Item", command=create_new_item)
add_item_button.pack(side=tk.RIGHT, fill=tk.Y)


del_item_button = tk.Button(root, text="Delete Item", command=delete_selected_item)
del_item_button.pack(side=tk.LEFT, fill=tk.Y)


def update_view():
    list_todo.delete(0, tk.END)
    for item in todo_list:
        list_todo.insert(tk.END, item)

