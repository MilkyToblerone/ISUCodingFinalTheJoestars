import random

PLOTLINES = [
    {
        "title": "Steel Phantom Run",
        "goal": "Win a transcontinental horse race across America while surviving enemy Stand users."
    },
    {
        "title": "Heaven's Spiral",
        "goal": "Ascend a sacred spiral tower guarded by stand users and ancient machines."
    },
    {
        "title": "Red Planet Crusade",
        "goal": "Survive a deadly Stand tournament on a terraformed Mars."
    }
]
MOTIVATIONS = [
    "To cure their dying mother with the prize money",
    "To outrun a bounty placed on their head",
    "To uncover the truth about their past",
    "To fulfill a promise made to a fallen friend",
    "To protect a sacred artifact from evil hands",
    "To escape a Stand curse that slowly drains their soul",
    "To prove themselves worthy of their family legacy"
]

def assign_plotline():
    return random.choice(PLOTLINES)

def describe_plotline(plot):
    return f"=== MAIN PLOT: {plot['title']} ===\nGoal: {plot['goal']}"

def assign_motivation():
    return random.choice(MOTIVATIONS)