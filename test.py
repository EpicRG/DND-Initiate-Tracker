import customtkinter
import Backend

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.title("CustomTkinter Test")
root.geometry("600x300")



type_frame = customtkinter.CTkFrame(master=root, width=200, height=100)
type_frame.pack(pady=10, padx=10, fill="both", expand=True)

main_frame = customtkinter.CTkFrame(master=root)
main_frame.pack(pady=10, padx=10, fill="both", expand=True)


def buttons():
    add_character_button = customtkinter.CTkButton(master=type_frame, text="Add Character", width=50, height=30, command=lambda: print("Add Character button clicked"))
    add_character_button.pack(pady=10, padx=12, side="right")
    for i in range(3):
        player_names = ["L", "Mitgalad", "Eran"]
        player_checkbox = customtkinter.CTkCheckBox(master=type_frame, text=player_names[i])
        player_checkbox.pack(pady=10, padx=12, side="left")
        character_row = customtkinter.CTkFrame(master=type_frame, width=200, height=30)
        character_row.pack(anchor="w", pady=6, padx=10)

def test_main():
    buttons()
    root.mainloop()
test_main()
