import tkinter as tk
from tkinter import font
from tkinter import ttk
from model import todo_list

root = tk.Tk()

FONT = font.Font(family="Arial", size=20)
root.option_add("*Listbox*Font", FONT)


view_list = tk.Listbox(root)

scrollbarY = tk.Scrollbar(root, orient="vertical")

scrollbarY.pack(fill=tk.Y, side=tk.RIGHT)
view_list.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=view_list.yview)


scrollbarX = tk.Scrollbar(root, orient="horizontal")

scrollbarX.pack(fill=tk.X, side=tk.BOTTOM)
view_list.config(xscrollcommand=scrollbarX.set)
scrollbarX.config(command=view_list.xview)

view_list.pack()


todo_content = tk.StringVar()
todo_textbox = ttk.Entry(root, width=15, textvariable=todo_content)
todo_textbox.pack(side=tk.RIGHT, fill=tk.Y)


add_item_button = tk.Button(root, text="Add Item")
add_item_button.pack(side=tk.RIGHT, fill=tk.Y)


del_item_button = tk.Button(root, text="Delete Item")
del_item_button.pack(side=tk.LEFT, fill=tk.Y)

