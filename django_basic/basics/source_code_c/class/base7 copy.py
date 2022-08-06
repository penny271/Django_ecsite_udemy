# クラスの多重継承

class ClassA:

    def __init__(self, name, age=999):
        self.a_name = name
        self.age = age

    def print_a(self):
        print('ClassAのメソッド実行')
        print('a = {}'.format(self.a_name))

    def print_hi(self):
        print('A hi')

    def print_age(self):
        print('age', self.age)

class ClassB:

    def __init__(self, name):
        self.b_name = name

    def print_b(self):
        print('ClassBのメソッド実行')
        print('b = {}'.format(self.b_name))

    def print_hi(self):
        print('B hi')

class NewClass(ClassA,ClassB):

    def __init__(self, name):
        ClassA.__init__(self, name)
        ClassB.__init__(self, name)

newC = NewClass('Tom')

newC.print_a()
newC.print_age()
newC.print_b()