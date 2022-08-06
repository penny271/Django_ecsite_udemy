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

#- ジェネレータ関数
def generator(max):
    print('ジェネレータ作成' ,n)
    for n in range(max): # n=>0
        yield n
        print('yield実行: ',n)

gen = generator(10)
#- a = next(gen) # generatorを呼び出します
next(gen)