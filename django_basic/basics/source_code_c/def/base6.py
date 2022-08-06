# サブジェネレータ

def sub_sub_generator():
    yield "Sub Subのyield"
    return "sub sub のreturn"

def sub_generator():
    yield "subのyield"
    res = yield from sub_sub_generator()
    print("sub res = {}".format(res))
    return "subのreturn"

def generator():
    yield "generatorのyield"
    res = yield from sub_generator()
    print('gen res = {}'.format(res))
    return 'generatorのreturn'

gen = generator()
print(next(gen)) # generatorのyield
print(next(gen)) # subのyield
print(next(gen)) # Sub Subのyield  / sub res = sub sub のreturn  /  gen res = subのreturn
print(next(gen)) # yeildがもうほかに無いため、呼び出すことができずエラーになる
print(next(gen)) #



