from tkinter import *
from tkinter import simpledialog

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter First Integer:",
           "Enter Operator [ + - * /]:",
           "Enter Second Integer:"]

# add you code to the run method below:
def run():
    n1 = int(fields[0].get())
    operator = fields[1].get()
    n2 = int(fields[2].get())

    result = 0
    remainder = ""

    if operator == "+":
        result = n1 + n2
    elif operator == "-":
        result = n1 - n2
    elif operator == "*":
        result = n1 * n2
    elif operator == "/":
        result = n1 // n2
        remainder = "remainder " + str(n1 % n2)
    else:
        outputln('Invalid operator')

    outputln(f'{n1} {operator} {n2} = {result} {remainder}')

# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('815x600')
root.title('Integer Calc')

fields = [None] * (len(prompts))
row_num = 0

for index, prompt in enumerate(prompts):
    label = Label(root, text=prompt)
    label.grid(row=row_num, column=0, sticky=W)
    row_num += 2
    fields[index] = Entry(root, textvariable=f"{index}", width=100)
    fields[index].grid(row=row_num, column=0, sticky=W, padx=4)
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

