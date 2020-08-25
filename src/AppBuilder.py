from tkinter import *
prompts = ["Name"]
fields = [None] * len(prompts)

def run():
    outputln(fields[0].get())

tkWindow = Tk()
tkWindow.geometry('800x600')
tkWindow.title('AppBuilder')

row_num = 0

for prompt in prompts:
    label = Label(tkWindow, text=prompt).grid(row=row_num, column=0)
    fields[row_num] = Entry(tkWindow, textvariable="field", width=100)
    fields[row_num].grid(row=row_num, column=1)
    row_num += 1

runButton = Button(tkWindow, text="Run", command=run).grid(row=row_num, column=0)

row_num +=  1
display = Text(tkWindow)
display.grid(row=row_num, column=1, rowspan=2)

def outputln(text_to_output):
    display.insert(END, f'{text_to_output}\n', 'big')

def output(text_to_output):
    display.insert(END, f'{text_to_output}', 'big')

tkWindow.mainloop()

