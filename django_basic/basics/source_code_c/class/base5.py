# 特殊関数

class Human:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    #- str(object), print(object)の際に呼び出され、オブジェクトを文字列として返す
    def __str__(self):
        return '★def __str__(self): name = {}, age = {}, phone_number: {}'.format(self.name, self.age, self.phone_number)

    #- ==が実行される際に呼ばれる 例: print(man == man2)
    def __eq__(self, other): #! print(man == man2)  selfに man, otherに man2 が入る
        return (self.name == other.name) and (self.phone_number == other.phone_number)

    #- set_men = {man, man2, man3} セットが作成された際に呼び出される
    def __hash__(self):
        print('hash関数が呼ばれました')
        return hash(self.name + self.phone_number)

    #- if文が実行されたときに呼ばれ、判定を行う
    def __bool__(self):
        return True if self.age >= 20 else False
        if self.age > 20:
            return True
        else:
            return False

    def __len__(self):
        print('lenが呼ばれました')
        return len(self.name)
        return 2

man = Human('Taro', 20, '08011111111')
man2 = Human('Taro', 18, '08011111111')
man3 = Human('Jiro2', 18, '09011111111')
man_str = str(man)

print(man_str)

print(man == man2)
print(hash('Taro')) #- def __hash__(self)は関係なく通常のhash関数を使っている
print(hash('Taro')) #- def __hash__(self)は関係なく通常のhash関数を使っている
print(hash('Jiro')) #- def __hash__(self)は関係なく通常のhash関数を使っている

#- セット - 格納する値はハッシュ化可能でなければなりません。これは、setは要素のユニークさを判定する際にハッシュ値を利用するためです。
set_men = {man, man2, man3} #- def __hash__(self)が呼ばれる
for x in set_men:
    print(x)

if man:
    print('manはTrue')
if man2:
    print('manはTrue')

print(len(man)) #- def __len(self)__が呼ばれる
print(len(man3)) #- def __len(self)__が呼ばれる

# woman = Human('Elsa', 20, '08011111111')
# # w = str(woman)
# woman2 = Human('Elsa', 22, '08022222222')
# print(hash(woman))
# print(hash(woman2))
# # set, 辞書のキー
# dict_a = {
#     woman: 'AAA'
# }
# print(dict_a)
# if woman:
#     print('WomanはTrue')
# if woman2:
#     print('Woman2はTrue')

# print(len(woman))
# print(Human.__name__)