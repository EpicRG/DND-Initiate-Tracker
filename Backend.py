
def sort_initiative_order(characters):
    # Each character is stored as (name, roll); the second value is the roll.
    return sorted(characters, key=lambda character: character[1], reverse=True)


def parse_roll(character_name, roll_text):
    # Entry widgets return text, so convert the roll before doing numeric work.
    try:
        return int(roll_text)
    except ValueError as error:
        raise ValueError(f"Enter a valid roll for {character_name}.") from error


def build_initiative_order(selected_characters, custom_characters):
    # Copy the selected list so extending it does not change the original list.
    characters = list(selected_characters)
    characters.extend(custom_characters)
    return sort_initiative_order(characters)


def split_dead_characters(initiative_order, dead_characters):
    # A set makes checking whether a character is dead fast and straightforward.
    active = [character for character in initiative_order if character not in dead_characters]
    dead = [character for character in initiative_order if character in dead_characters]
    return active, dead


def leaderboard_entries(initiative_order, rows_per_column=4):
    # Return grid coordinates so the UI can place four entries in each column.
    return [
        (index % rows_per_column, index // rows_per_column, f"{index + 1}. {name} ({roll})")
        for index, (name, roll) in enumerate(initiative_order)
    ]