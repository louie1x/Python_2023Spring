from tkinter import *
from tkinter import ttk

def show_detail_window():
    detail_window = Toplevel(root)
    detail_window.title('Detail Window')

    # Create Treeview
    columns = ('Product Name', 'Unit Price', 'Quantity', 'Subtotal')
    treeview = ttk.Treeview(detail_window, columns=columns, show='headings')
    treeview.pack()

    # Set headings and column styles
    for i, column in enumerate(columns):
        treeview.heading(i, text=column)
        if i == 0:
            treeview.column(i, width=250, anchor=CENTER)
        else:
            treeview.column(i, anchor=CENTER)

    # Set tag configure
    treeview.tag_configure('totalcolor', background='#E7E2E2')

    # Populate Treeview
    items = [
        {'name': 'Product 1', 'price': 10, 'quantity': 2},
        {'name': 'Product 2', 'price': 20, 'quantity': 3},
        {'name': 'Product 3', 'price': 30, 'quantity': 4},
        {'name': 'Product 4', 'price': 40, 'quantity': 5},
    ]

    total = 0
    for item in items:
        subtotal = item['price'] * item['quantity']
        treeview.insert('', END, values=(item['name'], item['price'], item['quantity'], subtotal))
        total += subtotal

    treeview.insert('', END, values=('Total', '', '', total), tags=('totalcolor',))
    
    detail_window.mainloop()

# Create main window
root = Tk()

# Create button
show_detail_button = Button(root, text='Show Detail', command=show_detail_window)
show_detail_button.pack()

root.mainloop()
