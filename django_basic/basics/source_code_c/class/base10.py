# private変数
#- Private変数 アンダースコア(_)を二つ付けて定義

class Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name # private変数
        self.__age = age

    #- 下記のようにクラス内からはPrivate変数を使用できる
    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Taro', 15)
#- private変数はクラスの外からはアクセスできない - クラス内のみアクセス可能
# print(human.__name)
# print(human._Human__name) #! 例外的にアクセスできるが基本使わない
# human.print_msg()

human.print_msg()











# class Human:

#     __class_val = 'Human'

#     def __init__(self, name, age):
#         self.__name = name # private変数
#         self.__age = age

#     def print_msg(self):
#         print('name = {}, age = {}'.format(self.__name, self.__age))


# human = Human('Taro', 15)
# human.print_msg()