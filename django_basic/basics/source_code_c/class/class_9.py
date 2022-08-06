# python(ポリモーフィズム(多態性))
#- python(ポリモーフィズム(多態性))をする場合、普通の継承と違い、
#- 小クラスでdef __init__(self,xx): をする必要なく、
#- 親クラスで@abstractmethod と 小クラスで対象メソッドをオーバーライドするだけで良い

#- 逆に言えば、通常の継承では、小クラスでdef __init__(self,xx): をする必要あり!!

from abc import abstractmethod, ABCMeta

# class Person: # 親クラス
class Person(metaclass=ABCMeta): # 親クラス

    def __init__(self, name, age):
        print('小クラスを呼び出すと、親クラスが強制発動!! __init__コンストラクタの中に処理があるため')
        self.name = name
        self.age = age

    @abstractmethod
    def greeting(self):
        print('hello {}'.format(self.name))

    def say_age(self):
        print('{} years old'.format(self.age))

class Employee(Person): # Personの機能を継承する
    def greeting(self):
        print('hello {}'.format(self.name))

man = Employee('Tonegawa', 45)
man.greeting() #- 親クラスのメソッドをオーバーライドしている
man.say_age() #- Employeeインスタンスから親クラスのメソッドを呼び出している