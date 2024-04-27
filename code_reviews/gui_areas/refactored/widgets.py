"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Entry, Label, Frame, StringVar, OptionMenu


class CustomMenu(Frame):

    def __init__(self, text, options, command=None, master=None):
        super().__init__(master=master)
        self.text = text
        self.value = StringVar()
        self.value.set(text)
        self.options = OptionMenu(self, self.value, *options, command=command)
        self.options.configure(width=20)
        self.options.pack(padx=5, pady=5)

    def get(self, default=None):
        if self.value.get() == self.text:
            return default
        return self.value.get()


class CustomEntry(Frame):

    def __init__(self, text, master=None):
        super().__init__(master=master)
        Label(self, text=text, width=10).pack(side="left", padx=5, pady=5)
        self.entry = Entry(self)
        self.entry.pack(side="left")

    def get(self):
        if not self.entry.get():
            return 0
        return float(self.entry.get())


class CustomFrame(Frame):

    def __init__(self, entries):
        super().__init__()
        self.entries = entries
        self.widgets = []
        self.setup_ui()

    def setup_ui(self):
        for entry in self.entries:
            widget = CustomEntry(entry, master=self)
            widget.pack()
            self.widgets.append(widget)
        self.result = Label(master=self)
        self.result.pack(padx=5, pady=5)

    def get_entries(self):
        return [widget.get() for widget in self.widgets]

    def set_result(self, result):
        self.result.config(text=result)
