import requests 
from tkinter import *
from tkhtmlview import *
from tkinter import filedialog


def test(url_entry, option, text_widget):
    url = requests.get(url_entry)
    # Pas ndryshimit te formes rikthehet text ne 0 
    text_widget.delete(1.0, END)
    # Add your logic to handle the URL
    if option == 'HTML Structure':
        # Shfaqja e HTML-it ne nje dritare te re
        a1 = Tk()
        a1.title('webS Raw HTML')
        a1.geometry('1000x700')  
        HTMLLabel(a1, html=url.text).pack(fill="both", expand=True)
        a1.mainloop()
    elif option == 'HTML Code':
        text_widget.insert("1.0", url.text)
    elif option == 'JSON':
        try:
            json_data = url.json()
            text_widget.insert("1.0", json_data)
        except ValueError:
            text_widget.insert("1.0", "Invalid JSON data")
    else:
        print('Error')

def save(text_widget):
    # Zgjedhja e vendit te shkrakimit
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        # importimi i datave nga text.widget
        content = text_widget.get("1.0", END)

        with open(file_path, "w") as file:
            file.write(content)


a = Tk()
a.title('webS')
a.geometry('1000x700') 

# krijmi i pozicjonev
left_frame = Frame(a)
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame = Frame(a)
right_frame.grid(row=0, column=1, sticky="nsew")

# instalimi i gridave per pozicjon 
a.grid_columnconfigure(0, weight=3)
a.grid_columnconfigure(1, weight=7)
a.grid_rowconfigure(0, weight=1)

# Input per link
Label(left_frame, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = Entry(left_frame)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Button per aktivizim te scrapit
Button(left_frame, text='Scrap URL', command=lambda: test(url_entry.get(), selected_file_type.get(), text_widget)).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Menu per zgjehje te formes se scrapit
file_types = ['HTML Structure', 'HTML Code', 'JSON']
selected_file_type = StringVar(left_frame)
selected_file_type.set(file_types[0]) 
OptionMenu(left_frame, selected_file_type, *file_types).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Button to save content
Button(left_frame, text='Save', command=lambda: save(text_widget)).grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Vend per paraqitje te dataes
text_widget = Text(right_frame)
text_widget.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# scroll per text
scrollbar = Scrollbar(right_frame, command=text_widget.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
text_widget.config(yscrollcommand=scrollbar.set)

# Konfigurmi i te dhanave 
right_frame.grid_rowconfigure(0, weight=1)
right_frame.grid_columnconfigure(0, weight=1)

a.mainloop()
