from custom import get_all_stands, only_custom_stands
import random
import openai
from characters import Character, Stand, get_random_name
from savegame import prompt_save_game
from episodes import generate_episode_summary, save_episode_text

def generate_ai_battle(action, player, enemy, scenario, turn, prev_summary):
    prompt = f"""
    Write a JoJo-style battle scene (Turn {turn}/3).
    Player: {player.name}, HP: {player.hp}, Stand: {player.stand.name if player.stand else player.alternative_power}
    Enemy: {enemy.name}(if the enemy has references in its name catch it and respond accordingly), HP: {enemy.hp}, Stand: {enemy.stand.name}, Weakness: {enemy.stand.weakness}, Motivation: {enemy.motivation}
    Scenario: {scenario}
    Player action: {action}
    Player's Motivation: {player.motivation}
    Previous summary: {prev_summary if prev_summary else 'This is the first turn.'}
    The enemy should appear dominant early on, but the player can slowly gain ground.
    Make it dramatic and bizarre, 8–12 sentences.
    Include inner monologue about the motivation.
    At the end, estimate the damage the player took this turn (0–30 range), and also the damage dealt to the enemy (10–60 range).
    Output like this:
    [SCENE] ...full scene here...
    [DAMAGE_TAKEN] X
    [DAMAGE_DEALT] Y
    """
    response = openai.ChatCompletion.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.95,
        max_tokens=400
    )
    return response['choices'][0]['message']['content'].strip()

def parse_battle_result(text):
    damage_taken = random.randint(5, 30)
    damage_dealt = random.randint(10, 60)
    lines = text.splitlines()
    for line in lines:
        if line.startswith("[DAMAGE_TAKEN]"):
            try:
                damage_taken = int(line.split("[DAMAGE_TAKEN]")[1].strip())
            except:
                pass
        elif line.startswith("[DAMAGE_DEALT]"):
            try:
                damage_dealt = int(line.split("[DAMAGE_DEALT]")[1].strip())
            except:
                pass
    return damage_taken, damage_dealt

def start_battle_sequence(player, start_index=0):
    SCENARIOS = [
        "In the ruins of a casino suspended over a volcano",
        "Inside a frozen submarine spiraling underwater",
        "While skydiving from a crumbling space elevator",
        "Within a moving carnival train in the desert"
    ]

    enemies = [
        Character(get_random_name()),
        Character(get_random_name()),
        Character(get_random_name()),
        Character(get_random_name())
    ]

    for index, enemy in enumerate(enemies[start_index:], start=start_index):
        scenario = random.choice(SCENARIOS)
        enemy.stand = random.choice(get_all_stands())
        enemy.hp = 100
        enemy.motivation = "Unknown Ambition"

        print(f"\n=== BATTLE {index+1}: {enemy.name} ===")
        print(f"Location: {scenario}")
        print(enemy.describeEnemy())

        summary = ""
        for turn in range(1, 4):
            action = input(f"\n[TURN {turn}] What does {player.name} do? → ")
            result = generate_ai_battle(action, player, enemy, scenario, turn, summary)
            print("\n" + result)
            summary += "\n" + result
            damage_taken, damage_dealt = parse_battle_result(result)

            player.hp -= damage_taken
            enemy.hp -= damage_dealt

            print(f"\n{player.name} took {damage_taken} damage! HP remaining: {player.hp}")
            print(f"{enemy.name} took {damage_dealt} damage! HP remaining: {enemy.hp}")

            if player.hp <= 0:
                print("\n=== YOU HAVE FALLEN IN BATTLE ===")
                return
            if enemy.hp <= 0:
                print(f"\n=== {enemy.name} WAS DEFEATED BEFORE TURN 3! ===")
                break

        if enemy.hp > 0:
            print(f"\n=== FINAL STRIKE! {player.name} finishes off {enemy.name} ===")
            enemy.hp = 0

        print(f"\n=== {enemy.name} DEFEATED ===")
        heal = random.randint(0,20)
        player.hp =+ heal
        print(f"{player.name} healed {heal} HP!")
        episode_text = generate_episode_summary(player, summary, index + 1)
        print("\n=== EPISODE SAVED ===")
        save_episode_text(player.name, episode_text, index + 1)

        prompt_save_game(player, index+1)

    print("\n=== YOU HAVE COMPLETED THE GAME!===")
    print("A new legend is born.")
