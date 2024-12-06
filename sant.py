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

# Function to handle exit menu action
def exit_program():
    root.quit()

# Function to open the Main Ledger page
def open_main_ledger():
    # Create a new window for Main Ledger
    ledger_window = tk.Toplevel(root)
    ledger_window.title("Main Ledger")
    ledger_window.geometry("800x600")
    ledger_window.configure(bg="lightblue")
    
    # Add content for last month's calculations
    tk.Label(
        ledger_window, 
        text="Main Ledger - Last Month's Calculations", 
        font=("Arial", 16, "bold"), 
        bg="lightblue", 
        fg="darkblue"
    ).pack(pady=10)

    # Example data table
    table_frame = tk.Frame(ledger_window, bg="lightblue")
    table_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Create a Treeview for displaying data
    columns = ("#1", "#2", "#3", "#4", "#5")
    ledger_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

    ledger_tree.heading("#1", text="Date")
    ledger_tree.heading("#2", text="Party Name")
    ledger_tree.heading("#3", text="Transaction Type")
    ledger_tree.heading("#4", text="Amount")
    ledger_tree.heading("#5", text="Remarks")

    ledger_tree.column("#1", width=100, anchor=tk.CENTER)
    ledger_tree.column("#2", width=200, anchor=tk.W)
    ledger_tree.column("#3", width=150, anchor=tk.W)
    ledger_tree.column("#4", width=100, anchor=tk.E)
    ledger_tree.column("#5", width=250, anchor=tk.W)

    # Insert sample data (Replace with actual logic to fetch data)
    sample_data = [
        ("01-11-2024", "Balaji", "Cash Receipt", "10000", "Gold Purchase"),
        ("02-11-2024", "Santhosh", "Invoice", "15000", "Payment for Necklace"),
        ("03-11-2024", "Dinesh", "Payment", "20000", "Advance Payment"),
    ]
    for row in sample_data:
        ledger_tree.insert("", "end", values=row)

    ledger_tree.pack(fill="both", expand=True)

    # Add a button to close the ledger window
    tk.Button(
        ledger_window, 
        text="Close", 
        width=12, 
        bg="red", 
        fg="white", 
        command=ledger_window.destroy
    ).pack(pady=10)




# Initialize the main window
root = tk.Tk()
root.title("Jewelry Shop Management")
root.geometry("900x600")
root.configure(bg="lightpink")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add menu items
master_menu = tk.Menu(menu_bar, tearoff=0)
transaction_menu = tk.Menu(menu_bar, tearoff=0)
report_menu = tk.Menu(menu_bar, tearoff=0)
utility_menu = tk.Menu(menu_bar, tearoff=0)
exit_menu = tk.Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Master", menu=master_menu)
menu_bar.add_cascade(label="Transaction", menu=transaction_menu)
menu_bar.add_cascade(label="Report", menu=report_menu)
menu_bar.add_cascade(label="Utility", menu=utility_menu)
menu_bar.add_cascade(label="Exit", menu=exit_menu)

exit_menu.add_command(label="Exit", command=exit_program)

#Master
# Adding submenu items to the Master menu
master_menu.add_command(label="Main Ledger", command=open_main_ledger)
master_menu.add_command(label="Sub Ledger", command=lambda: messagebox.showinfo("Action", "Sub Ledger clicked"))
master_menu.add_command(label="Main Product", command=lambda: messagebox.showinfo("Action", "Main Product clicked"))
master_menu.add_command(label="Sub Product", command=lambda: messagebox.showinfo("Action", "Sub Product clicked"))
master_menu.add_command(label="Opening Stock", command=lambda: messagebox.showinfo("Action", "Opening Stock clicked"))
master_menu.add_command(label="Party Opening Balance", command=lambda: messagebox.showinfo("Action", "Party Opening Balance clicked"))
master_menu.add_command(label="Delete Opening Balance by Group", command=lambda: messagebox.showinfo("Action", "Delete Opening Balance by Group clicked"))
master_menu.add_command(label="Zero Balance", command=lambda: messagebox.showinfo("Action", "Zero Balance clicked"))
master_menu.add_command(label="Price List", command=lambda: messagebox.showinfo("Action", "Price List clicked"))
master_menu.add_command(label="Party PriceList By Sub Product", command=lambda: messagebox.showinfo("Action", "Party PriceList By Sub Product clicked"))
master_menu.add_command(label="Party PriceList By Design", command=lambda: messagebox.showinfo("Action", "Party PriceList By Design clicked"))
master_menu.add_command(label="Product Merge", command=lambda: messagebox.showinfo("Action", "Product Merge clicked"))
master_menu.add_command(label="Account Merge", command=lambda: messagebox.showinfo("Action", "Account Merge clicked"))
master_menu.add_command(label="Design Merge", command=lambda: messagebox.showinfo("Action", "Design Merge clicked"))
master_menu.add_command(label="Rate Cut OB", command=lambda: messagebox.showinfo("Action", "Rate Cut OB clicked"))



#Transaction
# Adding submenu items to the Trasaction menu
transaction_menu.add_command(label="Recepit & Issue", command=lambda: messagebox.showinfo("Action", "Recepit & Issue clicked"))
transaction_menu.add_command(label="Journal", command=lambda: messagebox.showinfo("Action", "Journal clicked"))
transaction_menu.add_command(label="Bill", command=lambda: messagebox.showinfo("Action", "Bill clicked"))
transaction_menu.add_command(label="Product Conversion", command=lambda: messagebox.showinfo("Action", "Product Conversion clicked"))
transaction_menu.add_command(label="Tally & Conformation Date", command=lambda: messagebox.showinfo("Action", "Tally & Conformation Date clicked"))
transaction_menu.add_command(label="Stock Valuvation", command=lambda: messagebox.showinfo("Action", "Stock Valuvation clicked"))

#Report
# Adding submenu items to the Report menu
report_menu.add_command(label="DayBook", command=lambda: messagebox.showinfo("Action", "DayBook clicked"))
report_menu.add_command(label="PartyLedger", command=lambda: messagebox.showinfo("Action", "PartyLedger clicked"))
report_menu.add_command(label="Trail Balance", command=lambda: messagebox.showinfo("Action", "Trail Balance clicked"))
report_menu.add_command(label="Party Balance", command=lambda: messagebox.showinfo("Action", "Party Balance clicked"))
report_menu.add_command(label="Stock", command=lambda: messagebox.showinfo("Action", "Stock clicked"))
report_menu.add_command(label="Purchase & Sales Books", command=lambda: messagebox.showinfo("Action", "Purchase & Sales Books clicked"))
report_menu.add_command(label="MIS", command=lambda: messagebox.showinfo("Action", "MIS clicked"))
report_menu.add_command(label="Books", command=lambda: messagebox.showinfo("Action", "Books clicked"))
report_menu.add_command(label="Adjustment Details", command=lambda: messagebox.showinfo("Action", "Adjustment Details clicked"))
report_menu.add_command(label="Aging Analysis", command=lambda: messagebox.showinfo("Action", "Aging Analysis clicked"))
report_menu.add_command(label="Intrest", command=lambda: messagebox.showinfo("Action", "Intrest clicked"))
report_menu.add_command(label="Excel File For Adjustment Details", command=lambda: messagebox.showinfo("Action", "Excel File For Adjustment Details clicked"))


#Utility
# Adding submenu items to the Utility menu
utility_menu.add_command(label="Year Change", command=lambda: messagebox.showinfo("Action", "Year Change clicked"))
utility_menu.add_command(label="New Company", command=lambda: messagebox.showinfo("Action", "New Company clicked"))
utility_menu.add_command(label="Company Change", command=lambda: messagebox.showinfo("Action", "Company Change clicked"))
utility_menu.add_command(label="Year End", command=lambda: messagebox.showinfo("Action", "Year End clicked"))
utility_menu.add_command(label="Update Party Balance", command=lambda: messagebox.showinfo("Action", "Update Party Balance clicked"))
utility_menu.add_command(label="End Date Change", command=lambda: messagebox.showinfo("Action", "End Date Change clicked"))
utility_menu.add_command(label="Ageing To OB", command=lambda: messagebox.showinfo("Action", "Ageing To OB clicked"))
utility_menu.add_command(label="Delete All Adjustment", command=lambda: messagebox.showinfo("Action", "Delete All Adjustment clicked"))
utility_menu.add_command(label="Merge with Previous Data", command=lambda: messagebox.showinfo("Action", "Merge with Previous Data clicked"))
utility_menu.add_command(label="Merge From Daily", command=lambda: messagebox.showinfo("Action", "Merge From Daily clicked"))
utility_menu.add_command(label="Delete Openeing BillDetails", command=lambda: messagebox.showinfo("Action", "Delete Openeing BillDetails clicked"))
utility_menu.add_command(label="VouNo", command=lambda: messagebox.showinfo("Action", "VouNo clicked"))
utility_menu.add_command(label="Compare", command=lambda: messagebox.showinfo("Action", "Compare clicked"))
utility_menu.add_command(label="Change Password", command=lambda: messagebox.showinfo("Action", "Change Password clicked"))
utility_menu.add_command(label="Memory", command=lambda: messagebox.showinfo("Action", "Memory clicked"))
utility_menu.add_command(label="Calcalutor", command=lambda: messagebox.showinfo("Action", "Calcalutor clicked"))
utility_menu.add_command(label="Update Tables", command=lambda: messagebox.showinfo("Action", "Update Tables clicked"))




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
