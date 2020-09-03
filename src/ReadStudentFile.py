from tkinter import *
from tkinter import simpledialog
import random
from collections import namedtuple
import csv

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter filename"]
fields = [None] * (len(prompts))
values = ["StudentList.csv"]  # * (len(prompts))

# SID	STUDENT`S NAME	DAY PHONE 	EVENING PHONE 	EMAIL
StudentRecord = namedtuple('StudentRecord', 'sid, name, day_phone, evening_phone, email')

# add you code to the run method below:
def run():
    filename = fields[0].get()
    students = map(StudentRecord._make, csv.reader(open(filename, 'r')))
    for student in students:
        names = student.name.split(" ")
        full_name = names[1] + " " + names[0]
        phone = student.day_phone
        email = student.email
        outputln(f'{full_name:<25}{phone:>12}{email:>35}')

# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('815x600')
root.title('Read Text File Example')

row_num = 0

for index, prompt in enumerate(prompts):
    label = Label(root, text=prompt)
    label.grid(row=row_num, column=0, sticky=W)
    row_num += 2
    fields[index] = Entry(root, textvariable=f"{index}", width=100)
    fields[index].grid(row=row_num, column=0, padx=4, sticky=W)
    fields[index].insert(0, values[index])
    if index == 0:
        fields[index].focus_set()
    row_num += 1

def clearOutput():
    display.delete("1.0", "end")

def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n')

def output(text_to_output):
    display.insert(END, f'{text_to_output}')

buttonFrame = Frame(root)

row_num += 1

runButton = Button(buttonFrame, text="Run", command=run)
runButton.grid(row=row_num, column=0, ipadx=10, pady=5)

clrButton = Button(buttonFrame, text="Clear Output", command=clearOutput)
clrButton.grid(row=row_num, column=1, ipadx=10, pady=5)

buttonFrame.grid(row=row_num, column=0)

row_num += 1
display = Text(root)
display.configure(font=("Courier", 12, "bold"))
display.grid(row=row_num, column=0, padx=4)

root.mainloop()
