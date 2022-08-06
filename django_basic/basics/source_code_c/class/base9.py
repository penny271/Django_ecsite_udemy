# python(ポリモーフィズム(多態性))
#- サブクラスを複数作成し、同じメソッドを定義して呼び出す際にどのクラスか意識せずに呼び出すこと
from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta): # 親クラス

    def __init__(self, name):
        self.name = name

    #- #親クラスでは処理を定義しないメソッド。子クラスで必ずオーバーライドする(オーバーライド しないとABCMetaにはじかれる)
    @abstractmethod
    def say_something(self):
        pass

    def say_name(self):
        print(self.name)

class Woman(Human):
    #- TypeError: Can't instantiate abstract class Woman with abstract methods say_something <= @abstractmethodのメソッドをオーバーライドする必要あり
    # pass

    def say_something(self):
        print('女性: 名まえは={}'.format(self.name))

class Man(Human):
    def say_something(self):
        print('男性: 名まえは={}'.format(self.name))

human = Woman('Hanako')

# # ポリモーフィズム
num = input('0か1を入力してください')
if num == '0':
    human = Man('Taro')
    human.say_name()

elif num == '1':
    human = Woman('Hanako')
    human.say_name()
else:
    print('入力が間違っています')
human.say_something()
