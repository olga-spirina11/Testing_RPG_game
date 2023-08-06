

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print(f"{self.name} attacks {enemy.name}!")

    def is_alive(self):
        return self.health > 0

class Player(Character):
    def decision(self, enemy):
        decision = input("Do you want to [A]ttack, [H]eal, or [R]un away? ")
        if decision.upper() == "A":
            self.attack(enemy)
        elif decision.upper() == "H":
            self.health += 10
            print(f"{self.name} heals!")
        elif decision.upper() == "R":
            print(f"{self.name} runs away...")
            return False
        return True

class Enemy(Character):
    pass

def game():
    player = Player("Hero", 50, 10)
    enemy = Enemy("Enemy", 50, 5)

    while player.is_alive() and enemy.is_alive():
        print(f"{player.name} HP: {player.health}, {enemy.name} HP: {enemy.health}")
        if not player.decision(enemy):
            break
        if enemy.is_alive():
            enemy.attack(player)

game()

def test_hero_defeat_enemy():

    #given

    player = Player('test_hero', 20, 10)
    enemy = Enemy('test_enemy', 15, 5)



    #when

    # Запускаем игру
    game()
    print('A')

    #then

    # output 'A'
    # check stdout
    assert 'test_hero attacks test_enemy!'

    # output 'A'
    # check stdout












