import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.geometry("600x400")
window.title("Football player Table")

label1 = tk.Label(window, text="Football Player Football")
label1.pack()

# tree view
cols = ("ID", "Name", "Gender", "Position")
table = ttk.Treeview(window, columns=cols, show="headings")
table.column("ID", width=80, anchor="center")
table.column("Name", width=180, anchor="center")
table.column("Gender", width=100, anchor="center")
table.column("Position", width=150, anchor="center")
# set heading to column
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Gender", text="Gender")
table.heading("Position", text="Position")

# table.insert('', "end", values=(1, "Keo Sreymich", "Female", "Defender"))
# table.insert('', "end", values=(2, "Khorn Sothean", "Male", "LB"))
data = [
    {"ID": 1, "Name": "Lionel Messi", "Gender": "Male", "Position": "Forward"},
    {"ID": 2, "Name": "Cristiano Ronaldo", "Gender": "Male", "Position": "Forward"},
    {"ID": 3, "Name": "Neymar Jr", "Gender": "Male", "Position": "Forward"},
    {"ID": 4, "Name": "Kylian Mbappé", "Gender": "Male", "Position": "Forward"},
    {"ID": 5, "Name": "Kevin De Bruyne", "Gender": "Male", "Position": "Midfielder"},
    {"ID": 6, "Name": "Luka Modrić", "Gender": "Male", "Position": "Midfielder"},
    {"ID": 7, "Name": "Virgil van Dijk", "Gender": "Male", "Position": "Defender"},
    {"ID": 8, "Name": "Erling Haaland", "Gender": "Male", "Position": "Forward"},
    {"ID": 9, "Name": "Alisson Becker", "Gender": "Male", "Position": "Goalkeeper"},
    {"ID": 10, "Name": "Robert Lewandowski", "Gender": "Male", "Position": "Forward"},
    {"ID": 11, "Name": "Harry Kane", "Gender": "Male", "Position": "Forward"},
    {"ID": 12, "Name": "Mohamed Salah", "Gender": "Male", "Position": "Forward"},
    {"ID": 13, "Name": "Karim Benzema", "Gender": "Male", "Position": "Forward"},
    {"ID": 14, "Name": "Joshua Kimmich", "Gender": "Male", "Position": "Midfielder"},
    {"ID": 15, "Name": "Jude Bellingham", "Gender": "Male", "Position": "Midfielder"},
    {"ID": 16, "Name": "Pedri", "Gender": "Male", "Position": "Midfielder"},
    {"ID": 17, "Name": "Thibaut Courtois", "Gender": "Male", "Position": "Goalkeeper"},
    {"ID": 18, "Name": "Vinícius Jr", "Gender": "Male", "Position": "Forward"},
    {"ID": 19, "Name": "Sergio Ramos", "Gender": "Male", "Position": "Defender"},
    {"ID": 20, "Name": "Trent Alexander-Arnold", "Gender": "Male", "Position": "Defender"}
]

for row in data:
    each_row = (row['ID'], row['Name'], row['Gender'], row['Position'])
    table.insert('', 'end', values=each_row)
    
table.pack()

window.mainloop()