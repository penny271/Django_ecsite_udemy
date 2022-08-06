# 高階関数
#- pythonでは、関数もオブジェクトの一つにすぎないため変数として扱うこともできます。また、関数を他の関数の引数として渡したり、返り 値として扱うこともできます。
#-関数を引数にしたり、返り値にする関数を高階関数と言います

# def print_hello():
#     print('hello')

# def print_goodbye():
#     print('goodbye')

# var = ['AA', 'BB', print_hello, print_goodbye]
# var[2]()
# var[3]()

def print_world(msg):
    print('{} world'.format(msg))

def print_konnichiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konnichiwa

var = print_hello(print_world)
var()