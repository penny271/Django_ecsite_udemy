# 関数
#- num = num_max(b=20, a=10) # 引数を直接指定することもできます

def print_hello():
    print('Hello World')

print_hello()

#- 肩を
def num_max(a: int, b: int):
    print('a = {}, b = {}'.format(a, b))
    if a > b:
        return a
    else:
        return b
#- num = num_max(b=20, a=10) # 引数を直接指定することもできます
print(num_max(b=100,a=20))
print(num_max())