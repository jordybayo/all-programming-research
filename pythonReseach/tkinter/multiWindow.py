from tkinter import *

class Welcome():
    def __init__(self, master):
        self.master=master
        self.master.geometry("400x200+100+200")
        self.master.title("Welcome")

        self.label1=Label(self.master, text="Welcome to the wages calculator GUI", fg='red').grid(row=0, column=2)
        self.button1=Button(self.master, text="OK", fg='blue', command=self.getWages).grid(row=6, column=2)
        self.button1=Button(self.master, text="QUIT", fg='blue', command=self.finish).grid(row=6, column=3)

    def getWages(self):
        root2=Toplevel(self.master)
        myGUI=Wages(root2)

    def finish(self):
        self.master.destroy()


class Wages():
    def __init__(self, master):
        self.nhours=DoubleVar()
        self.salaryh=DoubleVar()

        self.master=master
        self.master.geometry("500x200+100+200")
        self.master.title("Wages calculator")

        self.label1=Label(self.master, text="Welcome to the Wages calculator GUI", fg='red').grid(row=0, column=2)
        self.label2=Label(self.master, text="Enter your salary per hour").grid(row=3, column=0)
        self.button3=Label(self.master, text="Enter the number of hours worked").grid(row=4, column=0)

        self.mysalary=Entry(self.master, textvariable=self.salaryh).grid(row=3, column=2)
        self.myhours=Entry(self.master, textvariable=self.nhours).grid(row=4, column=2)
        self.button1=Button(self.master, text="Calculate salary", fg='blue', command=self.calculateSalary).grid(row=5, column=2)
        self.button2=Button(self.master, text="Back", fg='blue', command=self.myquit).grid(row=5, column=3)

    def calculateSalary(self):
        hours=self.nhours.get()
        print(hours)
        hsal=self.salaryh.get()
        salary=hours*hsal
        print(salary)
        self.labelresult=Label(self.master, text="your salary is %.2f XAF"% salary).grid(row=7, column=2)

    def myquit(self):
        self.master.destroy()
    

def mainEconomic():
    root=Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

if __name__ == "__main__":
    main()