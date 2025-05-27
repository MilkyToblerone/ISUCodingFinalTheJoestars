
import json
import os
from datetime import datetime

def get_save_path(name):
    folder = "data/saves"
    os.makedirs(folder, exist_ok=True)
    filename = f"{name.lower().replace(' ', '_')}_save.json"
    return os.path.join(folder, filename)

def save_game(player, battle_number):
    save_data = {
        "name": player.name,
        "hp": player.hp,
        "stand": player.stand.name if player.stand else None,
        "stand_ability": player.stand.ability if player.stand else None,
        "stand_weakness": player.stand.weakness if player.stand else None,
        "alternative_power": player.alternative_power,
        "motivation": player.motivation,
        "battle_number": battle_number,
        "saved_at": datetime.now().isoformat()
    }

    path = get_save_path(player.name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(save_data, f, indent=4)
    print(f"\nGame saved as '{path}'")

def load_game():
    name = input("Enter the name of your character to load: ")
    path = get_save_path(name)
    if not os.path.exists(path):
        print("Save file not found.")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    from characters import Character, Stand
    loaded = Character(data["name"])
    loaded.hp = data["hp"]
    loaded.motivation = data["motivation"]
    loaded.alternative_power = data["alternative_power"]
    if data["stand"]:
        loaded.stand = Stand(data["stand"], data["stand_ability"], data["stand_weakness"])

    print(f"\nLoaded character: {loaded.name} (HP: {loaded.hp})")
    print(loaded.describe())

    from battle import start_battle_sequence
    start_battle_sequence(loaded, start_index=data["battle_number"])

def prompt_save_game(player, battle_number):
    choice = input("\nDo you want to save your progress? (y/n): ").strip().lower()
    if choice == "y":
        save_game(player, battle_number)