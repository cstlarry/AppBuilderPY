from tkinter import *
from tkinter import simpledialog
import random

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter a comma separated list of words", "Enter a space separated list of test scores"]
fields = [None] * (len(prompts))
values = ["All, fish, play, in, the, blue, ocean", "60 70 80 90 100"]  # * (len(prompts))


# Write a program that accepts a comma separated sequence of words as input and prints
# the words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program: without,hello,bag,world Then, the output
# should be: bag,hello,without,world
def run():
    # items = [x for x in simpledialog.askstring("Create Sorted CSV", "Enter comma separated words").split(',')]
    input = fields[0].get()
    striped = ''.join(input.split()) # remove all spaces from input
    items = [x for x in striped.split(',')]
    items.sort()
    outputln(','.join(items))
    # calculate the average of a comma separated list of test scores
    scores = [x for x in fields[1].get().split(' ')]
    scores = [float(i) for i in scores]
    average = sum(scores) / len(scores)
    outputln(f'The average of {scores} is {average}')

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


def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n')


def output(text_to_output):
    display.insert(END, f'{text_to_output}')


frame = Frame(root)

row_num += 1

runButton = Button(frame, text="Run", command=run)
runButton.grid(row=row_num, column=0, ipadx=10, pady=5)

clrButton = Button(frame, text="Clear Output", command=clearOutput)
clrButton.grid(row=row_num, column=1, ipadx=10, pady=5)

frame.grid(row=row_num, column=0)

row_num += 1
display = Text(root)
display.configure(font=("Courier", 12, "bold"))
display.grid(row=row_num, column=0, padx=4)

root.mainloop()
