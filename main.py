from tkinter import *
from canvas import CustomCanvas
from constants import *

class Window(Tk):
    def __init__(self):
        super().__init__()

        canvas = CustomCanvas(self)
        canvas.place(x=0, y=0, relheight=1, relwidth=0.8)

        self.config_frame = Frame(self, bg="#222222")
        self.config_frame.place(relx=0.8, y=0, relwidth=0.2, relheight=1)
        
        # region Config Frame Elements

        self.mass_var = IntVar()
        self.rad_var = IntVar()
        self.g_var = IntVar()

        self.mass_lbl = Label(self.config_frame, text="Mass:", font=("Helvetica", 20, "bold"))
        self.mass_lbl.pack(pady=10)

        self.mass_entry = Entry(self.config_frame, highlightthickness=0, textvariable=self.mass_var)
        self.mass_entry.pack(padx=5)

        self.radius_lbl = Label(self.config_frame, text="Radius:", font=("Helvetica", 20, "bold"))
        self.radius_lbl.pack(pady=10)

        self.radius_entry = Entry(self.config_frame, highlightthickness=0, textvariable=self.rad_var)
        self.radius_entry.pack(padx=5)

        self.g_lbl = Label(self.config_frame, text="Gravity:", font=("Helvetica", 20, "bold"))
        self.g_lbl.pack(pady=10)

        self.g_entry = Entry(self.config_frame, highlightthickness=0, textvariable=self.g_var)
        self.g_entry.pack(padx=5)


tk = Window()
tk.geometry("1000x700")
tk.resizable(False, False)

# endregion

tk.mainloop()