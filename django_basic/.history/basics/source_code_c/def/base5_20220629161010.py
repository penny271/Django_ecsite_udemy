# ジェネレータ関数
#- ジェネレータ関数は以下のようにyieldを用いる

# def generator(max):
#     print('ジェネレータ作成')
#     for n in range(max): # n=>0
#         try:
#             x = yield n
#             print('x = {}'.format(x))
#             print('yield実行')
#         except ValueError as e:
#             print('throwを実行しました')

# gen = generator(10)
# next(gen)
# gen.send(100)
# # gen.throw(ValueError('Invalid Value'))
# # gen.close()
# next(gen)
# # for x in gen:
# #     print('x = {}'.format(x))
# # send

#-def func(): yield 〇〇
#- • ジェネレータ関数を宣言して実行すると、yieldの部分で処理がストップし、yieldの〇〇に記載された値(配列、辞書等オ ブジェクト)が呼び出し元に返されます。
#- • その後、再度ジェネレータ関数を呼び出すと、yieldの部分から処理がスタートし、yieldの部分でストップします。
#- • プログラムが終了するまで、何度もジェネレータ関数を呼び出すことができます。(その度に、yieldからスタート、yield
#- で終了します)

#- ジェネレータ関数
def generator(max):
    print('ジェネレータ作成')
    for n in range(max): # n=>0
        yield n
        print('yield実行: ',n)

gen = generator(10)
#- a = next(gen) # generatorを呼び出します
n = next(gen)
print(f'{n=}')
n = next(gen)
print(f'{n=}')
