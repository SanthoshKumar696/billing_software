import tkinter as tk
from tkinter import ttk, messagebox

# Functionality for buttons
def add_item():
    sl_no = len(tree.get_children()) + 1
    name = party_entry.get()
    transaction = transaction_combo.get()
    gross = gross_entry.get()
    melting = "-"
    net_weight = "-"
    mc = "-"

    if name and transaction and gross:
        tree.insert("", "end", values=(sl_no, name, transaction, gross, melting, net_weight, mc))
        party_entry.delete(0, tk.END)
        gross_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Please fill all required fields.")

def delete_item():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            tree.delete(item)
    else:
        messagebox.showerror("Selection Error", "Please select an item to delete.")

def save_items():
    items = tree.get_children()
    if items:
        with open("jewelry_data.csv", "w") as file:
            file.write("SLNo,Name,Transaction,Gross,Melting,Net Weight,MC\n")
            for item in items:
                values = tree.item(item, "values")
                file.write(",".join(values) + "\n")
        messagebox.showinfo("Save Success", "Data saved to jewelry_data.csv")
    else:
        messagebox.showerror("Save Error", "No data to save.")

# Initialize the main window
root = tk.Tk()
root.title("Jewelry Shop Management")
root.geometry("900x600")
root.configure(bg="lightpink")

# Header


cash_receipt_label = tk.Label(root, text="Cash Receipt", font=("Arial", 14, "bold"), bg="lightpink", fg="red")
cash_receipt_label.pack()

# Top frame for basic details
top_frame = tk.Frame(root, bg="lightpink")
top_frame.pack(pady=10)

tk.Label(top_frame, text="Date:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=0, padx=5)
date_entry = tk.Entry(top_frame, width=15)
date_entry.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Transaction:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=2, padx=5)
transaction_combo = ttk.Combobox(top_frame, values=["Cash Receipt", "Invoice", "Payment"], width=15)
transaction_combo.grid(row=0, column=3, padx=5)

party_label = tk.Label(top_frame, text="Party Name:", bg="lightpink", font=("Arial", 10))
party_label.grid(row=0, column=4, padx=5)
party_entry = tk.Entry(top_frame, width=20)
party_entry.grid(row=0, column=5, padx=5)

# Second frame for item details
item_frame = tk.Frame(root, bg="lightpink")
item_frame.pack(pady=10)

item_label = tk.Label(item_frame, text="Design:", bg="lightpink", font=("Arial", 10))
item_label.grid(row=0, column=0, padx=5)
item_combo = ttk.Combobox(item_frame, values=["24K GOLD LEAF", "22K Ring", "18K Necklace"], width=20)
item_combo.grid(row=0, column=1, padx=5)

# Fields for item details
tk.Label(item_frame, text="Gross Wt:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=2, padx=5)
gross_entry = tk.Entry(item_frame, width=10)
gross_entry.grid(row=0, column=3, padx=5)

tk.Label(item_frame, text="Stones:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=4, padx=5)
stones_entry = tk.Entry(item_frame, width=10)
stones_entry.grid(row=0, column=5, padx=5)

tk.Label(item_frame, text="Touch:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=6, padx=5)
touch_entry = tk.Entry(item_frame, width=10)
touch_entry.grid(row=0, column=7, padx=5)

# Table to display items
tree_frame = tk.Frame(root, bg="lightpink")
tree_frame.pack(pady=10)

columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

tree.heading("#1", text="SLNo")
tree.heading("#2", text="Name")
tree.heading("#3", text="Transaction")
tree.heading("#4", text="Gross")
tree.heading("#5", text="Melting")
tree.heading("#6", text="Net Weight")
tree.heading("#7", text="MC")

tree.column("#1", width=50, anchor=tk.CENTER)
tree.column("#2", width=100, anchor=tk.W)
tree.column("#3", width=100, anchor=tk.W)
tree.column("#4", width=80, anchor=tk.E)
tree.column("#5", width=80, anchor=tk.E)
tree.column("#6", width=100, anchor=tk.E)
tree.column("#7", width=80, anchor=tk.E)

tree.pack(fill="x", padx=20)

# Footer buttons
footer_frame = tk.Frame(root, bg="lightpink")
footer_frame.pack(pady=10)

tk.Button(footer_frame, text="Add", width=12, bg="green", fg="white", command=add_item).grid(row=0, column=0, padx=10)
tk.Button(footer_frame, text="Delete", width=12, bg="red", fg="white", command=delete_item).grid(row=0, column=1, padx=10)
tk.Button(footer_frame, text="Save", width=12, bg="blue", fg="white", command=save_items).grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
