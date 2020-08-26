from tkinter import *
# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter Wage:", "Enter Hours Worked:"]

# add you code to the run method below:
def run():
    wage = float(fields[0].get())
    hours = float(fields[1].get())
    pay = hours * wage
    outputln(f'You earned ${pay: .2f}')

# **************** Put helper methods below *********************

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
tkWindow = Tk()
tkWindow.geometry('990x600')
tkWindow.title('AppBuilder')

fields = [None] * len(prompts)
row_num = 0

for prompt in prompts:
    label = Label(tkWindow, text=prompt)
    label.grid(row=row_num, column=0)
    fields[row_num] = Entry(tkWindow, textvariable=f"{row_num}", width=100)
    fields[row_num].grid(row=row_num, column=1)
    row_num += 1

runButton = Button(tkWindow, text="Run", command=run)
runButton.grid(row=row_num, column=1, ipadx=10)

row_num += 1
display = Text(tkWindow)
display.configure(font=("Courier", 12, "bold"))
display.grid(row=row_num, column=1)

def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n')

def output(text_to_output):
    display.insert(END, f'{text_to_output}')

tkWindow.mainloop()

