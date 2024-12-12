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
    gross_wt = gross_wt_entry.get()
    stones = stones_entry.get()
    touch = touch_entry.get()
    net_wt = net_wt_entry.get()
    mc_at = mc_at_entry.get()
    mc = mc_entry.get()
    rate = rate_entry.get()
    amount = amount_entry.get()
    narration = narration_entry.get()

    if name and transaction and gross_wt:
        tree.insert("", "end", values=(sl_no, name, transaction, gross_wt, stones, touch, net_wt, mc_at, mc, rate, amount, narration))
        clear_fields()
    else:
        messagebox.showerror("Input Error", "Please fill all required fields.")

def delete_item():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showerror("Selection Error", "Please select an item to delete.")

def clear_fields():
    party_entry.delete(0, tk.END)
    gross_wt_entry.delete(0, tk.END)
    stones_entry.delete(0, tk.END)
    touch_entry.delete(0, tk.END)
    net_wt_entry.delete(0, tk.END)
    mc_at_entry.delete(0, tk.END)
    mc_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    narration_entry.delete(0, tk.END)


def save_items():
    items = tree.get_children()
    if items:
        with open("jewelry_data.csv", "w") as file:
            file.write("SLNo,Name,Transaction,Gross,Stones,Touch,Net Weight,MC@,MC,Rate,Amount,Narration\n")
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
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    ledger_window.geometry(f"{screen_width}x{screen_height}")
    
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
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    sub_ledger_window.geometry(f"{screen_width}x{screen_height}")
    
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
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    sub_ledger_window.geometry(f"{screen_width}x{screen_height}")
    
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
### main product master page ended

def open_sub_product():  #### start the sub product 
    # Create a new window for Main Ledger
    sub_ledger_window = tk.Toplevel(root)
    sub_ledger_window.title("Main Product Master")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    sub_ledger_window.geometry(f"{screen_width}x{screen_height}")
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
### sub product master page ended

def opening_stock():  ### start the opening stock   
    opening_stock_window = tk.Toplevel(root)
    opening_stock_window.title("Opening Stock")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    opening_stock_window.geometry(f"{screen_width}x{screen_height}")
    opening_stock_window.configure(bg="lightblue")

    # Variables for input fields
    operation_var = tk.StringVar(value="Correction")  # Default radio button selection
    main_product_var = tk.StringVar()  # Dropdown selection
    sub_product_var = tk.StringVar()  # Dropdown selection
    pcs_var = tk.StringVar()
    gross_wt_var = tk.StringVar()
    melting_var = tk.StringVar()
    net_wt_var = tk.StringVar()
    rate_var = tk.StringVar()
    mc_var = tk.StringVar()

    # First Line: Radio Buttons for Operations
    tk.Label(
        opening_stock_window,
        text="Select Operation:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    operations = ["Correction", "Deletion", "View"]
    for i, operation in enumerate(operations):
        tk.Radiobutton(
            opening_stock_window,
            text=operation,
            variable=operation_var,
            value=operation,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Second Line: Main Product Dropdown
    tk.Label(
        opening_stock_window,
        text="Main Product:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    main_product_options = ["Product 1", "Product 2", "Product 3"]  # Example options
    main_product_dropdown = ttk.Combobox(
        opening_stock_window,
        textvariable=main_product_var,
        values=main_product_options,
        state="readonly",
        width=30
    )
    main_product_dropdown.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Third Line: Sub Product Dropdown
    tk.Label(
        opening_stock_window,
        text="Sub Product:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    sub_product_options = ["Sub Product A", "Sub Product B", "Sub Product C"]  # Example options
    sub_product_dropdown = ttk.Combobox(
        opening_stock_window,
        textvariable=sub_product_var,
        values=sub_product_options,
        state="readonly",
        width=30
    )
    sub_product_dropdown.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Fourth Line: Pcs
    tk.Label(
        opening_stock_window,
        text="Pcs:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    pcs_entry = tk.Entry(
        opening_stock_window,
        textvariable=pcs_var,
        font=("Arial", 12),
        width=30
    )
    pcs_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    # Fifth Line: Gross Weight
    tk.Label(
        opening_stock_window,
        text="Gross Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

    gross_wt_entry = tk.Entry(
        opening_stock_window,
        textvariable=gross_wt_var,
        font=("Arial", 12),
        width=30
    )
    gross_wt_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    # Sixth Line: Melting Weight
    tk.Label(
        opening_stock_window,
        text="Melting Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    melting_entry = tk.Entry(
        opening_stock_window,
        textvariable=melting_var,
        font=("Arial", 12),
        width=30
    )
    melting_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

    # Seventh Line: Net Weight
    tk.Label(
        opening_stock_window,
        text="Net Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=6, column=0, sticky="w", padx=10, pady=10)

    net_wt_entry = tk.Entry(
        opening_stock_window,
        textvariable=net_wt_var,
        font=("Arial", 12),
        width=30
    )
    net_wt_entry.grid(row=6, column=1, columnspan=3, padx=10, pady=10)

    # Eighth Line: Rate
    tk.Label(
        opening_stock_window,
        text="Rate:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=7, column=0, sticky="w", padx=10, pady=10)

    rate_entry = tk.Entry(
        opening_stock_window,
        textvariable=rate_var,
        font=("Arial", 12),
        width=30
    )
    rate_entry.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

    # Ninth Line: MC@
    tk.Label(
        opening_stock_window,
        text="MC@: ",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=8, column=0, sticky="w", padx=10, pady=10)

    mc_entry = tk.Entry(
        opening_stock_window,
        textvariable=mc_var,
        font=("Arial", 12),
        width=30
    )
    mc_entry.grid(row=8, column=1, columnspan=3, padx=10, pady=10)

    # Function to save the entered details
    def save_entry():
        if (
            operation_var.get() and
            main_product_var.get() and
            sub_product_var.get() and
            pcs_var.get() and
            gross_wt_var.get() and
            melting_var.get() and
            net_wt_var.get() and
            rate_var.get() and
            mc_var.get()
        ):
            messagebox.showinfo("Saved", "Details Saved Successfully!")
        else:
            messagebox.showwarning("Missing Fields", "Please fill all the fields!")

    def cancel_entry():
        # Clear all fields
        operation_var.set("Correction")
        main_product_var.set("")
        sub_product_var.set("")
        pcs_var.set("")
        gross_wt_var.set("")
        melting_var.set("")
        net_wt_var.set("")
        rate_var.set("")
        mc_var.set("")

    # Buttons
    tk.Button(
        opening_stock_window,
        text="Save",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=save_entry
    ).grid(row=9, column=0, pady=20)

    tk.Button(
        opening_stock_window,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=cancel_entry
    ).grid(row=9, column=1, pady=20)

    tk.Button(
        opening_stock_window,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=opening_stock_window.destroy
    ).grid(row=9, column=2, pady=20)
### opening stock page ended    

def opening_balance():  ### start the opening balance  
    opening_stock_window = tk.Toplevel(root)
    opening_stock_window.title("Opening Balance")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    opening_stock_window.geometry(f"{screen_width}x{screen_height}")
    opening_stock_window.configure(bg="lightblue")

    # Variables for input fields
    operation_var = tk.StringVar(value="Correction")  # Default radio button selection
    main_product_var = tk.StringVar()  # Dropdown selection
    sub_product_var = tk.StringVar()  # Dropdown selection
    pcs_var = tk.StringVar()
    gross_wt_var = tk.StringVar()
    melting_var = tk.StringVar()
    net_wt_var = tk.StringVar()
    rate_var = tk.StringVar()
    mc_var = tk.StringVar()

    # First Line: Radio Buttons for Operations
    tk.Label(
        opening_stock_window,
        text="Select Operation:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    operations = ["Correction", "Deletion", "View"]
    for i, operation in enumerate(operations):
        tk.Radiobutton(
            opening_stock_window,
            text=operation,
            variable=operation_var,
            value=operation,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Second Line: Main Product Dropdown
    tk.Label(
        opening_stock_window,
        text="Main Product:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    main_product_options = ["Product 1", "Product 2", "Product 3"]  # Example options
    main_product_dropdown = ttk.Combobox(
        opening_stock_window,
        textvariable=main_product_var,
        values=main_product_options,
        state="readonly",
        width=30
    )
    main_product_dropdown.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    # Third Line: Sub Product Dropdown
    tk.Label(
        opening_stock_window,
        text="Sub Product:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    sub_product_options = ["Sub Product A", "Sub Product B", "Sub Product C"]  # Example options
    sub_product_dropdown = ttk.Combobox(
        opening_stock_window,
        textvariable=sub_product_var,
        values=sub_product_options,
        state="readonly",
        width=30
    )
    sub_product_dropdown.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    # Fourth Line: Pcs
    tk.Label(
        opening_stock_window,
        text="Pcs:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    pcs_entry = tk.Entry(
        opening_stock_window,
        textvariable=pcs_var,
        font=("Arial", 12),
        width=30
    )
    pcs_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=10)

    # Fifth Line: Gross Weight
    tk.Label(
        opening_stock_window,
        text="Gross Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

    gross_wt_entry = tk.Entry(
        opening_stock_window,
        textvariable=gross_wt_var,
        font=("Arial", 12),
        width=30
    )
    gross_wt_entry.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    # Sixth Line: Melting Weight
    tk.Label(
        opening_stock_window,
        text="Melting Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    melting_entry = tk.Entry(
        opening_stock_window,
        textvariable=melting_var,
        font=("Arial", 12),
        width=30
    )
    melting_entry.grid(row=5, column=1, columnspan=3, padx=10, pady=10)

    # Seventh Line: Net Weight
    tk.Label(
        opening_stock_window,
        text="Net Weight:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=6, column=0, sticky="w", padx=10, pady=10)

    net_wt_entry = tk.Entry(
        opening_stock_window,
        textvariable=net_wt_var,
        font=("Arial", 12),
        width=30
    )
    net_wt_entry.grid(row=6, column=1, columnspan=3, padx=10, pady=10)

    # Eighth Line: Rate
    tk.Label(
        opening_stock_window,
        text="Rate:",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=7, column=0, sticky="w", padx=10, pady=10)

    rate_entry = tk.Entry(
        opening_stock_window,
        textvariable=rate_var,
        font=("Arial", 12),
        width=30
    )
    rate_entry.grid(row=7, column=1, columnspan=3, padx=10, pady=10)

    # Ninth Line: MC@
    tk.Label(
        opening_stock_window,
        text="MC@: ",
        font=("Arial", 12),
        bg="lightblue"
    ).grid(row=8, column=0, sticky="w", padx=10, pady=10)

    mc_entry = tk.Entry(
        opening_stock_window,
        textvariable=mc_var,
        font=("Arial", 12),
        width=30
    )
    mc_entry.grid(row=8, column=1, columnspan=3, padx=10, pady=10)

    # Function to save the entered details
    def save_entry():
        if (
            operation_var.get() and
            main_product_var.get() and
            sub_product_var.get() and
            pcs_var.get() and
            gross_wt_var.get() and
            melting_var.get() and
            net_wt_var.get() and
            rate_var.get() and
            mc_var.get()
        ):
            messagebox.showinfo("Saved", "Details Saved Successfully!")
        else:
            messagebox.showwarning("Missing Fields", "Please fill all the fields!")

    def cancel_entry():
        # Clear all fields
        operation_var.set("Correction")
        main_product_var.set("")
        sub_product_var.set("")
        pcs_var.set("")
        gross_wt_var.set("")
        melting_var.set("")
        net_wt_var.set("")
        rate_var.set("")
        mc_var.set("")

    # Buttons
    tk.Button(
        opening_stock_window,
        text="Save",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=save_entry
    ).grid(row=9, column=0, pady=20)

    tk.Button(
        opening_stock_window,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=cancel_entry
    ).grid(row=9, column=1, pady=20)

    tk.Button(
        opening_stock_window,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=opening_stock_window.destroy
    ).grid(row=9, column=2, pady=20)
### opening balance page ended

def recepit_issue():
    pass

def day_book():   #### day book page start
     # Create a new window for Day Book
    day_book_window = tk.Toplevel(root)
    day_book_window.title("Day Book")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    day_book_window.geometry(f"{screen_width}x{screen_height}")
    day_book_window.configure(bg="lightblue")

    # Add a big and bold heading for Day Book
    tk.Label(
        day_book_window,
        text="Day Book",
        font=("Arial", 24, "bold"),
        bg="lightblue",
        fg="darkblue"
    ).pack(pady=10)

    # From Date input
    from_date_frame = tk.Frame(day_book_window, bg="lightblue")
    from_date_frame.pack(pady=10)

    tk.Label(
        from_date_frame,
        text="From Date:",
        font=("Arial", 14),
        bg="lightblue"
    ).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    from_date_entry = tk.Entry(from_date_frame, font=("Arial", 14), width=20)
    from_date_entry.grid(row=0, column=1, padx=5, pady=5)

    # To Date input
    to_date_frame = tk.Frame(day_book_window, bg="lightblue")
    to_date_frame.pack(pady=10)

    tk.Label(
        to_date_frame,
        text="To Date:",
        font=("Arial", 14),
        bg="lightblue"
    ).grid(row=0, column=0, padx=5, pady=5, sticky="w")

    to_date_entry = tk.Entry(to_date_frame, font=("Arial", 14), width=20)
    to_date_entry.grid(row=0, column=1, padx=5, pady=5)

    # Buttons
    button_frame = tk.Frame(day_book_window, bg="lightblue")
    button_frame.pack(pady=20)
    # Report Button
    tk.Button(
        button_frame,
        text="Report",
        font=("Arial", 12),
        bg="green",
        fg="white",
        width=10,
        command=lambda: print(f"Report generated for {from_date_entry.get()} to {to_date_entry.get()}")
    ).grid(row=0, column=0, padx=10)

    # Cancel Button
    tk.Button(
        button_frame,
        text="Cancel",
        font=("Arial", 12),
        bg="orange",
        fg="white",
        width=10,
        command=lambda: [from_date_entry.delete(0, tk.END), to_date_entry.delete(0, tk.END)]
    ).grid(row=0, column=1, padx=10)
     # Exit Button
    tk.Button(
        button_frame,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        width=10,
        command=day_book_window.destroy
    ).grid(row=0, column=2, padx=10)
### day book page ended

def party_ledger():   #### party ledger page start
    party_ledger_window = tk.Toplevel(root)
    party_ledger_window.title("Party Ledger")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    party_ledger_window.geometry(f"{screen_width}x{screen_height}")
    party_ledger_window.configure(bg="lightblue")

    tk.Label(
        party_ledger_window, text="Party Ledger",
        font=("Arial", 16, "bold"), bg="lightblue"
    ).grid(row=0, column=0, columnspan=5, pady=20)

    # Frame to group all options with a border
    options_frame = tk.Frame(party_ledger_window, bg="lightblue", bd=2, relief="groove")
    options_frame.grid(row=1, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")

    # Balance options
    tk.Label(
        options_frame, text="Select Ledger:", font=("Arial", 12, "bold"), bg="lightblue"
    ).grid(row=0, column=0, sticky="w", padx=10, pady=10)

    balance_var = tk.StringVar(value="Nil Bal")
    balance_options = ["Nil Bal", "Only Bal", "Both"]
    for i, option in enumerate(balance_options):
        tk.Radiobutton(
            options_frame, text=option, value=option,
            variable=balance_var, font=("Arial", 10), bg="lightblue"
        ).grid(row=0, column=i + 1, padx=10)

    # Account options
    tk.Label(
        options_frame, text="Select Account:", font=("Arial", 12, "bold"), bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    account_var = tk.StringVar(value="All A/C")
    account_options = ["All A/C", "Individual"]
    for i, option in enumerate(account_options):
        tk.Radiobutton(
            options_frame, text=option, value=option,
            variable=account_var, font=("Arial", 10), bg="lightblue"
        ).grid(row=1, column=i + 1, padx=10)

    # Stone options
    tk.Label(
        options_frame, text="Select Stone:", font=("Arial", 12, "bold"), bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    stone_var = tk.StringVar(value="Without St")
    stone_options = ["Without St", "With Stones", "Pcs/WO Touch", "Running"]
    for i, option in enumerate(stone_options):
        tk.Radiobutton(
            options_frame, text=option, value=option,
            variable=stone_var, font=("Arial", 10), bg="lightblue"
        ).grid(row=2, column=i + 1, padx=10)

    # Balance type options
    tk.Label(
        options_frame, text="Select Balance:", font=("Arial", 12, "bold"), bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    bal_var = tk.StringVar(value="With Opening Balance")
    bal_options = ["With Opening Balance", "Without Opening Balance"]
    for i, option in enumerate(bal_options):
        tk.Radiobutton(
            options_frame, text=option, value=option,
            variable=bal_var, font=("Arial", 10), bg="lightblue"
        ).grid(row=3, column=i + 1, padx=10)

    # Date options
    tk.Label(
        options_frame, text="Select Date:", font=("Arial", 12, "bold"), bg="lightblue"
    ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

    date_var = tk.StringVar(value="Monthly")
    date_options = ["Monthly", "Date Wise", "BillWise"]
    for i, option in enumerate(date_options):
        tk.Radiobutton(
            options_frame, text=option, value=option,
            variable=date_var, font=("Arial", 10), bg="lightblue"
        ).grid(row=4, column=i + 1, padx=10)

    # Date Inputs
    tk.Label(party_ledger_window, text="From Date:", font=("Arial", 14), bg="lightblue").grid(row=2, column=0, padx=10, pady=10)
    from_date_entry = tk.Entry(party_ledger_window, font=("Arial", 14), width=20)
    from_date_entry.grid(row=2, column=1)

    tk.Label(party_ledger_window, text="To Date:", font=("Arial", 14), bg="lightblue").grid(row=3, column=0, padx=10, pady=10)
    to_date_entry = tk.Entry(party_ledger_window, font=("Arial", 14), width=20)
    to_date_entry.grid(row=3, column=1)

    # Buttons
    tk.Button(
        party_ledger_window, text="Report", font=("Arial", 12), bg="green", fg="white",
        width=10, command=lambda: print(f"Generating report from {from_date_entry.get()} to {to_date_entry.get()}")
    ).grid(row=4, column=0, padx=10, pady=10)

    tk.Button(
        party_ledger_window, text="Cancel", font=("Arial", 12), bg="orange", fg="white",
        width=10, command=lambda: [from_date_entry.delete(0, tk.END), to_date_entry.delete(0, tk.END)]
    ).grid(row=4, column=1, padx=10, pady=10)

    tk.Button(
        party_ledger_window, text="Exit", font=("Arial", 12), bg="red", fg="white",
        width=10, command=party_ledger_window.destroy
    ).grid(row=4, column=2, padx=10, pady=10)
###  party ledger page ended

def party_balance(): #### party balance page start
    # Function to generate the report
    def generate_report():
        messagebox.showinfo("Report", "Generating report...")

    # Function to exit the application
    def exit_app():
        root.quit()

    # Create the main window for Party Balance
    party_balance_window = tk.Toplevel(root)
    party_balance_window.title("Party Balance")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    party_balance_window.geometry(f"{screen_width}x{screen_height}")
    party_balance_window.configure(bg="lightblue")

    # Variables for input fields
    ledger_var = tk.StringVar(value="all")  # Default radio button selection
    currency_var = tk.StringVar(value="Rs")
    balance_var = tk.StringVar(value="opening")
    columns_var = tk.StringVar(value="two")
    message_box_var = tk.StringVar()

    # First Line: Title
    tk.Label(
        party_balance_window,
        text="PARTY BALANCE",
        font=("Arial", 16, "bold"),
        bg="lightblue"
    ).grid(row=0, column=0, columnspan=4, pady=20)

    # Second Line: Radio Buttons for Ledger Selection
    tk.Label(
        party_balance_window,
        text="Select Ledger:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=1, column=0, sticky="w", padx=10, pady=10)

    ledger_options = ["All Ledger", "Individual Ledger"]
    for i, option in enumerate(ledger_options):
        tk.Radiobutton(
            party_balance_window,
            text=option,
            variable=ledger_var,
            value=option,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=1, column=i + 1, padx=10)

    # Third Line: Radio Buttons for Currency Selection
    tk.Label(
        party_balance_window,
        text="Select Currency:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=2, column=0, sticky="w", padx=10, pady=10)

    currency_options = ["Rs", "Metal", "Rs & Metal"]
    for i, option in enumerate(currency_options):
        tk.Radiobutton(
            party_balance_window,
            text=option,
            variable=currency_var,
            value=option,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=2, column=i + 1, padx=10)

    # Fourth Line: Radio Buttons for Balance Type
    tk.Label(
        party_balance_window,
        text="Select Balance Type:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=3, column=0, sticky="w", padx=10, pady=10)

    balance_options = ["Opening Bal", "Closing Bal"]
    for i, option in enumerate(balance_options):
        tk.Radiobutton(
            party_balance_window,
            text=option,
            variable=balance_var,
            value=option,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=3, column=i + 1, padx=10)

    # Fifth Line: Message Box
    tk.Label(
        party_balance_window,
        text="Enter Message:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=4, column=0, sticky="w", padx=10, pady=10)

    message_box = tk.Text(
        party_balance_window,
        height=3,
        width=50,
        wrap=tk.WORD
    )
    message_box.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

    # Sixth Line: Radio Buttons for Column Selection
    tk.Label(
        party_balance_window,
        text="Select Columns:",
        font=("Arial", 12, "bold"),
        bg="lightblue"
    ).grid(row=5, column=0, sticky="w", padx=10, pady=10)

    columns_options = ["Two Columns", "Three Columns"]
    for i, option in enumerate(columns_options):
        tk.Radiobutton(
            party_balance_window,
            text=option,
            variable=columns_var,
            value=option,
            font=("Arial", 10),
            bg="lightblue"
        ).grid(row=5, column=i + 1, padx=10)

    # Buttons for Report and Exit
    buttons_frame = tk.Frame(party_balance_window, bg="lightblue")
    buttons_frame.grid(row=6, column=0, columnspan=4, pady=20)

    report_button = tk.Button(
        buttons_frame,
        text="Report",
        font=("Arial", 12),
        command=generate_report
    )
    report_button.grid(row=0, column=0, padx=10)

    exit_button = tk.Button(
        buttons_frame,
        text="Exit",
        font=("Arial", 12),
        command=exit_app
    )
    exit_button.grid(row=0, column=1, padx=10)

    # Run the application
    party_balance_window.mainloop()
#### party balance page start


# Initialize the main window

root = tk.Tk()
root.title("Jewelry Management System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
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

#Master
# Adding submenu items to the Master menu
master_menu.add_command(label="Main Ledger", command=open_main_ledger)
master_menu.add_command(label="Sub Ledger", command=open_sub_ledger)
master_menu.add_command(label="Main Product", command=open_main_product)
master_menu.add_command(label="Sub Product", command=open_sub_product)
master_menu.add_command(label="Opening Stock", command=opening_stock) #######
master_menu.add_command(label="Party Opening Balance", command=opening_balance) #####

#Transaction
# Adding submenu items to the Trasaction menu
transaction_menu.add_command(label="Recepit & Issue", command=recepit_issue)

#Report
# Adding submenu items to the Report menu
report_menu.add_command(label="DayBook", command=day_book)
report_menu.add_command(label="PartyLedger", command=party_ledger)
report_menu.add_command(label="Party Balance", command=party_balance)

#Exit
exit_menu.add_command(label="Exit", command=exit_program)


# Header Label
cash_receipt_label = tk.Label(root, text="Cash Receipt", font=("Arial", 14, "bold"), bg="lightpink", fg="red")
cash_receipt_label.pack(pady=10)

# Top Frame - Row 1: Basic Details
top_frame = tk.Frame(root, bg="lightpink")
top_frame.pack(pady=5)

tk.Label(top_frame, text="Date:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=0, padx=5)
date_entry = tk.Entry(top_frame, width=15)
date_entry.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Transaction:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=2, padx=5)
transaction_combo = ttk.Combobox(top_frame, values=["Cash Receipt", "Invoice", "Payment"], width=15)
transaction_combo.grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Party Name:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=4, padx=5)
party_entry = tk.Entry(top_frame, width=20)
party_entry.grid(row=0, column=5, padx=5)

# Middle Frame - Row 2: Product Details
middle_frame = tk.Frame(root, bg="lightpink")
middle_frame.pack(pady=5)

tk.Label(middle_frame, text="Main Product:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=0, padx=5)
main_product_combo = ttk.Combobox(middle_frame, values=["GOLD", "SILVER", "DIAMOND"], width=20)
main_product_combo.grid(row=0, column=1, padx=5)

tk.Label(middle_frame, text="Sub Product:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=2, padx=5)
sub_product_combo = ttk.Combobox(middle_frame, values=["RING", "NECKLACE", "CHAIN"], width=20)
sub_product_combo.grid(row=0, column=3, padx=5)

tk.Label(middle_frame, text="Gross Wt:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=4, padx=5)
gross_wt_entry = tk.Entry(middle_frame, width=10)
gross_wt_entry.grid(row=0, column=5, padx=5)

tk.Label(middle_frame, text="Stones:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=6, padx=5)
stones_entry = tk.Entry(middle_frame, width=10)
stones_entry.grid(row=0, column=7, padx=5)


# Bottom Frame - Row 3: Additional Details
bottom_frame = tk.Frame(root, bg="lightpink")
bottom_frame.pack(pady=5)

tk.Label(bottom_frame, text="Touch:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=0, padx=5)
touch_entry = tk.Entry(bottom_frame, width=10)
touch_entry.grid(row=0, column=1, padx=5)

tk.Label(bottom_frame, text="Net Wt:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=2, padx=5)
net_wt_entry = tk.Entry(bottom_frame, width=10)
net_wt_entry.grid(row=0, column=3, padx=5)

tk.Label(bottom_frame, text="MC@:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=4, padx=5)
mc_at_entry = tk.Entry(bottom_frame, width=10)
mc_at_entry.grid(row=0, column=5, padx=5)

tk.Label(bottom_frame, text="MC:", bg="lightpink", font=("Arial", 10)).grid(row=0, column=6, padx=5)
mc_entry = tk.Entry(bottom_frame, width=10)
mc_entry.grid(row=0, column=7, padx=5)

tk.Label(bottom_frame, text="Rate:", bg="lightpink", font=("Arial", 10)).grid(row=1, column=0, padx=5)
rate_entry = tk.Entry(bottom_frame, width=10)
rate_entry.grid(row=1, column=1, padx=5)

tk.Label(bottom_frame, text="Amount:", bg="lightpink", font=("Arial", 10)).grid(row=1, column=2, padx=5)
amount_entry = tk.Entry(bottom_frame, width=10)
amount_entry.grid(row=1, column=3, padx=5)

tk.Label(bottom_frame, text="Narration:", bg="lightpink", font=("Arial", 10)).grid(row=1, column=4, padx=5)
narration_entry = tk.Entry(bottom_frame, width=30)
narration_entry.grid(row=1, column=5, padx=5, columnspan=3)

# Treeview Frame for Displaying Items
tree_frame = tk.Frame(root, bg="lightpink")
tree_frame.pack(pady=10, fill="both", expand=True)

columns = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11", "#12")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)

tree.heading("#1", text="SLNo")
tree.heading("#2", text="Name")
tree.heading("#3", text="Transaction")
tree.heading("#4", text="Gross")
tree.heading("#5", text="Stones")
tree.heading("#6", text="Touch")
tree.heading("#7", text="Net Wt")
tree.heading("#8", text="MC@")
tree.heading("#9", text="MC")
tree.heading("#10", text="Rate")
tree.heading("#11", text="Amount")
tree.heading("#12", text="Narration")


tree.column("#1", width=50, anchor=tk.CENTER)
for col in columns[1:]:
    tree.column(col, width=100, anchor=tk.W)

tree.pack(fill="both", expand=True)

# Footer Frame - Buttons
footer_frame = tk.Frame(root, bg="lightpink")
footer_frame.pack(pady=10)

tk.Button(footer_frame, text="Add", width=12, bg="green", fg="white", command=add_item).grid(row=0, column=0, padx=10)
tk.Button(footer_frame, text="Delete", width=12, bg="red", fg="white", command=delete_item).grid(row=0, column=1, padx=10)
tk.Button(footer_frame, text="Save", width=12, bg="blue", fg="white", command=save_items).grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
