import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename

#BASICOS
# win = tk.Tk()
# label = tk.Label(text="name")
# label.pack()
# entry = tk.Entry(fg="yellow",bg="black",width=50)
# entry.pack()
# button = tk.Button(text="Info")
# button.pack()
# win.mainloop()

#Text
# win = tk.Tk()
# text_box = tk.Text()
# text_box.pack()
# text_box.get("1.0","1.5")
# print(text_box)


# win.mainloop()
#Frame
# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()
# label_a = tk.Label(master=frame_a,text="im in frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_a,text="im in frame B")
# label_b.pack()

# frame_a.pack()
# frame_b.pack()
#window.mainloop()
# window = tk.Tk()
# border_effects = {
#     "flat": tk.FLAT,
#     "sunken": tk.SUNKEN,
#     "raised": tk.RAISED,
#     "groove": tk.GROOVE,
#     "ridge": tk.RIDGE,
# }

# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master=window,relief=relief,borderwidth=5)
#     frame.pack(side=tk.LEFT)
#     label = tk.Label(master=frame,text=relief_name)
#     label.pack()

# window.mainloop()

#exercicio do tktinter

# win = tk.Tk()
# entry = tk.Entry(bg="white",fg="Black",width=40)
# entry.pack()
# entry.insert(0,"What is your name")

# win.mainloop()

# def fahrenheit_to_celsius():
#     fahrenheit = ent_temperature.get()
#     celsius = (5/9) * (float(fahrenheit)-32)
#     lbl_result["text"] = f"{round(celsius,2)}"


# window = tk.Tk()
# window.title("Temperature Converter")
# window.resizable(width=False,height=False)

# frm_entry = tk.Frame(master=window)
# ent_temperature = tk.Entry(master=frm_entry,width=10)
# lbl_temp = tk.Label(master=frm_entry,text="DEGREE FARHENHEIT")

# ent_temperature.grid(row=0, column=0,sticky="e")
# lbl_temp.grid(row=0,column=1,sticky="w")

# btn_convert = tk.Button(
#     master=window,
#     text="RIGHTWARDS BLACK ARROW",
#     command= fahrenheit_to_celsius
# )
# lbl_result = tk.Label(master=window,text= "\N{DEGREE CELSIUS}")

# frm_entry.grid(row=0,column=0,padx=10)
# btn_convert.grid(row=0,column=1,pady=10)
# lbl_result.grid(row=0,column=2,padx=10)


# window.mainloop()


def open_file():
    filepath = askopenfilename(
        filetypes=[("text files","*.txt"),("All Files","*.*")]

    )
    if not filepath:
        return
    txt_edit.delete("1.0",tk.END)
    with open(filepath,mode="r",encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END,text)
    window.title(f"simple text editor -{filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes = [("Text Files","*.txt"),("All files","*.*")],

    )

    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0",tk.END)
        output_file.write(text)
    window.title(f"Simple text editor-{filepath}")


window = tk.Tk()
window.title("simple text editor")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window,relief=tk.RAISED,bd=2)
btn_open = tk.Button(frm_buttons, text="open",command=open_file)
btn_save = tk.Button(frm_buttons,text="Save as...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()