import random
import tkinter as tk

def pas():
    #get your username and password
    username.get()
    password = int(key.get())
    #Loop continue if x is not None
    while not None:
        x = random.randint(0000, 9999)
        print(x)
        if x == password:
            print("Found your password:{}".format(password))
            break
    labelResult["text"] = "Complete"

win = tk.Tk()
win.geometry("350x220")
win.title("Login")

labelFirst = tk.Label(win, text="username:")
labelFirst.grid(row=1, column=1, padx=10)
labelFirst.pack()

username = tk.Entry(win, width=30)
username.grid(row=1, column=2)
username.pack()

labelSecond = tk.Label(win, text="password(4):")
labelSecond.grid(row=2, column=1, padx=10)
labelSecond.pack()

key = tk.Entry(win, show="*", width=30)
key.grid(row=2, column=2)
key.pack()

kmButton = tk.Button(win, text="Enter")
kmButton["command"] = pas
kmButton.pack()

labelResult = tk.Label(win, text="---")
labelResult.pack()

win.mainloop()




