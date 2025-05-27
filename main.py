import random
import openai
import json
from characters import Character
from custom import create_custom_stand, view_custom_stands, get_all_stands, only_custom_stands
from plotline import assign_motivation, assign_plotline, describe_plotline
from battle import start_battle_sequence
from savegame import save_game, load_game
from apikey import apikey

openai.api_key = apikey


def main_menu():
    while True:
        print("\n=== JOJO: THE AI CHRONICLES ===")
        print("1. Play Game")
        print("2. Design Custom Stand")
        print("3. View Custom Stands")
        print("4. Load Saved Game")
        print("5. Exit")
        choice = input("> ")

        if choice == "1":
            choose_game_mode()
        elif choice == "2":
            create_custom_stand()
        elif choice == "3":
            view_custom_stands()
        elif choice == "4":
            load_game()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

def choose_game_mode():
    while True:
        print("Choose your game mode:")
        print("1. Classic Mode (All stands)")
        print("2. Custom Stands Only")
        mode = input("> ").strip()

        if mode == "1":
            new_game(custom_only=False)
            break
        elif mode == "2":
            if not only_custom_stands():
                print("No custom stands found! Redirecting you to Stand Designer...")
                create_custom_stand()
                break
            new_game(custom_only=True)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    custom_only = mode.strip() == "2"
    new_game(custom_only)

def new_game(custom_only):
    print("\n=== CHARACTER CREATION ===")
    name = input("Enter your character's name: ")


    if name.lower() == "33":
        name = "Gustave"
        print("(Easter Egg Activated: Gustave Mode)")
    elif name.lower() == "55":
        name = "Kazım Timuçin Utkan"
        print("(Easter Egg Activated: Instructor Mode)")
    elif name.lower() == "muda":
        name = "DIO"
        print("(Easter Egg Activated: ZA WARUDO!!)")

    player = Character(name)
    player.assign_random_power(custom_only=custom_only)

    print("\n=== CHARACTER SUMMARY ===")
    print(player.describe())

    player.motivation = assign_motivation()
    print(f"\nMotivation: {player.motivation}")

    player.plotline = assign_plotline()
    print("\n" + describe_plotline(player.plotline))


    start_battle_sequence(player)

if __name__ == "__main__":
    main_menu()
