import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# class TemperatureConverter:

#     @staticmethod
#     def fahrenheit_to_celsius(f,format = True):
#         result = (f-32) * 5/9

#         if format:
#             return f"{f} Fahrenheit = {result: .2f} celsius"
        
#         return result
#     @staticmethod

#     def celsius_to_fahrenheit(c,format=True):
#         result = c * 9/5 +32
#         if format:
#             return f"{c} celsius = {result: .2f} Fahrenheit"
#         return result

# class ConverterFrame(ttk.Frame):
#     def __init__(self,container, unit_from,converter):
#         super().__init__(container)
#         self.unit_from = unit_from
#         self.converter = converter

#         options = {"padx":5,"pady":0}
#         self.temperature_label = ttk.Label(self, text=self.unit_from)
#         self.temperature_label.grid(column=0,row=0,sticky=tk.W,**options)

#         self.temperature = tk.StringVar()
#         self.temperature_entry = ttk.Entry(self,textvariable= self.temperature)
#         self.temperature_entry.grid(column=1,row=0,**options)
#         self.temperature_entry.focus()

#         self.convert_button = ttk.Button(self,text="Convert")
#         self.convert_button["command"] = self.convert
#         self.convert_button.grid(column=2,row=0,sticky=tk.W,**options)
#         self.convert_button.configure(command=self.convert)

#         self.result_label = ttk.Label(self)
#         self.result_label.grid(row=1,columnspan=3,**options)
#         self.grid(column=0,row=0,padx=10,pady=10,sticky=tk.NSEW)

#     def convert(self):

#         try:
#             input_value = float(self.temperature.get())
#             result = self.convert(input_value)
#             self.result_label.config(text=result)

#         except ValueError as error:
#             showerror(title="ERROR",message=error)

#     def reset(self):
#         self.temperature_entry.delete(0,"end")
#         self.result_label.text = ''


# class ControlFrame(tk.Frame):
#     def __init__(self,container):
#         super().__init__(container)
#         self["text"] = "options"
#         self.selected_value = tk.IntVar()
#         ttk.Radiobutton(self,text="F to C",value=0,variable=self.selected_value,command=self.change_frame
#                         ).grid(column=0,row=0,padx=5,pady=5)
        
#         ttk.Radiobutton(self,text="C to F", value=1,variable=self.selected_value,command=self.change_frame
#                         ).grid(column=1,row=0,padx=5,pady=5)
        
#         self.grid(column=0,row=1,padx=5,pady=5,sticky="ew")
#         self.frames = {}
#         self.frames[0] = ConverterFrame(container,"Fahrenheit",TemperatureConverter.fahrenheit_to_celsius)
#         self.frames[1] = ConverterFrame(container,"celsius",TemperatureConverter.celsius_to_fahrenheit)
#         self.change_frame() 



#     def change_frame(self):
#         frame = self.frames[self.selected_value.get()]
#         frame.tkraise()
#         frame.reset()

# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title("conversor de tempertura")
#         self.geometry("300x120")
#         self.resizable(False,False)
        


# if __name__ == "__main__":
#     app = App()
#     ControlFrame(app)
#     app.mainloop()

# class MainFrame(ttk.Frame):
#     def __init__(self,container):
#         super().__init__(container)

#         options = {"padx":5,"pady":5}
#         self.label = ttk.Label(self,text="Hello tkinter")
#         self.label.pack(**options)

#         self.button = ttk.Button(self,text = "Click me")
#         self.button["command"] = self.button_clicked
#         self.button.pack(**options)

#         self.pack(**options)

#     def button_clicked(self):
#         showinfo(title="information",message="hello tkinter")


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()


#         self.title("my awesome app")
#         self.geometry("300x100")


# app = App()
# frame = MainFrame(app)
# app.mainloop()


# class InputFrame(ttk.Frame):
#     def __init__(self,container):
#         super().__init__(container)

#         self.columnconfigure(0,weight=1)
#         self.columnconfigure(0,weight=3)

#         self.__create_widgets()

#     def __create_widgets(self):

#         ttk.Label(self, text="Find what: ").grid(column=0,row=0,sticky=tk.W)
#         keyword = ttk.Entry(self,width=30)
#         keyword.focus()
#         keyword.grid(column=1,row=0,sticky=tk.W)

#         ttk.Label(self,text="Replace with: ").grid(column=0,row=1,sticky=tk.W)
#         replacement = ttk.Entry(self,width=30)
#         replacement.grid(column=1,row=1,sticky=tk.W)

#         match_case = tk.StringVar()
#         match_case_check = ttk.Checkbutton(self,
#                                            text="Match case",
#                                            variable=match_case,
#                                            command=lambda:print(match_case.get()))
#         match_case_check.grid(column=0,row=2,sticky=tk.W)



#         wrap_around = tk.StringVar()
#         wrap_around_check= ttk.Checkbutton(self,
#                                            text="Wrap around",
#                                            variable=wrap_around,
#                                            command=lambda:print(wrap_around.get()))
#         wrap_around_check.grid(column=0,row=3,sticky=tk.W)

#         for widget in self.winfo_children():
#             widget.grid(padx=0,pady=5)

# class ButtonFrame(ttk.Frame):
#     def __init__(self,container):
#         super().__init__(container)

#         self.columnconfigure(0,weight=1)
#         self.__create_widgets()

#     def __create_widgets(self):

#         ttk.Button(self,text="Find Next").grid(column=0,row=0)
#         ttk.Button(self,text="Replace").grid(column=0,row=1)
#         ttk.Button(self,text="Replace All").grid(column=0,row=2)
#         ttk.Button(self,text="Cancel").grid(column=0,row=3)

#         for widget in self.winfo_children():
#             widget.grid(padx=0,pady=5)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("replace")
#         self.geometry("400x150")
#         self.resizable(0,0)

#         self.attributes("-toolwindow", True)

#         self.columnconfigure(0,weight=4)
#         self.columnconfigure(1,weight=1)
#         self.__create_widgets()

#     def __create_widgets(self):
#         input_frame = InputFrame(self)
#         input_frame.grid(column=0,row=0)

#         button_frame = ButtonFrame(self)
#         button_frame.grid(column=1,row=0)



# app = App()
# app.mainloop()


class Startpage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self, text = "Startpage")

        label.grid(row=0,column=4,padx=10,pady=10)


        button1 = ttk.Button(self,text="page1",
        command=lambda:controller.show_frame(Page1))

        button1.grid(row=1,column=1,padx=10,pady=10)

        button2 = ttk.Button(self,text="page2",
            command= lambda:controller.show_frame(Page2))
        
        button2.grid(row=2,column=1,padx=10,pady=10)

class Page1(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        label = ttk.Label(self,text="page1")
        label.grid(row=0,column=4,padx=10,pady=10)

        button1 = ttk.Button(self,text="StartPage",
                             command= lambda: controller.show_frame(Startpage))
        
        button1.grid(row=1,column=1,padx=10,pady=10)

        button2 = ttk.Button(self,text = "page2",
                             command= lambda:controller.show_frame(Page2))
        

        button2.grid(row=2,column=1,padx=10,pady=10)


class Page2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self,text="page2")
        label.grid(row=0,column=4,padx=10,pady=10)


        button1 = ttk.Button(self,text="page1",
                             command=lambda:controller.show_frame(Page1))
        
        button1.grid(row=1,column=1,padx=10,pady=10)

        button2 = ttk.Button(self,text = "start page",
                             command=lambda:controller.show_frame(Startpage))
        
        button2.grid(row=2,column=1,padx=10,pady=10)


class TkinterApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container = tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (Startpage,Page1,Page2):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="nsew")

        self.show_frame(Startpage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()




app = TkinterApp()
app.mainloop()


class FirstWindow(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,text="this is window 1").pack(padx=10,pady=10)
        self.pack(padx=10,pady=10)


class SecondWindow(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        tk.Label(self,text="This is window 2").pack(padx=10,pady=10)
        self.pack(padx=10,pady=10)
class MainWindow:
    def __init__(self,master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10,pady=10,fill="both",expand=1)
        self.windownum = 0
        self.framelist = []
        self.framelist.append(FirstWindow(mainframe))
        self.framelist.append(SecondWindow(mainframe))
        self.framelist[1].forget()
        bottomframe = tk.Frame(master)
        bottomframe.pack(padx=10, pady=10)

        switch = tk.Button(bottomframe, text = "Switch", command=self.switchwindows)
        switch.pack(padx=10, pady=10)

    def switchwindows(self):
        self.framelist[self.windownum].forget()
        self.windownum = (self.windownum + 1) % len(self.framelist)
        self.framelist[self.windownum].tkraise()
        self.framelist[self.windownum].pack(padx=10,pady=10)


                


root = tk.Tk()
window = MainWindow(root)
root.mainloop()

