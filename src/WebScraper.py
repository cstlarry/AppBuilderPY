from tkinter import *
from tkinter import simpledialog
import requests
import re


# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = []


# add you code to the run method below:
def run():
    resp = requests.get("https://realpython.com")
    html = resp.text
    outputln(re.findall("python", html))


# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('800x600')
root.title('AppBuilder')

fields = [None] * (len(prompts))
row_num = 0

for index, prompt in enumerate(prompts):
    label = Label(root, text=prompt)
    label.grid(row=row_num, column=0, sticky=W)
    row_num += 2
    fields[index] = Entry(root, textvariable=f"{index}", width=100)
    fields[index].grid(row=row_num, column=0, padx=4, sticky=W)
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
