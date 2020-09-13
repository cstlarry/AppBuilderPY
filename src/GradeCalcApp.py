from tkinter import *
from tkinter import simpledialog
import random
import pickle

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter Name",
           "Enter space-separated quiz scores",
           "Enter space-separated project scores",
           "Enter Attendance score",
           "Enter Final Exam score"]
fields = [None] * (len(prompts))
values = [""] * (len(prompts))

weights = {"Quiz": 0.25, "Project": 0.25, "Attend": 0.25, "Final": 0.25}

# file = open("state", 'rb')
# pickle.dump(score_type, file)
# score_type = pickle.load(file)
# file.close()


# add you code to the run method below:
def run():
    outputln(weights)
    name = fields[0].get()

    quiz_scores = fields[1].get().strip().split(" ")
    quiz_avg = get_average(quiz_scores)
    quiz_avg = quiz_avg * weights.get('Quiz')

    proj_scores = fields[2].get().strip().split(" ")
    proj_avg = get_average(proj_scores)
    proj_avg = proj_avg * weights.get("Project")

    attend_score = float(fields[3].get().strip())
    attend_score = attend_score * weights.get("Attend")

    final_score = float(fields[4].get().strip())
    final_score = final_score * weights.get("Final")

    over_all_avg = quiz_avg + proj_avg + attend_score + final_score

    grade = get_letter_grade(over_all_avg)

    outputln(f"{name}\t\t{over_all_avg: .2f}\t{grade}")


# **************** Put helper methods below *********************
def get_average(score_list):
    score_list = [float(i) for i in score_list]
    return sum(score_list) / len(score_list)

def get_letter_grade(score):
    grade = "F"
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    return grade

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
