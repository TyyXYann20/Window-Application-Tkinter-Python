import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry("900x600")
window.title("Sample UI")

# global
style = ttk.Style()

style.configure('TButton', font=("Arial", 12))
style.map('TButton', foreground=[('pressed', 'red')],
          )
style.map('insertBtn.TButton', foreground=[('pressed', 'blue')],
          )

#define column for root window
window.columnconfigure(0, weight=1)
window.rowconfigure((0, 2), weight=1)
window.rowconfigure(1, weight=2)
#Input Frame
inputFrame = tk.Frame(window, bg="#f2f2f2")
inputFrame.grid(row=0, column=0, padx=20, pady=10, sticky="news")
# Define row and col in inputFrame
inputFrame.columnconfigure((0, 1, 2), weight=1)
inputFrame.rowconfigure((0,1,2,3,4), weight=1)

entry_width = 25
# Create Label
ttk.Label(inputFrame, text="Product Code").grid(row=0, column=0)
ttk.Label(inputFrame, text="Vendor").grid(row=0, column=1)
ttk.Label(inputFrame, text="Product Name").grid(row=0, column=2)
ttk.Label(inputFrame, text="Quantity").grid(row=2, column=0)
ttk.Label(inputFrame, text="Price").grid(row=2, column=1)
ttk.Label(inputFrame, text="Currency").grid(row=2, column=2)
#Create Input box(Entry)
ttk.Entry(inputFrame, width=entry_width).grid(row=1, column=0)
ttk.Entry(inputFrame, width=entry_width).grid(row=1, column=1)
ttk.Entry(inputFrame,width=entry_width).grid(row=1, column=2)
# Row 4
qty_spinbox = ttk.Spinbox(inputFrame, from_=1, to=999, width=entry_width, 
                            increment=0.5)
price_spinbox = ttk.Spinbox(inputFrame, from_=1, to=99999, width=entry_width, 
                            increment=0.5)
currency_options = [
    "៛ រៀល (KHR)",
    "$ ដុល្លារ (USD)",
    "€ អឺរ៉ូ (EUR)",
    "¥ យេន (JPY)",
    "£ ផោន (GBP)",
    "₩ វុន (KRW)"
]


currencyBox = ttk.Combobox(inputFrame, values=currency_options,
                           width=entry_width, state="readonly")
currencyBox.set("៛ រៀល (KHR)")

qty_spinbox.grid(row=3, column=0)
price_spinbox.grid(row=3, column=1)
currencyBox.grid(row=3, column=2)
ttk.Button(inputFrame, text="Add Product", cursor="hand2", style="insertBtn.TButton").grid(row=4, column=2, sticky="e",
                                                                padx=80, ipadx=5, ipady=5)

#TreeviewFrame
tableFrame = tk.Frame(window, bg="#f2f2f2")
tableFrame.rowconfigure(0, weight=1)
tableFrame.columnconfigure(0, weight=1)
tableFrame.grid(row=1, column=0, sticky="news")

style.configure('Treeview', foreground="black",  background="white",
                font=('Arial', 11))
style.configure('Treeview.Heading', foreground="green", font=('Arial', 11),
                background="red")

cols = ('ID', 'Product Name', 'Price', 'Quantity')
table = ttk.Treeview(tableFrame, columns=cols, show='headings')
# table.column('ID', width=100)
# table.column('Product Name', width=180)
# table.column('Price', width=100)
# table.column('Quantity', width=100)

table.heading('ID', text='ID')
table.heading('Product Name', text='Product Name')
table.heading('Price', text='Price')
table.heading('Quantity', text='Quantity')
table.grid(row=0, column=0)
products = [
    {"id": "P001", "name": "ទឹកសុទ្ធប៉េអិល", "price": "1500៛", "qty": "10"},
    {"id": "P002", "name": "ម្ជូរមាន់", "price": "5000៛", "qty": "5"},
    {"id": "P003", "name": "សាប៊ូកក់សក់", "price": "3500៛", "qty": "8"},
    {"id": "P004", "name": "បាយសរ 1គីឡូ", "price": "3000៛", "qty": "12"},
    {"id": "P005", "name": "ទឹកត្នោត", "price": "2000៛", "qty": "6"},
    {"id": "P006", "name": "កាហ្វេកក", "price": "2$", "qty": "15"},
    {"id": "P007", "name": "ខោជើងខ្លីបុរស", "price": "8$", "qty": "9"},
    {"id": "P008", "name": "សៀវភៅ", "price": "2500៛", "qty": "20"},
    {"id": "P009", "name": "ខ្យល់បាញ់", "price": "4$", "qty": "7"},
    {"id": "P010", "name": "ម្សៅជូរត្រាំ", "price": "1200៛", "qty": "18"},
]

for product in products:
    row = (product['id'], product['name'], product['price'], product['qty'])
    table.insert('', 'end', values=row)
    
    
    
buttonFrame = tk.Frame(window, bg="#9b9696")   
buttonFrame.grid(row=2, column=0, sticky="news")
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.rowconfigure((0, 1), weight=1)

ttk.Button(buttonFrame, text="Print Invoice", cursor="hand2").grid(row=0, column=0, sticky="news",
                                                   ipadx=10, ipady=10,)
ttk.Button(buttonFrame, text="New Invoice", cursor="hand2").grid(row=1, column=0,
                                                sticky="news", ipady=5,
                                                ipadx=10)
    

window.mainloop()
