# デフォルト値、可変長引数、複数の返り値
#- 複数の返り値 return a, b
#- 可変長引数: 場合に応じてその都度、引数の長さが変わるもの *arg1のように*を一つつけると、可変長のタプル
#- **arg2のように*を2つつけると、可変長の辞書

#- デフォルト値
def sample(arg1, arg2=100):
    print(arg1, arg2)

# sample(200)

def spam(arg1, *arg2):
    print("arg1 = {}, arg2 = {}".format(arg1, arg2))
    print(type(arg2))

spam(1,2,3,4,5)

def spam_2(arg1, **arg2):
    print('arg1 = {}, arg2 = {}'.format(arg1, arg2))
    print(type(arg2))

spam_2(3, name='Taro', 20)

def spam_3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

spam_3(1,2,3,4,5,name='Taro', age=15)

def sample_2():
    return 1, 2, 3

a,b, c = sample_2()
print(a,b,c)