from tkinter import *
from tkinter import simpledialog
import random

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = []
fields = [None] * (len(prompts))
values = [""] * (len(prompts))

# add you code to the run method below:
def run():
    pass

# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('815x600')
root.title('AppBuilder')

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

def clearFields():
    if len(fields) > 0:
        for field in fields:
            field.delete(0, 'end')

def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n')

def output(text_to_output):
    display.insert(END, f'{text_to_output}')

frame = Frame(root)

row_num += 1

runButton = Button(frame, text="Run", command=run)
runButton.grid(row=row_num, column=0, ipadx=10, pady=5, padx=5)

clrOutput = Button(frame, text="Clear Output", command=clearOutput)
clrOutput.grid(row=row_num, column=1, ipadx=10, pady=5, padx=5)

clrFields = Button(frame, text="Clear Fields", command=clearFields)
clrFields.grid(row=row_num, column=2, ipadx=10, pady=5, padx=5)
if len(fields) > 0:
    clrFields.config(state='normal')
else:
    clrFields.config(state="disabled")

frame.grid(row=row_num, column=0)

row_num += 1
display = Text(root)
display.configure(font=("Courier", 12, "bold"))
display.grid(row=row_num, column=0, padx=4)

root.mainloop()

