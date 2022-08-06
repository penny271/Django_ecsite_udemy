# コンストラクタ, デストラクタ
#- オブジェクトをインスタンス化する際に呼び出されるメソッドをコンストラクタと言います。
#- デストラクタ(__del__)を定義すると、インスタンスを削除する際に呼び出されます。

class SampleClass:

    def __init__(self, msg, name = None): # コンストラクタ
        print('コンストラクタが呼ばれました')
        self.msg = msg # インスタンス変数
        self.name = name  # インスタンス変数

    #- デストラクタ
    def __del__(self):
        print('デストラクタが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var_1 = SampleClass('Hello', 'Jiro')
var_1.print_msg()
var_1.print_name()
del var_1




















# class SampleClass:

#     def __init__(self, msg, name=None): # コンストラクタ
#         print('コンストラクタが呼ばれました')
#         self.msg = msg # インスタンス変数
#         self.name = name # インスタンス変数

#     def __del__(self):
#         print('デストラクタが実行されました')
#         print('name = {}'.format(self.name))

#     def print_msg(self):
#         print(self.msg)

#     def print_name(self):
#         print(self.name)

# var_1 = SampleClass('Hello', 'Jiro')
# var_1.print_msg()
# var_1.print_name()
# del var_1