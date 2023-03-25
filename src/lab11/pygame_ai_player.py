import random
from turn_combat import CombatPlayer
""" Create PyGameAIPlayer class here"""


class PyGameAIPlayer:
    def __init__(self) -> None:
        pass

    def selectAction(self, state):
        return random.randint(0,9)  # Not a safe operation for >10 cities

def random_weapon_select():
    return random.randint(0, 2)
""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.initial_weapon = random_weapon_select()
    
    def weapon_selecting_strategy(self):
        if self.opponent_choices == []:
            return self.initial_weapon
        elif len(self.my_choices)>2:
            if self.opponent_choices[-1] == self.my_choices[-2] and self.opponent_choices[-2] == self.my_choices[-3]:
                return (self.my_choices[-1]+1)%3
        return (self.opponent_choices[-1]+1)%3
    """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [ord("s"), ord("a"), ord("f")]:
                        choice = {ord("s"): 1, ord("a"): 2, ord("f"): 3}[event.key]
                        self.weapon = choice - 1
                        return self.weapon
    """