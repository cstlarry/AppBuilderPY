from tkinter import *
prompts = ["Wage"]
fields = [None] * len(prompts)


def run():
    text = fields[0].get()
    num = float(text)
    outputln(f'{num: .2f}')

tkWindow = Tk()
tkWindow.geometry('990x600')
tkWindow.title('AppBuilder')

row_num = 0

for prompt in prompts:
    label = Label(tkWindow, text=prompt, justify=LEFT)
    label.grid(row=row_num, column=0)
    fields[row_num] = Entry(tkWindow, textvariable=f"{row_num}", width=100)
    fields[row_num].grid(row=row_num, column=1)
    row_num += 1

runButton = Button(tkWindow, text="Run", command=run).grid(row=row_num, column=0)

row_num += 1
display = Text(tkWindow)
display.configure(font=("Courier", 12, "bold"))
display.grid(row=row_num, column=1)

def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n')

def output(text_to_output):
    display.insert(END, f'{text_to_output}')

tkWindow.mainloop()

