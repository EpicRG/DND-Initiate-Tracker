import customtkinter
import Initiate_order

customtkinter.set_appearance_mode("system") #choses systeme theme (light/dark)
customtkinter.set_default_color_theme("green") #sets theme of buttons osv

root = customtkinter.CTk()
root.geometry("900x700") #create window

def start_initiative_tracker():

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    lable = customtkinter.CTkLabel(master=frame, text="Initiative Tracker", font=("Roboto Medium", 25))
    lable.pack(pady=12, padx=10)

    name_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Character Name")
    name_entry.pack(pady=12, padx=10)

    roll_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Initiative Roll")
    roll_entry.pack(pady=12, padx=10)

    enter_button = customtkinter.CTkButton(master=frame, text="Enter", command=lambda: )
    sort_button.pack(pady=12, padx=10)

start_initiative_tracker()
root.mainloop()