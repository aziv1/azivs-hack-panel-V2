from tkinter import *
import tkinter as tk
from tkinter.ttk import *

from click import echo_via_pager
import dos_panel

class master(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        def quit_program():
            quit()

        def open_window_dosing(self):
            window = dos_panel.dossing_panel(self)
            window.grab_set()

        # place a button on the root window
        tk.Label(self, text="HACK PANEL V2.0.0").pack(expand=True)
        tk.ttk.Button(self, text="Open Dossing Window", command=self.open_window_dosing).pack(expand=True)
        tk.ttk.Button(self, text="Quit", command=quit_program).pack(expand=True)

if __name__ == "__main__":
    app = master()
    app.mainloop()