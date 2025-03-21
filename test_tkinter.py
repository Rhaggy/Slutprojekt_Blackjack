import tkinter as tk

root = tk.Tk()
root.title("Blackjack")

def ja():
    print("f u")



lbl = tk.Label(root, text="1")
lbl.grid(row= 1, column= 1)

btn = tk.Button(root, text="HIT", command=ja)
btn.grid(row= 0, column= 0)

root.mainloop()