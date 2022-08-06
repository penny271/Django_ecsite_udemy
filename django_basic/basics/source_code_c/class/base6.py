# クラスの継承

class Person: # 親クラス

    def __init__(self, name, age):
        print('小クラスを呼び出すと、親クラスが強制発動!! __init__コンストラクタの中に処理があるため')
        self.name = name
        self.age = age

    def greeting(self):
        print('hello {}'.format(self.name))

    def say_age(self):
        print('{} years old'.format(self.age))

class Employee(Person): # Personの機能を継承する

    def __init__(self, name, age, number):
        super().__init__(name, age) # super()で親クラスにアクセスしている - 初期化
        self.number = number

    def say_number(self):
        print('my number is = {}'.format(self.number))

    def greeting(self): #- オーバーライド 上書き super()親クラスに存在しているため
        super().greeting()
        print('I\'m employee phone_number = {}'.format(self.number))

    #! pythonではオーバーロードは使用不可能 <= pythonでは引数が違くても上書きし、オーバーライドしてしまうため
    # def greeting(self, age): # オーバーロード 引数の数や返り値が違うメソッドを定義すること
    #     print('オーバーロード')

man = Employee('Tonegawa', 45, '0801111111')
man.greeting() #- 親クラスのメソッドをオーバーライドしている
man.say_age() #- Employeeインスタンスから親クラスのメソッドを呼び出している
man.say_number()















# class Employee(Person): # Personの機能を継承

#     def __init__(self, name, age, number):
#         super().__init__(name, age)
#         self.number = number

#     def say_number(self):
#         print('my number is = {}'.format(self.number))

#     def greeting(self): # オーバライド
#         super().greeting()
#         print('I\'m employee phone_number = {}'.format(self.number))

#     # def greeting(self, age): # オーバロード
#     #     print('オーバーロード')
# man = Employee('Tonegawa', 45, '08011111111')
# man.greeting()
# man.say_age()
# man.say_number()