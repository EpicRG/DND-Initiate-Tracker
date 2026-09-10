import os

def sort_initiative_order(characters):
    return sorted(characters, key=lambda x: x[1], reverse=True)

def main():

    Initiate_Order = []

    include_midgalad = input("Is Midgalad in the Fight? (y/n): ")
    if include_midgalad.lower() == 'y' or include_midgalad.lower() == 'yes':
        midgalad_roll = int(input("What did Midgalad roll?: "))
        Initiate_Order = [("Midgalad", midgalad_roll)]


    include_erran = input("Is Erran in the Fight? (y/n): ")
    if include_erran.lower() == "y" or include_erran.lower() == "yes":
        erran_roll = int(input("What did Erran roll?: "))
        Initiate_Order.append(("Erran", erran_roll))


    include_odin = input("Is L in the Fight? (y/n): ")
    if include_odin.lower() == 'y' or include_odin.lower() == 'yes':
        odin_roll = int(input("What did L roll?: "))
        Initiate_Order.append(("L", odin_roll))


    enemies = int(input("How many NPCs?: "))

    for i in range (enemies):
        enemy_name = input("Enter NPC name: ")
        if enemy_name.lower() == 'done':
            break

        try:
            roll = int(input(f"Enter roll for {enemy_name}: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        Initiate_Order.append((enemy_name, roll))

    Initiate_Order = sort_initiative_order(Initiate_Order)

    print("\n--- INITIATIVE ORDER ---")
    for position, (name, roll) in enumerate(Initiate_Order, start=1):
        print(f"{position}. {name} (Roll: {roll})")
    print("------------------------\n")

while True:
    main()
    
    user_choice = input("Press ENTER to start a new encounter, or type 'exit' to close: ")
    if user_choice.strip().lower() in ['exit', 'quit', 'e']:
        print("Exiting combat tracker...")
        break
        
    # Optional: Clears the terminal screen for the next round so it stays neat
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Starting new encounter...\n")