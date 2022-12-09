"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Label

LAYOUT = (
    (("#0095E5", "arrow"), ("#F529A4", "hand2"), ("#9532B2", "heart")),
    (("#775AA1", "fleur"), ("#F4CF00", "watch"), ("#F5375C", "pirate")),
)


def setup_ui(master):
    for i, row in enumerate(LAYOUT):
        for j, (color, cursor) in enumerate(row):
            Label(
                master, bg=color, width=15, height=8, cursor=cursor
            ).grid(row=i, column=j, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    root.config(bd=20)
    setup_ui(root)
    root.mainloop()
