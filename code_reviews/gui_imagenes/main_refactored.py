from tkinter import Checkbutton, Frame, IntVar, Label, PhotoImage, Tk

ITEMS = ("pizza", "tomahawk", "jamon")


class Card(Frame):

    def __init__(self, filename, orientation):
        super().__init__()
        self.value = IntVar() 
        self.photo = PhotoImage(file=f"images/{filename}.gif")
        Label(self, image=self.photo).pack()
        Checkbutton(
            self, text=filename.capitalize(), variable=self.value
        ).pack(side=orientation)


class App(Tk):

    def __init__(self):
        super().__init__()
        self.cards = []
        self.setup_ui()

    def setup_ui(self):
        for item in ITEMS:
            card = Card(item, "right")
            card.pack(side="left")
            self.cards.append(card)


if __name__ == "__main__":
    app = App()
    app.mainloop()
