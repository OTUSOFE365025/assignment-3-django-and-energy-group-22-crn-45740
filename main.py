import os
import django
import tkinter as tk
from tkinter import messagebox, ttk

# --- Django ORM setup ---
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()
# ------------------------

from db.models import Product


def populate_products():
    """Populate the database with a set of sample products."""
    sample_data = [
        ("123456789012", "Milk", 2.49),
        ("987654321098", "Bread", 3.19),
        ("111111111111", "Eggs", 4.79),
        ("222222222222", "Butter", 5.25),
        ("333333333333", "Cheese", 6.49),
        ("444444444444", "Apples (1 lb bag)", 3.99),
        ("555555555555", "Bananas (1 lb)", 1.59),
        ("666666666666", "Orange Juice", 4.29),
        ("777777777777", "Cereal", 5.99),
        ("888888888888", "Toothpaste", 2.89),
        ("999999999999", "Soap Bar", 1.49),
        ("101010101010", "Shampoo", 6.75),
    ]
    for upc, name, price in sample_data:
        Product.objects.get_or_create(upc=upc, defaults={"name": name, "price": price})


# --- Global subtotal variable ---
subtotal = 0.0


def scan_product():
    """Search for a product based on entered UPC."""
    global subtotal
    code = upc_entry.get().strip()
    if not code:
        messagebox.showwarning("Warning", "Please enter a UPC code.")
        return

    product = Product.objects.filter(upc=code).first()
    if product:
        # Add price to subtotal
        subtotal += float(product.price)
        result_label.config(
            text=f"Product: {product.name}\nPrice: ${product.price:.2f}", fg="green"
        )
        subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")

        # Add to the item list
        items_list.insert("", "end", values=(product.name, f"${product.price:.2f}"))

    else:
        result_label.config(text="Product not found.", fg="red")

    # Clear the UPC box after 2 seconds
    root.after(2000, lambda: upc_entry.delete(0, tk.END))
    # Clear the result label after 3 seconds
    root.after(3000, lambda: result_label.config(text=""))


def reset_transaction():
    """Clear all items and reset subtotal."""
    global subtotal
    subtotal = 0.0
    subtotal_label.config(text="Subtotal: $0.00")
    for row in items_list.get_children():
        items_list.delete(row)
    result_label.config(text="")
    upc_entry.delete(0, tk.END)


# --- GUI Setup ---
root = tk.Tk()
root.title("Cash Register (Django ORM)")
root.geometry("420x450")
root.resizable(False, False)

tk.Label(root, text="Enter Product UPC:", font=("Arial", 12)).pack(pady=10)
upc_entry = tk.Entry(root, font=("Arial", 12), justify="center")
upc_entry.pack(pady=5)

scan_button = tk.Button(
    root, text="Scan", font=("Arial", 12), bg="#0078D7", fg="white", command=scan_product
)
scan_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=5)

subtotal_label = tk.Label(root, text="Subtotal: $0.00", font=("Arial", 12, "bold"))
subtotal_label.pack(pady=10)

# --- Item List Section ---
list_frame = tk.Frame(root)
list_frame.pack(pady=5)

columns = ("Item", "Price")
items_list = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)
items_list.heading("Item", text="Item")
items_list.heading("Price", text="Price")
items_list.column("Item", width=220, anchor="center")
items_list.column("Price", width=100, anchor="center")
items_list.pack(side="left")

# Add scrollbar
scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=items_list.yview)
items_list.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# --- Reset Button ---
reset_button = tk.Button(
    root,
    text="Clear Transaction",
    font=("Arial", 11),
    bg="#E81123",
    fg="white",
    command=reset_transaction,
)
reset_button.pack(pady=10)

populate_products()
root.mainloop()
