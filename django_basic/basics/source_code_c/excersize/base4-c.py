

# from decimal import Clamped

class CharacterAlreadyExistException(Exception): #- 継承
    pass

class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls,name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistException('キャラクターはすでに存在しています')
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_delete(cls,name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:

    def __init__(self, name, hp, offense, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print('キャラクターはすでに死んでいます')
            return
        attack_point = self.offense - enemy.defense
        attack_point = 1 if attack_point <= 0 else attack_point
        enemy.hp -= attack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_delete(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)

character_a = Character('A', 10, 5, 3)
character_b = Character('B', 8, 6, 2)

print(character_b.hp)
# character_a.attack(character_b)
character_a.critical_hit(character_b) # 8 -> 2
print(character_b.hp)
print('alive: ', AllCharacters.alive_characters)
print('dead: ', AllCharacters.dead_characters)
character_a.attack(character_b) # 2-> -1
print('alive: ', AllCharacters.alive_characters)
print('dead: ', AllCharacters.dead_characters)
character_b.attack(character_a)
# character_c = Character('A',10,8,6) #- 例外処理発動 同じ名前なので



#- 自作
# class Character:

#     def __init__(self,name, hp, offense, defense):
#         self.name = name
#         self.hp = hp
#         self.offense = offense
#         self.defense = defense

#     def attack(self, enemy_instance):
#         damage = self.offense - enemy_instance.defense
#         print(damage)
#         return damage

# player1 = Character('p1', 100, 50, 40)
# player2 = Character('p2', 90, 40, 35)


# print(player1.attack(player2))
# print(player2.hp)