from tkinter import *
import requests
from bs4 import BeautifulSoup
from tkinter.font import Font
from tkinter import ttk
import time
import threading

root = Tk()
root.title("COVID-19")
root.geometry("300x360")
root.resizable(0, 0)
root.iconbitmap("icon.ico")

label_frame_1 = LabelFrame(root, text="Details")
label_frame_1.pack(expand="yes", fill="both", padx=5)


def my_threading():
    progress["value"] = 0
    total_cases.set("")
    new_cases.set("")
    total_deaths.set("")
    new_deaths.set("")
    total_recovered.set("")
    active_cases.set("")
    t = threading.Thread(target=main_procedure)
    t.start()


def main_procedure():
    options_menu.config(state="disabled")
    progress["value"] += 20
    label_frame_1.update_idletasks()

    find_button.config(state="disabled")
    html = requests.get("https://www.worldometers.info/coronavirus/").text

    progress["value"] += 20
    label_frame_1.update_idletasks()

    html_soup = BeautifulSoup(html, "html.parser")
    rows = html_soup.find_all("tr")

    progress["value"] += 20
    label_frame_1.update_idletasks()

    def extract_text(row, tag):
        element = BeautifulSoup(row, 'html.parser').find_all(tag)
        text = [col.get_text() for col in element]
        return text

    progress["value"] += 20
    label_frame_1.update_idletasks()

    data = []

    for row in rows:
        data.append(extract_text(str(row), 'td')[1:9])

    progress["value"] += 10
    label_frame_1.update_idletasks()

    for sublists in data:
        try:
            if sublists[0] == str(selected_country.get()):
                progress["value"] += 10
                label_frame_1.update_idletasks()
                total_cases.set(sublists[1])
                new_cases.set(str(sublists[2]).replace("+", ""))
                total_deaths.set(sublists[3])
                new_deaths.set(str(sublists[4]).replace("+", ""))
                total_recovered.set(sublists[5])
                active_cases.set(sublists[7])
                find_button.config(state="normal")
                options_menu.config(state="normal")
                exit_button.config(state="normal")
                break
        except:
            pass


total_cases = StringVar()
new_cases = StringVar()
total_deaths = StringVar()
new_deaths = StringVar()
total_recovered = StringVar()
active_cases = StringVar()


label_font = Font(size=11, family="Myraid Pro", weight="bold")

options = ["World", "USA", "UK", "Oman", "Australia", "Sri Lanka"]

selected_country = StringVar()
selected_country.set("World")

options_menu = OptionMenu(root, selected_country, *options)
options_menu.pack()


find_button = Button(root, text="Find", bg="#f53d3d", fg="white", font=label_font, width=40, height=2, command=my_threading)
find_button.pack()

exit_button = Button(root, text="Exit", bg="#7703fc", fg="white", font=label_font, width=40, height=2, command=root.destroy)
exit_button.pack()
exit_button.config(state="disabled")

title_label = Label(root, text="CREATED BY: YATHURSHAN", font="Roboto 10 bold")
title_label.pack()

######################################

total_cases_label = Label(label_frame_1, text="Total Cases", fg="red", font=label_font)
total_cases_label.place(x=32, y=5)

total_cases_box = Entry(label_frame_1, textvariable=total_cases, justify="center", bd=5)
total_cases_box.place(x=10, y=25)
total_cases_box.config(state="disabled")

new_cases_label = Label(label_frame_1, text="New Cases", fg="red", font=label_font)
new_cases_label.place(x=32, y=55)

new_cases_box = Entry(label_frame_1, textvariable=new_cases, justify="center", bd=5)
new_cases_box.place(x=10, y=75)
new_cases_box.config(state="disabled")

active_cases_label = Label(label_frame_1, text="Active Cases", fg="red", font=label_font)
active_cases_label.place(x=32, y=105)

active_cases_box = Entry(label_frame_1, textvariable=active_cases, justify="center", bd=5)
active_cases_box.place(x=10, y=125)
active_cases_box.config(state="disabled")

##############################################

total_deaths_label = Label(label_frame_1, text="Total Deaths", fg="red", font=label_font)
total_deaths_label.place(x=172, y=5)

total_deaths_box = Entry(label_frame_1, textvariable=total_deaths, justify="center", bd=5)
total_deaths_box.place(x=150, y=25)
total_deaths_box.config(state="disabled")

new_deaths_label = Label(label_frame_1, text="New Deaths", fg="red", font=label_font)
new_deaths_label.place(x=172, y=55)

new_deaths_box = Entry(label_frame_1, textvariable=new_deaths, justify="center", bd=5)
new_deaths_box.place(x=150, y=75)
new_deaths_box.config(state="disabled")

total_recovered_label = Label(label_frame_1, text="Total Recovered", fg="red", font=label_font)
total_recovered_label.place(x=155, y=105)

total_recovered_box = Entry(label_frame_1, textvariable=total_recovered, justify="center", bd=5)
total_recovered_box.place(x=150, y=125)
total_recovered_box.config(state="disabled")

progress = ttk.Progressbar(label_frame_1, orient=HORIZONTAL, length=200, mode="determinate")
progress.place(x=50, y=160)

root.mainloop()
