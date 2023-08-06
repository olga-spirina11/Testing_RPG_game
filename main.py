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

    process_game(player, enemy)


def process_game(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"{player.name} HP: {player.health}, {enemy.name} HP: {enemy.health}")
        if not player.decision(enemy):
            break
        if enemy.is_alive():
            enemy.attack(player)


if __name__ == '__main__':
    game()


def test_hero_defeat_enemy(monkeypatch, capsys):
    # given
    player = Player('test_hero', 20, 10)
    enemy = Enemy('test_enemy', 15, 5)

    # when
    inputs = iter(['a', 'a'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    process_game(player, enemy)

    # then
    captured = capsys.readouterr().out
    expected = 'test_hero HP: 20, test_enemy HP: 15\n' \
               'test_hero attacks test_enemy!\n' \
               'test_enemy attacks test_hero!\n' \
               'test_hero HP: 15, test_enemy HP: 5\n' \
               'test_hero attacks test_enemy!\n'
    assert captured == expected


def test_enemy_defeat_hero(monkeypatch, capsys):
    # given
    player = Player('test_hero', 10, 10)
    enemy = Enemy('test_enemy', 30, 5)

    # when
    inputs = iter(['a', 'a'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    process_game(player, enemy)

    # then
    captured = capsys.readouterr().out
    expected = 'test_hero HP: 10, test_enemy HP: 30\n' \
               'test_hero attacks test_enemy!\n' \
               'test_enemy attacks test_hero!\n' \
               'test_hero HP: 5, test_enemy HP: 20\n' \
               'test_hero attacks test_enemy!\n' \
               'test_enemy attacks test_hero!\n'

    assert captured == expected


def test_hero_run_after_attack(monkeypatch, capsys):
    # given
    player = Player('test_hero', 50, 10)
    enemy = Enemy('test_enemy', 50, 5)

    # when
    inputs = iter(['a', 'r'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    process_game(player, enemy)

    # then
    captured = capsys.readouterr().out
    expected = 'test_hero HP: 50, test_enemy HP: 50\n' \
               'test_hero attacks test_enemy!\n' \
               'test_enemy attacks test_hero!\n' \
               'test_hero HP: 45, test_enemy HP: 40\n' \
               'test_hero runs away...\n'

    assert captured == expected

def test_hero_heal_and_defeat_enemy(monkeypatch, capsys):
    # given
    player = Player('test_hero', 10, 10)
    enemy = Enemy('test_enemy', 15, 5)

    # when
    inputs = iter(['a', 'h', 'a'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    process_game(player, enemy)

    # then
    captured = capsys.readouterr().out
    expected = 'test_hero HP: 10, test_enemy HP: 15\n' \
               'test_hero attacks test_enemy!\n' \
               'test_enemy attacks test_hero!\n' \
               'test_hero HP: 5, test_enemy HP: 5\n' \
               'test_hero heals!\n' \
               'test_enemy attacks test_hero!\n' \
               'test_hero HP: 10, test_enemy HP: 5\n' \
               'test_hero attacks test_enemy!\n'

    assert captured == expected
