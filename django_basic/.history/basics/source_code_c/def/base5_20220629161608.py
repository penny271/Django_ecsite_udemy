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
#! 毎回next()で回数分呼び出すのは大変
n = next(gen)
print(f'最初: {n=}')
n = next(gen)
print(f'最初:{n=}')

#- ループさせることで解決できる
#- ジェネレータ関数はループ文で使うことがよくある!
for x in gen:
    print(f'{x=}')

print('\n', '='*20  ,'\n')

#- ジェネレータ関数には以下のメソッドがあります
#- send(): yieldで停止している箇所に値を送ります。 <= yieldの部分に変数を置き、yieldの結果を格納する必要あり
#- throw(): 指定した例外が発生して処理が終了させます。
#- close(): ジェネレータを正常終了させます。
def generator_02(max):
    print('ジェネレータ作成')
    for n in range(max): # n=>0
        x = yield n
        print(f'{x=}')
        print('yield実行: ',n)

gen_02 = generator_02(10)
next(gen)