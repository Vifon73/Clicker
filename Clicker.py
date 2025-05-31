import tkinter as tk
from tkinter import *
import math


root = Tk()
root.geometry("800x600")
root.title("Clicker")

rebirth_count = 0
rebirth_cost = 1000
rebirth_value = 1

click_count = 0
click_value = 1

upgrade1_cost = 10
upgrade2_cost = 100

upgrade1_bought = 0
upgrade2_bought = 0


def clicks():
    global click_count,click_value
    click_count += click_value
    label.config(text=f"Liczba klikniec: {click_count}")

def rebirth():
    global rebirth_count,click_count,rebirth_cost
    rebirth_count += rebirth_value
    label_rebirth.config(text=f"Liczba Odrodzeń:{rebirth_count}")


def buy_rebirth():
    global click_count,click_value,rebirth_count,rebirth_cost
    if click_count >= rebirth_cost:
        click_count -= rebirth_cost
        click_value += 3
        rebirth_count += 1
        rebirth_cost = math.ceil(rebirth_cost * 5)
        label.config(text=f"Liczba klikniec: {click_count}")
        upgrade_label.config(text=f"Wartosc Klikniecia: {click_value}")
        label_rebirth.config(text=f"Liczba Odrodzen:{rebirth_count}")
        rebirth_button.config(text=f"Ulepszenie: {rebirth_cost} clicks")
        info_label.config(text="")
    else:
        info_label.config(text="Za malo puntkow!")


def buy_upg1():
    global click_count, click_value,upgrade1_bought,upgrade1_cost
    if click_count >= upgrade1_cost:
        click_count -= upgrade1_cost
        click_value += 1
        upgrade1_bought +=1
        upgrade1_cost = math.ceil(upgrade1_cost * 1.5)


        label.config(text=f"Liczba klikniec: {click_count}")
        upgrade_label.config(text=f"Wartosc Klikniecia: {click_value}")
        upgrade_button1.config(text=f"Ulepszenie: {upgrade1_cost} clicks")
        info_label.config(text="")
    else:
        info_label.config(text="Za malo puntkow!")

#upg2 za 100 zwieksza o 2
def buy_upg2():
    global click_count, click_value,upgrade2_bought,upgrade2_cost
    if click_count >= upgrade2_cost:
        click_count -= upgrade2_cost
        click_value += 2
        upgrade2_bought += 1
        upgrade2_cost = math.ceil(upgrade2_cost * 1.5)


        label.config(text=f"Liczba klikniec: {click_count}")
        upgrade_label.config(text=f"Wartosc Klikniecia: {click_value}")
        upgrade_button2.config(text=f"Ulepszenie: {upgrade2_cost} clicks")
        info_label.config(text="")
    else:
        info_label.config(text="Za malo puntkow!")


#etykieta
label = tk.Label(root,text="Liczba klikniec: 0",font=("Arial",30))
label.pack(pady=20)

label_rebirth = tk.Label(root,text='liczba odrodzeń: 0',font=('Arial',25))
label_rebirth.pack(pady=20)

#przycisk
button = tk.Button(root,text="Click me!",font=("Arial",16),command=clicks)
button.pack(pady=10)

upgrade_button1 = tk.Button(root,text="Ulepszenie: (10 clicks)",font=("Arial",16),command=buy_upg1)
upgrade_button1.pack(pady=10)

upgrade_button2 = tk.Button(root,text="Ulepszenie: (100 clicks)",font=("Arial",16),command=buy_upg2)
upgrade_button2.pack(pady=10)

rebirth_button = tk.Button(root,text="Odrodzenie:(1000 clicks)",font=('Arial',20),command=buy_rebirth)
rebirth_button.pack(pady=20)

upgrade_label = tk.Label(root, text=f"Wartosc Klikniecia: {click_value}", font=("Arial", 12))
upgrade_label.pack(side='bottom')



info_label = tk.Label(root,text="", font=("Arial",12), fg="red")
info_label.pack(pady=5)


root.mainloop()