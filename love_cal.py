from tkinter import *
import random

root = Tk()
root.geometry('500x350')
root.title('Love Calculator????')

def calculate_love():
    name1_value = name1.get().lower()
    name2_value = name2.get().lower()
    common_letters = set(name1_value) & set(name2_value)
    love_percentage = int((len(common_letters) / len(set(name1_value + name2_value))) * 100)
    result.config(text=f'Love Percentage between both of You: {love_percentage}%')

# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she into you', font=('Arial', 18, 'bold'))
heading.pack(pady=20)

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:", font=('Arial', 12))
slot1.pack()
name1 = Entry(root, border=5, width=30, font=('Arial', 12))
name1.pack(pady=10)

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:", font=('Arial', 12))
slot2.pack()
name2 = Entry(root, border=5, width=30, font=('Arial', 12))
name2.pack(pady=10)

bt = Button(root, text="Calculate", height=1, width=10, command=calculate_love, font=('Arial', 12), bg='lightblue')
bt.pack(pady=10)

# Text on result slot
result = Label(root, text='Love Percentage between both of You:', font=('Arial', 12))
result.pack(pady=10)

root.mainloop()