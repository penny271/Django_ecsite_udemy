# all, any
#- python(all, any関数)
#- ★★★new 20220628
# #^ allはオブジェクトの中が全てTrueの場合に処理をする
# if all(反復可能オブジェクト): # リスト、タプル等、for in でループできる変数を入れます。
# 処理
# #^ anyはオブジェクトの一部がTrueの場合に処理をする if any(反復可能オブジェクト):

# if all((30 < 10, 10 < 20, 'a' == 'a')): # allは全てTrue
#     print('allの中の処理')

# if not any((30<20, 10<5, 'a' == 'b')): # anyは1つでもTrue
#     print('anyの中の処理')

if all((True,True,True, 30 <10)):
    print('all')

if any((False, True, False)):
    print('any')


if all((True,True,False)):
    