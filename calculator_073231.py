import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    new_text = current_text + str(button_value)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)
    
def clear_entry():
    entry.delete(0, tk.END)
    
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
        
# Create the main window
root = tk.Tk()
root.title("TKinter Calculator")

#Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4)

#Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '.', '0', '=', '+',
]

#Add buttons to the grid
row_val = 1
col_val = 0

for button_value in buttons:
    tk.Button(root, text=button_value, width=5, height=2, command=lambda value=button_value: on_click(value)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#Clear button
tk.Button(root, text='C', width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)

#Equal button
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=row_val, column=col_val + 1)

#Run the Tkinter event loop
root.mainloop()