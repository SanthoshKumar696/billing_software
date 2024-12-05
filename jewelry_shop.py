import tkinter as tk
from tkinter import messagebox, ttk

# Initialize main window
root = tk.Tk()
root.title("Jewelry Shop Management System")
root.geometry("600x400")

# Jewelry items list
jewelry_items = []

# Add new item to the list
def add_item():
    name = entry_name.get()
    category = combo_category.get()
    price = entry_price.get()

    if not name or not category or not price:
        messagebox.showerror("Input Error", "All fields are required.")
        return

    try:
        price = float(price)
    except ValueError:
        messagebox.showerror("Input Error", "Price must be a number.")
        return

    jewelry_items.append({"name": name, "category": category, "price": price})
    update_table()
    clear_inputs()

# Clear input fields
def clear_inputs():
    entry_name.delete(0, tk.END)
    combo_category.set("")
    entry_price.delete(0, tk.END)

# Update the table
def update_table():
    for row in tree.get_children():
        tree.delete(row)
    for idx, item in enumerate(jewelry_items):
        tree.insert("", "end", values=(idx + 1, item["name"], item["category"], f"${item['price']:.2f}"))

# Delete selected item
def delete_item():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "No item selected.")
        return
    item_index = int(tree.item(selected_item)["values"][0]) - 1
    del jewelry_items[item_index]
    update_table()

# Labels and input fields
label_title = tk.Label(root, text="Jewelry Shop Management", font=("Arial", 20, "bold"))
label_title.pack(pady=10)

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

label_name = tk.Label(frame_inputs, text="Item Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_inputs, width=20)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_category = tk.Label(frame_inputs, text="Category:")
label_category.grid(row=1, column=0, padx=5, pady=5)
combo_category = ttk.Combobox(frame_inputs, values=["Necklace", "Ring", "Bracelet", "Earring"], width=18)
combo_category.grid(row=1, column=1, padx=5, pady=5)

label_price = tk.Label(frame_inputs, text="Price ($):")
label_price.grid(row=2, column=0, padx=5, pady=5)
entry_price = tk.Entry(frame_inputs, width=20)
entry_price.grid(row=2, column=1, padx=5, pady=5)

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add Item", command=add_item, width=15, bg="green", fg="white")
btn_add.grid(row=0, column=0, padx=10)

btn_delete = tk.Button(frame_buttons, text="Delete Item", command=delete_item, width=15, bg="red", fg="white")
btn_delete.grid(row=0, column=1, padx=10)

# Table to display jewelry items
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("#1", "#2", "#3", "#4")
tree = ttk.Treeview(frame_table, columns=columns, show="headings", height=10)
tree.heading("#1", text="ID")
tree.heading("#2", text="Item Name")
tree.heading("#3", text="Category")
tree.heading("#4", text="Price")
tree.column("#1", width=50, anchor=tk.CENTER)
tree.column("#2", width=150, anchor=tk.W)
tree.column("#3", width=100, anchor=tk.CENTER)
tree.column("#4", width=80, anchor=tk.E)
tree.pack()

# Run the application
root.mainloop()
