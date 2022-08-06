# setter, getter その2

# 【カプセル化の方法2】 @property,@var.setter
# python(カプセル化, setter, getter)
#-------------------

from tempfile import gettempprefix


class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): # getter
        print('getter nameが呼ばれました')
        return self.__name

    @property
    def age(self):
        print('getter ageを呼ばれました')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter nameが呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        #- 変更しようとしている値が正しいか確認できる
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

human = Human('Koichi', 22)
human.name = 'Makoto'
print(human.name)
human.age = -1
print(human.age)




#-----自作-------- 20220721
# class Human:

#     def __init__(self, name, age):

#         self.__name = name #- private変数
#         self.__age = age

#     @property
#     def name(self):
#         print('name getter 呼び出し')
#         return self.__name

#     @property
#     def age(self):
#         print('age getter 呼び出し')
#         return self.__age

#     @name.setter
#     def name(self, name):
#         if len(name) > 3:
#             pre_name = self.__name
#             self.__name = name
#             print(f'name setter 値変更! {pre_name} => {self.__name}')
#         else:
#             print('name setter 呼び出し')

#     @age.setter
#     def age(self, age):
#         if age > 30:
#             print('age setter呼び出し')
#             self.__age = age

# men = Human('太郎', 44)
# men.name
# men.age
# men.name = 'ルイージ'


