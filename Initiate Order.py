def main():
    midgalad_roll = int(input("What did Midgalad roll?: "))
    erran_roll = int(input("What did Erran roll?: "))
    odin_roll = int(input("What did Odin roll?: "))

    Initiate_Order = [
        ("Midgalad", midgalad_roll),
        ("Erran", erran_roll),
        ("Odin", odin_roll)
    ]

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



    Initiate_Order = sorted(Initiate_Order, key=lambda x: x[1], reverse=True)

    print(f"Initiate Order: {Initiate_Order}")

main()