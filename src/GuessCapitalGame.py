from tkinter import *
from tkinter import simpledialog
import random

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = []


# add you code to the run method below:
def run():
    capitals_dict = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne",
    }

    state, capital = random.choice(list(capitals_dict.items()))

    while True:
        question = f"What is the capital of '{state}'? "
        guess = simpledialog.askstring("Enter your answer", question)

        if guess == "exit":
            outputln(f"The capital of '{state}' is '{capital}'.")
            outputln("Goodbye")
            break
        elif guess.lower() == capital.lower():
            outputln("Correct! Nice job.")
            break


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
