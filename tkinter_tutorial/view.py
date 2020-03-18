import tkinter as tk
from tkinter import ttk
from tkinter import font

# Create the root element, the parent of all our widgets
root = tk.Tk()

# Create a font Tkinter font to bind it to Listboxs
FONT = font.Font(family="Arial", size=20)
root.option_add("*Listbox*Font", FONT)


todo_list = tk.Listbox(root)  # Create the Listbox widget

scrollbarY = tk.Scrollbar(root, orient="vertical")  # Create the vertical scrollbar

# Bind it to the listbox
todo_list.config(yscrollcommand=scrollbarY.set)
scrollbarY.config(command=todo_list.yview)

# Same thing for the horizontal scrollbar
scrollbarX = tk.Scrollbar(root, orient="horizontal")

todo_list.config(xscrollcommand=scrollbarX.set)
scrollbarX.config(command=todo_list.xview)

# Create the textbox to enter the name of the new todo elements
todo_textbox = ttk.Entry(root, width=15)

# Create buttons
add_item_button = tk.Button(root, text="Add Item")

del_item_button = tk.Button(root, text="Delete Item")

# Pack all these element (Pack = organize the widget in the layout)
scrollbarY.pack(fill=tk.Y, side=tk.RIGHT)
scrollbarX.pack(fill=tk.X, side=tk.BOTTOM)

todo_list.pack()
todo_textbox.pack(side=tk.RIGHT, fill=tk.Y)

add_item_button.pack(side=tk.RIGHT, fill=tk.Y)
del_item_button.pack(side=tk.LEFT, fill=tk.Y)
