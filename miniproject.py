from tkinter import *
import requests

def get_data():
    city = my_city.get()  # Retrieve the actual string value
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=001ca7304344291959d1872e9d1a472f").json()
    
    if data.get("weather"):  # Check if the data contains weather information
        w_label1.config(text=data["weather"][0]["main"])
        wd_label1.config(text=data["weather"][0]["description"])
        temp_label1.config(text=str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
        pr_label1.config(text=data["main"]["pressure"])
    else:
        w_label1.config(text="N/A")
        wd_label1.config(text="N/A")
        temp_label1.config(text="N/A")
        pr_label1.config(text="N/A")

win = Tk()
win.title("Weather Infographics")
win.config(bg="#ADD8E6")
win.geometry("600x600")

# Label of app
my_label = Label(win, text="Weather Information App", font=("Time New Roman", 30, "italic", "bold"))
my_label.place(x=25, y=20, height=50, width=550)

# Entry widget for user to input city
my_city = StringVar()
city_entry = Entry(win, textvariable=my_city, font=("Helvetica", 15, "italic", "bold"))
city_entry.place(x=25, y=90, width=550, height=50)

# Labels to display weather information
w_label = Label(win, text="Weather Climate", font=("Helvetica", 15, "italic", "bold"))
w_label.place(x=25, y=230)
w_label1 = Label(win, text="", font=("Helvetica", 15, "italic", "bold"))
w_label1.place(x=290, y=230)

wd_label = Label(win, text="Weather Description", font=("Helvetica", 15, "italic", "bold"))
wd_label.place(x=25, y=270)
wd_label1 = Label(win, text="", font=("Helvetica", 15, "italic", "bold"))
wd_label1.place(x=290, y=270)

temp_label = Label(win, text="Temperature", font=("Helvetica", 15, "italic", "bold"))
temp_label.place(x=25, y=310)
temp_label1 = Label(win, text="", font=("Helvetica", 15, "italic", "bold"))
temp_label1.place(x=290, y=310)

pr_label = Label(win, text="Pressure", font=("Helvetica", 15, "italic", "bold"))
pr_label.place(x=25, y=350)
pr_label1 = Label(win, text="", font=("Helvetica", 15, "italic", "bold"))
pr_label1.place(x=290, y=350)

# Button to get weather information
button = Button(win, text="Done", font=("Helvetica", 20, "italic", "bold"), command=get_data)
button.place(x=270, y=150, width=100, height=50)

win.mainloop()
