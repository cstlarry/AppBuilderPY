from tkinter import *
from tkinter import simpledialog
import requests

# Example of how to use the line below: prompts = ["Enter Wage", "Enter Hours Worked"]
prompts = ["Enter City, State"]
fields = [None] * (len(prompts))

# add you code to the run method below:
def run():
    clearOutput()
    city = fields[0].get()
    outputln(get_data(city))


# **************** Put helper methods below *********************
def get_data(city):
    api_key = "8e6944794cf74fd7e36158135dd675fd"
    url = "https://api.openweathermap.org/data/2.5/weather/"
    arguments = {"APPID": api_key, "q": city, "units": "imperial"}
    data = requests.get(url, params=arguments).json()

    try:
        # see example json string at the end of this source code file
        name = data['name']
        desc = data['weather'][0]['description']
        temp = data['main']['temp']
        wind = data['wind']['speed']
        feels_like = data['main']['feels_like']
        full_string = 'Location: {} \n' \
                      'Conditions: {} \n' \
                      'Temperature (F): {} \n' \
                      'Wind (MPH): {} \n' \
                      'Feels Like (F): {}'.format(name, desc, temp, wind, feels_like)
        print(data)
    except:
        full_string = "No matching location found.\nPlease check locations and try again."

    return full_string

# **************** DO NOT CHANGE ANYTHING BELOW THIS LINE **********************
root = Tk()
root.geometry('815x600')
root.title('Weather App')

row_num = 0

for index, prompt in enumerate(prompts):
    label = Label(root, text=prompt)
    label.grid(row=row_num, column=0, sticky=W)
    row_num += 2
    fields[index] = Entry(root, textvariable=f"{index}", width=100)
    fields[index].grid(row=row_num, column=0, padx=4, sticky=W)
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

# example json string below
"""
{
    'coord': {'lon': -120.31, 'lat': 47.42}, 
    'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
    'base': 'stations', 
    'main': {
        'temp': 80.83, 
        'feels_like': 76.1, 
        'temp_min': 78.8, 
        'temp_max': 82.99, 
        'pressure': 1014, 
        'humidity': 27}, 
        'visibility': 10000, 
        'wind': {
            'speed': 5.82, 
            'deg': 220
        }, 
    'clouds': {
        'all': 1
    }, 
    'dt': 1598913535, 
    'sys': {
        'type': 1, 
        'id': 3917, 
        'country': 'US', 
        'sunrise': 1598879985, 
        'sunset': 1598928204
    }, 
    'timezone': -25200, 
    'id': 5815342, 
    'name': 'Wenatchee', 
    'cod': 200
    }
"""
