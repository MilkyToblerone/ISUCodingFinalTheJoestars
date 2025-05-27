import json
import os
from characters import Stand

CUSTOM_STAND_FILE = "data/custom_stands.json"

def create_custom_stand():
    print("\n=== CREATE CUSTOM STAND ===")
    name = input("Stand Name: ")
    ability = input("Stand Ability: ")
    weakness = input("Stand Weakness: ")

    new_stand = {
        "name": name,
        "ability": ability,
        "weakness": weakness
    }

    stands = []
    if os.path.exists(CUSTOM_STAND_FILE):
        with open(CUSTOM_STAND_FILE, "r", encoding="utf-8") as f:
            stands = json.load(f)

    stands.append(new_stand)

    with open(CUSTOM_STAND_FILE, "w", encoding="utf-8") as f:
        json.dump(stands, f, indent=4)

    print(f"\nCustom stand '{name}' has been saved!")

def view_custom_stands():
    print("\n=== CUSTOM STANDS ===")
    if not os.path.exists(CUSTOM_STAND_FILE):
        print("No custom stands found.")
        return

    with open(CUSTOM_STAND_FILE, "r", encoding="utf-8") as f:
        stands = json.load(f)

    for i, s in enumerate(stands, start=1):
        print(f"\n#{i} - {s['name']}\n Ability: {s['ability']}\n Weakness: {s['weakness']}")

def get_all_stands():
    default_stands = [
        Stand("Silver Chariot", "High-speed fencing", "Short range"),
        Stand("The World", "Time stop", "Overconfidence"),
        Stand("Echoes", "Sound manipulation", "Fragile body"),
        Stand("Crazy Diamond", "Restoration", "Can't heal self"),
        Stand("Aerosmith", "Miniature fighter plane", "Limited fuel")
    ]

    custom_stands = []
    if os.path.exists(CUSTOM_STAND_FILE):
        with open(CUSTOM_STAND_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            for s in loaded:
                custom_stands.append(Stand(s["name"], s["ability"], s["weakness"]))

    return default_stands + custom_stands

def only_custom_stands():
    custom_stands = []
    if os.path.exists(CUSTOM_STAND_FILE):
        with open(CUSTOM_STAND_FILE, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            for s in loaded:
                custom_stands.append(Stand(s["name"], s["ability"], s["weakness"]))

    return custom_stands
