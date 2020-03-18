import tkinter as tk
from tkinter import font

root = tk.Tk()
FONT = font.Font(family="Arial", size=20)
root.option_add("*Listbox*Font", FONT)


todo_list = tk.Listbox(root)

scrollbarY = tk.Scrollbar(root, orient="vertical")
scrollbarY.pack(fill=tk.Y, side=tk.RIGHT)
todo_list.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=todo_list.yview)

scrollbarX = tk.Scrollbar(root, orient="horizontal")
scrollbarX.pack(fill=tk.X, side=tk.BOTTOM)
todo_list.config(xscrollcommand=scrollbarX.set)
scrollbarX.config(command=todo_list.xview)

todo_list.pack()


todo_textbox = tk.Entry(root, width=15)
todo_textbox.pack(side=tk.RIGHT, fill=tk.Y)


add_item_button = tk.Button(root, text="Add Item")
add_item_button.pack(side=tk.RIGHT, fill=tk.Y)


del_item_button = tk.Button(root, text="Delete Item")
del_item_button.pack(side=tk.LEFT, fill=tk.Y)
