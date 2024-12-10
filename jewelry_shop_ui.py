import tkinter as tk
from tkinter import ttk, messagebox

# Function to handle exit menu action
def exit_program():
    root.quit()

# Functionality for buttons

def add_item():
    sl_no = len(tree.get_children()) + 1
    name = party_entry.get()
    transaction = transaction_combo.get()
    gross = gross_entry.get()
    melting = "-"
    net_weight = "-"
    mc = "-"
    amount=amount_entry.get()


    if name and transaction and gross:
        tree.insert("", "end", values=(sl_no, name, transaction, int(gross)*2, melting, net_weight, mc, amount))
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
            file.write("SLNo,Name,Transaction,Gross,Melting,Net Weight,MC,Amount\n")
            for item in items:
                values = tree.item(item, "values")
                file.write(",".join(values) + "\n")
        messagebox.showinfo("Save Success", "Data saved to jewelry_data.csv")
    else:
        messagebox.showerror("Save Error", "No data to save.")

def open_main_ledger():
    # Create a new window for Main Ledger
    ledger_window = tk.Toplevel(root)
    ledger_window.title("Main Ledger")
    ledger_window.geometry("800x600")
    ledger_window.configure(bg="lightblue")

    # Frame for the left section (Radio Buttons and Inputs)
    left_frame = tk.Frame(ledger_window, bg="lightblue")
    left_frame.pack(side="left", fill="y", padx=10, pady=10)

    # Radio Button Options
    operation_var = tk.StringVar(value="Addition")  # Default selection
    tk.Label(
        left_frame, 
        text="Select Operation:", 
        font=("Arial", 12), 
        bg="lightblue"
    ).pack(anchor="w", padx=10, pady=5)

    for operation in ["Addition", "Correction", "Deletion", "View"]:
        tk.Radiobutton(
            left_frame, 
            text=operation, 
            variable=operation_var, 
            value=operation, 
            font=("Arial", 10), 
            bg="lightblue"
        ).pack(anchor="w", padx=20)

    # Input for Code
    tk.Label(
        left_frame, 
        text="Code:", 
        font=("Arial", 12), 
        bg="lightblue"
    ).pack(anchor="w", padx=10, pady=5)

    code_entry = tk.Entry(left_frame, width=30, font=("Arial", 12))
    code_entry.pack(padx=10, pady=5)

    # Input for Name
    tk.Label(
        left_frame, 
        text="Name:", 
        font=("Arial", 12), 
        bg="lightblue"
    ).pack(anchor="w", padx=10, pady=5)

    name_entry = tk.Entry(left_frame, width=30, font=("Arial", 12))
    name_entry.pack(padx=10, pady=5)

    # Save button functionality
    def save_entry():
        code = code_entry.get().strip()
        name = name_entry.get().strip()
        if code and name:
            stored_details_tree.insert("", "end", values=(code, name))
            code_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both Code and Name")

    # Buttons
    tk.Button(
        left_frame, 
        text="Save", 
        font=("Arial", 12), 
        bg="green", 
        fg="white", 
        width=10, 
        command=save_entry
    ).pack(pady=10)

    tk.Button(
        left_frame, 
        text="Cancel", 
        font=("Arial", 12), 
        bg="orange", 
        fg="white", 
        width=10, 
        command=lambda: [code_entry.delete(0, tk.END), name_entry.delete(0, tk.END)]
    ).pack(pady=5)

    tk.Button(
        left_frame, 
        text="Exit", 
        font=("Arial", 12), 
        bg="red", 
        fg="white", 
        width=10, 
        command=ledger_window.destroy
    ).pack(pady=5)

    # Frame for the right section (Stored Details Table)
    right_frame = tk.Frame(ledger_window, bg="lightblue")
    right_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

    tk.Label(
        right_frame, 
        text="Stored Details", 
        font=("Arial", 12, "bold"), 
        bg="lightblue"
    ).pack(pady=10)

    # Treeview (Table) for displaying stored details
    columns = ("Code", "Name")
    stored_details_tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=20)
    stored_details_tree.heading("Code", text="Code")
    stored_details_tree.heading("Name", text="Name")
    stored_details_tree.column("Code", width=100, anchor="center")
    stored_details_tree.column("Name", width=200, anchor="w")
    stored_details_tree.pack(fill="both", expand=True, padx=10)

    # Preloaded data
    stored_data = [
        ("101", "Balaji"),
        ("102", "Santhosh"),
        ("103", "Dinesh"),
    ]

    for item in stored_data:
        stored_details_tree.insert("", "end", values=item)
    
    

    
    

    # Add a button to close the ledger window
    
####### main ledger page ended

def open_sub_ledger(): ### start the sub ledger page

    # Create a new window for Sub Ledger
    sub_ledger_window = tk.Toplevel(root)
    sub_ledger_window.title("Sub Ledger")
    sub_ledger_window.geometry("1000x600")
    sub_ledger_window.configure(bg="lightblue")

    # Variables for input fields
    operation_var = tk.StringVar(value="Addition")  # Default radio button selection
    main_ledger_var = tk.StringVar()  # Dropdown selection
    code_var = tk.StringVar()
    name_var = tk.StringVar()
    credit_period_var = tk.StringVar()
    last_name_var = tk.StringVar()

    # First Line: Radio Buttons for Operations
    tk.Label(
        sub_ledger_window,
        text="Select Operation:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    operations = ["Addition", "Correction", "Deletion", "View"]
    for i, operation in enumerate(operations):
        tk.Radiobutton(
            sub_ledger_window,
            text=operation,
            variable=operation_var,
            value=operation,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Second Line: Main Ledger Dropdown
    tk.Label(
        sub_ledger_window,
        text="Main Ledger:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    main_ledger_options = ["Ledger 1", "Ledger 2", "Ledger 3"]  # Example options
    main_ledger_dropdown = ttk.Combobox(
        sub_ledger_window,
        textvariable=main_ledger_var,
        values=main_ledger_options,
        state="readonly",
        width=30
    )
    main_ledger_dropdown.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Third Line: Code
    tk.Label(
        sub_ledger_window,
        text="Code:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    code_entry = tk.Entry(
        sub_ledger_window,
        textvariable=code_var,
        font=("Arial", 12),
        width=30
    )
    code_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Fourth Line: Name
    tk.Label(
        sub_ledger_window,
        text="Name:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    name_entry = tk.Entry(
        sub_ledger_window,
        textvariable=name_var,
        font=("Arial", 12),
        width=30
    )
    name_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    # Fifth Line: Credit Period
    tk.Label(
        sub_ledger_window,
        text="Credit Period (Days):",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

    credit_period_entry = tk.Entry(
        sub_ledger_window,
        textvariable=credit_period_var,
        font=("Arial", 12),
        width=30
    )
    credit_period_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    # Sixth Line: Last Name
    tk.Label(
        sub_ledger_window,
        text="Last Name:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    last_name_entry = tk.Entry(
        sub_ledger_window,
        textvariable=last_name_var,
        font=("Arial", 12),
        width=30
    )
    last_name_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

    # Right-side Frame to Show Entered Details
    details_frame = tk.Frame(sub_ledger_window, bg="lightgray", width=400, height=300)
    details_frame.grid(row=0, column=4, rowspan=7, padx=20, pady=10)

    # Function to update and display entered details in the right-side box
    def display_entered_details():
        # Get the entered values
        operation = operation_var.get()
        main_ledger = main_ledger_var.get()
        code = code_var.get()
        name = name_var.get()
        credit_period = credit_period_var.get()
        last_name = last_name_var.get()

        # Clear previous details
        for widget in details_frame.winfo_children():
            widget.destroy()

        # Display the new details in a label
        details_label = tk.Label(
            details_frame,
            text=f"Operation: {operation}\n"
                 f"Main Ledger: {main_ledger}\n"
                 f"Code: {code}\n"
                 f"Name: {name}\n"
                 f"Credit Period: {credit_period} days\n"
                 f"Last Name: {last_name}",
            font=("Arial", 12),
            bg="lightgray",
            justify="left"
        )
        details_label.pack(padx=10, pady=10)

    # Button Actions
    def save_entry():
        if (
            operation_var.get() and
            main_ledger_var.get() and
            code_var.get() and
            name_var.get() and
            credit_period_var.get() and
            last_name_var.get()
        ):
            messagebox.showinfo("Saved", "Details Saved Successfully!")
            display_entered_details()
        else:
            messagebox.showwarning("Missing Fields", "Please fill all the fields!")

    def cancel_entry():
        # Clear all fields
        operation_var.set("Addition")
        main_ledger_var.set("")
        code_var.set("")
        name_var.set("")
        credit_period_var.set("")
        last_name_var.set("")

    # Buttons
    tk.Button(
        sub_ledger_window,
        text="Save",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=save_entry
    ).grid(row=6, column=0, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=cancel_entry
    ).grid(row=6, column=1, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=sub_ledger_window.destroy
    ).grid(row=6, column=2, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Name List",
        font=("Arial", 12),
        bg="blue",
        fg="white",
        width=10,
        command=lambda: messagebox.showinfo("Name List", "Display the name list logic here.")
    ).grid(row=6, column=3, pady=20)

    ##### sub ledger page ended
### sub ledger page ended

def open_main_product(): #### main product page start
    # Create a new window for Main Ledger
    sub_ledger_window = tk.Toplevel(root)
    sub_ledger_window.title("Main Product Master")
    sub_ledger_window.geometry("1000x600")
    sub_ledger_window.configure(bg="lightblue")

    # Variables for input fields
    operation_var = tk.StringVar(value="Addition")  # Default radio button selection
    main_ledger_var = tk.StringVar()  # Dropdown selection
    code_var = tk.StringVar()
    name_var = tk.StringVar()
    

    # First Line: Radio Buttons for Operations
    tk.Label(
        sub_ledger_window,
        text="Select Operation:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    operations = ["Addition", "Correction", "Deletion", "View"]
    for i, operation in enumerate(operations):
        tk.Radiobutton(
            sub_ledger_window,
            text=operation,
            variable=operation_var,
            value=operation,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Second Line: Main Ledger Dropdown
    

    # Third Line: Code
    tk.Label(
        sub_ledger_window,
        text="Code:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    code_entry = tk.Entry(
        sub_ledger_window,
        textvariable=code_var,
        font=("Arial", 12),
        width=30
    )
    code_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Fourth Line: Name
    tk.Label(
        sub_ledger_window,
        text="Name:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    name_entry = tk.Entry(
        sub_ledger_window,
        textvariable=name_var,
        font=("Arial", 12),
        width=30
    )
    name_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)


    # Right-side Frame to Show Entered Details
    details_frame = tk.Frame(sub_ledger_window, bg="lightgray", width=400, height=300)
    details_frame.grid(row=0, column=4, rowspan=7, padx=20, pady=10)

    # Function to update and display entered details in the right-side box
    def display_entered_details():
        # Get the entered values
        operation = operation_var.get()
        main_ledger = main_ledger_var.get()
        code = code_var.get()
        name = name_var.get()
        

        # Clear previous details
        for widget in details_frame.winfo_children():
            widget.destroy()

        # Display the new details in a label
        details_label = tk.Label(
            details_frame,
            text=f"Operation: {operation}\n"
                 f"Code: {code}\n"
                 f"Name: {name}\n",
            font=("Arial", 12),
            bg="lightgray",
            justify="left"
        )
        details_label.pack(padx=10, pady=10)

    # Button Actions
    def save_entry():
        if (
            operation_var.get() and
            main_ledger_var.get() and
            code_var.get() and
            name_var.get() 
        ):
            messagebox.showinfo("Saved", "Details Saved Successfully!")
            display_entered_details()
        else:
            messagebox.showwarning("Missing Fields", "Please fill all the fields!")

    def cancel_entry():
        # Clear all fields
        operation_var.set("Addition")
        main_ledger_var.set("")
        code_var.set("")
        name_var.set("")
        

    # Buttons
    tk.Button(
        sub_ledger_window,
        text="Save",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=save_entry
    ).grid(row=6, column=0, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=cancel_entry
    ).grid(row=6, column=1, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=sub_ledger_window.destroy
    ).grid(row=6, column=2, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Name List",
        font=("Arial", 12),
        bg="blue",
        fg="white",
        width=10,
        command=lambda: messagebox.showinfo("Name List", "Display the name list logic here.")
    ).grid(row=6, column=3, pady=20)
    ##### end the main product ended

def open_sub_product():  #### start the sub product 
    # Create a new window for Main Ledger
    sub_ledger_window = tk.Toplevel(root)
    sub_ledger_window.title("Main Product Master")
    sub_ledger_window.geometry("1000x600")
    sub_ledger_window.configure(bg="lightblue")

    # Variables for input fields
    operation_var = tk.StringVar(value="Addition")  # Default radio button selection
    main_ledger_var = tk.StringVar()  # Dropdown selection
    code_var = tk.StringVar()
    name_var = tk.StringVar()
    

    # First Line: Radio Buttons for Operations
    tk.Label(
        sub_ledger_window,
        text="Select Operation:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    operations = ["Addition", "Correction", "Deletion", "View"]
    for i, operation in enumerate(operations):
        tk.Radiobutton(
            sub_ledger_window,
            text=operation,
            variable=operation_var,
            value=operation,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Second Line: Main Ledger Dropdown
    tk.Label(
        sub_ledger_window,
        text="Main Ledger:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    main_ledger_options = ["Ledger 1", "Ledger 2", "Ledger 3"]  # Example options
    main_ledger_dropdown = ttk.Combobox(
        sub_ledger_window,
        textvariable=main_ledger_var,
        values=main_ledger_options,
        state="readonly",
        width=30
    )
    main_ledger_dropdown.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Third Line: Code
    tk.Label(
        sub_ledger_window,
        text="Code:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    code_entry = tk.Entry(
        sub_ledger_window,
        textvariable=code_var,
        font=("Arial", 12),
        width=30
    )
    code_entry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Fourth Line: Name
    tk.Label(
        sub_ledger_window,
        text="Name:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    name_entry = tk.Entry(
        sub_ledger_window,
        textvariable=name_var,
        font=("Arial", 12),
        width=30
    )
    name_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)


    # Right-side Frame to Show Entered Details
    details_frame = tk.Frame(sub_ledger_window, bg="lightgray", width=400, height=300)
    details_frame.grid(row=0, column=4, rowspan=7, padx=20, pady=10)

    # Function to update and display entered details in the right-side box
    def display_entered_details():
        # Get the entered values
        operation = operation_var.get()
        main_ledger = main_ledger_var.get()
        code = code_var.get()
        name = name_var.get()
        

        # Clear previous details
        for widget in details_frame.winfo_children():
            widget.destroy()

        # Display the new details in a label
        details_label = tk.Label(
            details_frame,
            text=f"Operation: {operation}\n"
                 f"Main Ledger: {main_ledger}\n"
                 f"Code: {code}\n"
                 f"Name: {name}\n",
            font=("Arial", 12),
            bg="lightgray",
            justify="left"
        )
        details_label.pack(padx=10, pady=10)

    # Button Actions
    def save_entry():
        if (
            operation_var.get() and
            main_ledger_var.get() and
            code_var.get() and
            name_var.get() 
        ):
            messagebox.showinfo("Saved", "Details Saved Successfully!")
            display_entered_details()
        else:
            messagebox.showwarning("Missing Fields", "Please fill all the fields!")

    def cancel_entry():
        # Clear all fields
        operation_var.set("Addition")
        main_ledger_var.set("")
        code_var.set("")
        name_var.set("")
        

    # Buttons
    tk.Button(
        sub_ledger_window,
        text="Save",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=save_entry
    ).grid(row=6, column=0, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=cancel_entry
    ).grid(row=6, column=1, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=sub_ledger_window.destroy
    ).grid(row=6, column=2, pady=20)

    tk.Button(
        sub_ledger_window,
        text="Name List",
        font=("Arial", 12),
        bg="blue",
        fg="white",
        width=10,
        command=lambda: messagebox.showinfo("Name List", "Display the name list logic here.")
    ).grid(row=6, column=3, pady=20)
    ##### end the sub product ended 


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
master_menu.add_command(label="Sub Ledger", command=open_sub_ledger)
master_menu.add_command(label="Main Product", command=open_main_product)
master_menu.add_command(label="Sub Product", command=open_sub_product)
master_menu.add_command(label="Opening Stock", command=lambda: messagebox.showinfo("Action", "Opening Stock clicked")) #######
master_menu.add_command(label="Party Opening Balance", command=lambda: messagebox.showinfo("Action", "Party Opening Balance clicked"))
master_menu.add_command(label="Delete Opening Balance by Group", command=lambda: messagebox.showinfo("Action", "Delete Opening Balance by Group clicked"))

#Transaction
# Adding submenu items to the Trasaction menu
transaction_menu.add_command(label="Recepit & Issue", command=lambda: messagebox.showinfo("Action", "Recepit & Issue clicked"))

#Report
# Adding submenu items to the Report menu
report_menu.add_command(label="DayBook", command=lambda: messagebox.showinfo("Action", "DayBook clicked"))
report_menu.add_command(label="PartyLedger", command=lambda: messagebox.showinfo("Action", "PartyLedger clicked"))
report_menu.add_command(label="Trail Balance", command=lambda: messagebox.showinfo("Action", "Trail Balance clicked"))
report_menu.add_command(label="Party Balance", command=lambda: messagebox.showinfo("Action", "Party Balance clicked"))
report_menu.add_command(label="Stock", command=lambda: messagebox.showinfo("Action", "Stock clicked"))

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

item_label = tk.Label(item_frame, text="Main Product:", bg="lightpink", font=("Arial", 10))
item_label.grid(row=0, column=0, padx=5)
item_combo = ttk.Combobox(item_frame, values=["GOLD", "SILVER", "DIAMOND"], width=20)
item_combo.grid(row=0, column=1, padx=5)

item_label = tk.Label(item_frame, text="Sub Product:", bg="lightpink", font=("Arial", 10))
item_label.grid(row=0, column=2, padx=5)
item_combo = ttk.Combobox(item_frame, values=["RING", "NECKLACE", "CHAIN"], width=20)
item_combo.grid(row=0, column=3, padx=5)

# Fields for item details
tk.Label(item_frame, text="Gross Wt:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=4, padx=5)
gross_entry = tk.Entry(item_frame, width=10)
gross_entry.grid(row=0, column=5, padx=5)

tk.Label(item_frame, text="Stones:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=6, padx=5)
stones_entry = tk.Entry(item_frame, width=10)
stones_entry.grid(row=0, column=7, padx=5)

tk.Label(item_frame, text="Touch:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=8, padx=5)
touch_entry = tk.Entry(item_frame, width=10)
touch_entry.grid(row=0, column=9, padx=5)




########## Add the amount column
tk.Label(item_frame, text="NetWT:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=10, padx=5)
amount_entry = tk.Entry(item_frame, width=10)
amount_entry.grid(row=0, column=11, padx=5)
##########




# Table to display items
tree_frame = tk.Frame(root, bg="lightpink")
tree_frame.pack(pady=10)


tk.Label(tree_frame, text="MC@:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=1, padx=5)
gross_entry = tk.Entry(tree_frame, width=10)
gross_entry.grid(row=0, column=2, padx=5)

tk.Label(tree_frame, text="MC:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=3, padx=5)
stones_entry = tk.Entry(item_frame, width=10)
stones_entry.grid(row=0, column=4, padx=5)

tk.Label(tree_frame, text="Rate:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=5, padx=5)
touch_entry = tk.Entry(tree_frame, width=10)
touch_entry.grid(row=0, column=6, padx=5)

tk.Label(tree_frame, text="Amount:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=7, padx=5)
gross_entry = tk.Entry(tree_frame, width=10)
gross_entry.grid(row=0, column=8, padx=5)

tk.Label(tree_frame, text="SNo:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=9, padx=5)
stones_entry = tk.Entry(item_frame, width=10)
stones_entry.grid(row=0, column=10, padx=5)

tk.Label(tree_frame, text="Narration:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=11, padx=5)
touch_entry = tk.Entry(tree_frame, width=10)
touch_entry.grid(row=0, column=12, padx=5)


# Table to display items
tree_frame = tk.Frame(root, bg="lightpink")
tree_frame.pack(pady=10)

columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12", "#13", "#14")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

tree.heading("#1", text="SLNo")
tree.heading("#2", text="Name")
tree.heading("#3", text="Transaction")
tree.heading("#4", text="Gross")
tree.heading("#5", text="Melting")
tree.heading("#6", text="Net Weight")
tree.heading("#7", text="MC")
tree.heading("#8", text="Amount")
tree.heading("#9", text="Melting")
tree.heading("#10", text="Net weight")
tree.heading("#11", text="MC")
tree.heading("#12", text="Amount")
tree.heading("#13", text="Product Name")
tree.heading("#14", text="Narration")

tree.column("#1", width=50, anchor=tk.CENTER)
tree.column("#2", width=100, anchor=tk.W)
tree.column("#3", width=100, anchor=tk.W)
tree.column("#4", width=80, anchor=tk.W)
tree.column("#5", width=80, anchor=tk.W)
tree.column("#6", width=100, anchor=tk.W)
tree.column("#7", width=80, anchor=tk.W)
tree.column("#8", width=70, anchor=tk.W)
tree.column("#9", width=100, anchor=tk.W)
tree.column("#10", width=100, anchor=tk.W)
tree.column("#11", width=80, anchor=tk.W)
tree.column("#12", width=80, anchor=tk.W)
tree.column("#13", width=100, anchor=tk.W)
tree.column("#14", width=80, anchor=tk.W)

# Add tree to grid
tree.grid(row=1, column=0, columnspan=13, sticky="nsew", padx=20, pady=10)

# Configure grid weights
tree_frame.grid_rowconfigure(1, weight=1)
tree_frame.grid_columnconfigure(0, weight=1)





tree.grid(row=1, column=0, columnspan=13, sticky="nsew", padx=20, pady=10)
tree_frame.grid_rowconfigure(1, weight=1)  # Allow row 1 to expand
tree_frame.grid_columnconfigure(0, weight=1)  # Allow column 0 to expand



# Footer buttons
footer_frame = tk.Frame(root, bg="lightpink")
footer_frame.pack(pady=10)

tk.Button(footer_frame, text="Add", width=12, bg="green", fg="white", command=add_item).grid(row=0, column=0, padx=10)
tk.Button(footer_frame, text="Delete", width=12, bg="red", fg="white", command=delete_item).grid(row=0, column=1, padx=10)
tk.Button(footer_frame, text="Save", width=12, bg="blue", fg="white", command=save_items).grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
