import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime 
from timestamp import Timestamp
# from tkcalendar import DateEntry


    
def open_secondary_window():
    # Create secondary (or popup) window.
    def save_command():
        begin_text = begin_entry.get()
        begin_time = datetime.datetime.strptime(begin_text,"%Y-%m-%d %H:%M:%S")
        print("begin time", begin_time)
        messagebox.showinfo("begin Time", str(begin_time))
        end_text = end_entry.get()
        end_time = datetime.datetime.strptime(end_text, "%Y-%m-%d %H:%M:%S")
        print("end time", end_time)
        messagebox.showinfo("end time", str(end_time))
        total_seconds = Timestamp(begin_time,end_time)
        print(total_seconds)
        messagebox.showinfo("total seconds", total_seconds)

    

    secondary_window = tk.Toplevel()
    secondary_window.geometry("240x100")
    secondary_window.title('New Timestamp')
    secondary_window.resizable(0, 0)

    # configure the grid
    secondary_window.columnconfigure(0, weight=1)
    secondary_window.columnconfigure(1, weight=3)

    # begin
    begin_label = ttk.Label(secondary_window, text="begin:")
    begin_label.grid(column=0, row=0, sticky=tk.E, padx=5, pady=5)

    begin_entry = ttk.Entry(secondary_window)
    begin_entry.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    # end
    end_label = ttk.Label(secondary_window, text="end:")
    end_label.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)

    end_entry = ttk.Entry(secondary_window)
    end_entry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

    # save button
    save_button = ttk.Button(secondary_window, text="save",command=save_command)
    save_button.grid(column=0, row=3, sticky=tk.SW, padx=5, pady=5)

    # cancel button
    cancel_button = ttk.Button(secondary_window, text="cancel",command=secondary_window.destroy)
    cancel_button.grid(column=1, row=3, sticky=tk.SE, padx=5, pady=5)


# Create the main window.
main_window = tk.Tk()
main_window.title('Task Demo - App')
window_width = 640
window_height = 480

# get the screen dimension
screen_width = main_window.winfo_screenwidth()
print(screen_width)
screen_height = main_window.winfo_screenheight()
print(screen_height)

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# Create a button inside the main window that
# invokes the open_secondary_window() function
# when pressed.
label_info = ttk.Label(
    main_window,
    text='Place other control'
)
label_info.grid(column=0,row=0)

button_open = ttk.Button(
    main_window,
    text="New Timestamp",
    command=open_secondary_window
)
button_open.grid(column=2,row=3)

    

main_window.mainloop()


