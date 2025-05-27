
import random

class Stand:
    def __init__(self, name, ability, weakness):
        self.name = name
        self.ability = ability
        self.weakness = weakness

    def describe(self):
        return f"Stand: {self.name}\n - Ability: {self.ability}\n - Weakness: {self.weakness}"

class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.stand = None
        self.alternative_power = None  # Hamon veya Spin
        self.motivation = None

    def assign_random_power(self, custom_only=False):
        from custom import get_all_stands, only_custom_stands

        if custom_only:
            all_stands = only_custom_stands()
        else:
            all_stands = get_all_stands()

        if random.random() > 0.1:
            self.stand = random.choice(all_stands)
        else:
            self.alternative_power = random.choice(["Hamon", "Spin"])


    def describe(self):
        info = f"Character: {self.name}\nHP: {self.hp}"
        if self.stand:
            info += f"\n{self.stand.describe()}"
        else:
            info += f"\nPower: {self.alternative_power}"
        return info
    def describeEnemy(self):
        ahmed = f"Character: {self.name} appears in your way!"
        return ahmed


def get_random_name():
    names = ["Renoir","DIO","Funny Valentine","Doğuhan","Zeynep Esin","Tareq","Mustafa","Ersin Ege","Cem Çetin","Red White","Yamen","Ahmed",
             "Kanye West","Ye","Drake","Kendirck Lamar","Yasuo","Puppet Master","Ali Koç","Sephiroth","Joker(DC)","JOKER(PERSONA)","Dr Doom",
             "Duke Erisia","Daft Punk(Dual Fight)","Ado","Abo","Tame Impala","The Ferryman","Primadon","Chaser, Scholar of the Crimson Contract",
             "Nautilodaunt","Donquixote Doflamingo","Masayuki Suzuki","ChatGPT","Pontiff Sulyvahn","Morgott","Radahn","Randy Orton","Rey Mysterio",
             "Calamitas","Undertaker","Jeff hardy","John Cena","Roman Reigns","Terrarian","Steve Minecraft","John Enemy","Pyke","Gurt","Kevin",
             "Jonesy Fortnite","Eren","Alicia","Simon the Digger","Kamina","Kittan Bachika","Viral(Tengen Toppa Gurren Lagann)"]
    return random.choice(names)