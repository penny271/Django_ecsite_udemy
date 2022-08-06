# base5.py

# from abc import abstractmethod, ABCMeta

# class Animal(metaclass=ABCMeta): #親クラス

#     @abstractmethod
#     def speak(self):
#         pass

class Dog:

    def speak(self):
        print('わん')

class Cat:

    def speak(self):
        print('にゃー')

class Sheep:

    def speak(self):
        print('めー')

class Other:

    def speak(self):
        print('そんな動物はいない')

number = input('好きな動物は？ 1: 犬、2: 猫, 3:羊')

if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak()



