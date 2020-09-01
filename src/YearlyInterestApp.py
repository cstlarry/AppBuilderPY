from tkinter import *
from tkinter import simpledialog
import random

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Principal", "Interest Rate", "Term (number of years)"]
fields = [None] * (len(prompts))
values = [1000, .08, 5]  # * (len(prompts))


# add you code to the run method below:
def run():
    principal = float(fields[0].get())
    rate = float(fields[1].get())
    term = int(fields[2].get())
    year = 1

    while year <= term:
        interest = principal * rate
        principal = principal + interest
        outputln(f"Year-{year} Principal:\t${principal:<10,.2f}")
        year = year + 1


# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('815x600')
root.title('Yearly Interest Calculator')

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
