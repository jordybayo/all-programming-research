import tkinter as tk


LARGE_FONT=("verone", 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container=tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (StartPage, pageOne, pageTwo):
            frame=F(container, self)
            self.frames[F]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()





class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label= tk.Label(self, text="Page one!", font=LARGE_FONT)
        label.pack(pady=10, padx=10) 

        button1 = tk.Button(self, text="Visit PAge1", command=lambda:controller.show_frame(pageOne))
        button1.pack()

        button2 = tk.Button(self, text="visit page two", command=lambda:controller.show_frame(pageTwo))
        button2.pack()

class pageOne(tk.Frame):
    def __init__(self, parent, controller) :     
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Back to home", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Visit PAge1", command=lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page two", command=lambda:controller.show_frame(pageTwo))
        button2.pack()


class pageTwo(tk.Frame):
    def __init__(self, parent, controller) :     
        tk.Frame.__init__(self, parent)
        label= tk.Label(self, text="Back to home", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Visit PAge1", command=lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit PAge1", command=lambda:controller.show_frame(pageOne))
        button2.pack()


app=SeaofBTCapp()
app.mainloop()