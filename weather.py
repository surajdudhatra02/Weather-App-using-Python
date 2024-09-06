from tkinter import * 
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=24af503d91adc41c53530b8dfcf8da3d").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data['main']["pressure"])

win = Tk()

win.title("My Weather App 🌥️")
win.config(bg="#413e45")
win.geometry("500x500")

name_label = Label(win, text="My Weather App 🌥️", font=("Time New Roman", 30, "bold"))

name_label.place(x=25, y=50, height=50, width=450)

city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, text="My Weather App", values=list_name ,font=("Time New Roman", 20, "bold"), textvariable=city_name)

com.place(x=25, y=130, height=50, width=450)

done_button = Button(win, text="🔍", font=("Time New Roman", 20, "bold"), command=data_get)

done_button.place(x=200,  y=200, height=35, width=80)



w_label = Label(win, text="Weather Climate 🌥️", font=("Time New Roman", 16))

w_label.place(x=25, y=250, height=40, width=220)

w_label1 = Label(win, text="", font=("Time New Roman", 20))

w_label1.place(x=250, y=250, height=40, width=220)




wb_label = Label(win, text="Weather Description", font=("Time New Roman", 17))

wb_label.place(x=25, y=300, height=40, width=220)

wb_label1 = Label(win, text="", font=("Time New Roman", 17))

wb_label1.place(x=250, y=300, height=40, width=220)



temp_label = Label(win, text="Temperature 🌡️", font=("Time New Roman", 19))

temp_label.place(x=25, y=350, height=40, width=220)

temp_label1 = Label(win, text="", font=("Time New Roman", 20))

temp_label1.place(x=250, y=350, height=40, width=220)



pre_label = Label(win, text="Pressure ⏱️", font=("Time New Roman", 20))

pre_label.place(x=25, y=400, height=40, width=220)

pre_label1 = Label(win, text="", font=("Time New Roman", 20))

pre_label1.place(x=250, y=400, height=40, width=220)

win.mainloop()