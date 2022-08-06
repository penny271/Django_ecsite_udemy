# python(ポリモーフィズム(多態性))
#- サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスか意識せずに呼び出すこと

from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta): # 親クラス

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    def say_something(self):
        print('女性: 名まえは={}'.format(self.name))

class Man(Human):

    def say_something(self):
        print('男性: 名まえは={}'.format(self.name))

human = Woman('Hanako')



# # ポリモーフィズム
# num = input('0か1を入力してください')
# if num == '0':
#     human = Man('Taro')
# elif num == '1':
#     human = Woman('Hanako')
# else:
#     print('入力が間違っています')
# human.say_something()
