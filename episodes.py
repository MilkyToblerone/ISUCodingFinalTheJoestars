import os
import json
import openai
from datetime import datetime

EPISODE_FOLDER = "data/episodes"
os.makedirs(EPISODE_FOLDER, exist_ok=True)

def generate_episode_summary(player, battle_summary, episode_number):
    prompt = f"""
    Create a JoJo-style anime episode summary.
    Episode {episode_number} follows {player.name}, whose motivation is: {player.motivation}.
    Stand: {player.stand.name if player.stand else player.alternative_power}.
    This episode covers a battle with the following details:
    {battle_summary}

    Give this episode a stylish, exaggerated JoJo-like title.
    Then write a 3-part episode summary (Part A, Part B, Part C).
    Use a tone similar to a real JoJo anime episode.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.95,
        max_tokens=500
    )
    return response['choices'][0]['message']['content'].strip()

def save_episode_text(player_name, episode_text, episode_number):
    filename = f"episode_{episode_number}_{player_name.lower().replace(' ', '_')}.txt"
    path = os.path.join(EPISODE_FOLDER, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(episode_text)
    print(f"\nEpisode {episode_number} saved as: {path}")
