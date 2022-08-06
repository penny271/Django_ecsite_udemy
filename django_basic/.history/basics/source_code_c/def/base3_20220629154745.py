# グローバル変数

def printAnimal():
    #- global animal #animalの前に、globalを付けて、global変数として宣言するとこのanimalは 関数の外までスコープが広がります(同名の 変数が関数の外に存在する場合は、同じ参照先になります) - 20220629
    global animal
    animal = 'Cat'
    print('関数内animal = {}, id = {}'.format(animal, id(animal)))

# animal = 'Dog'
printAnimal()
print('関数外animal = {}, id = {}'.format(animal, id(animal)))