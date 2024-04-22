#66111375 กฤษดา ขันตรี

class Enemy:
    def __init__(self, name, health,speech,fight_dialogue, weakness):
        self.name = name
        self.fight_dialogue = fight_dialogue
        self.weakness = weakness
        self.speech =speech
        self.health = health



    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_fight(self, dialogue):
        self.fight_dialogue = dialogue

    def get_fight(self):
        return self.fight_dialogue

    def set_weakness(self, weak):
        self.weakness = weak

    def get_weakness(self):
        return self.weakness

    def fight(self, weapon, wdamage):
        if weapon == self.weakness:
            print(f"You use {weapon} and defeat {self.name}!")
            self.take_damage(wdamage)
        else:
            print(f"{self.name} attacks you!")
            self.take_damage(wdamage)


    def print_detail(self):
        print(f'====== Monster ({self.name})Detail =========')
        print(f'Health:{self.health}')
        print(f'Speech:{self.speech}')
        print(f'{self.name} raise his and says...')
        print(f'"We are friend now"')
        print(f'{self.name} give you Toy Bat')
