# セット
#- ★★★new 20220628

#セットは、リスト[]、タプル()と似たように複数の値を入れる入れ物です
# • 同じ値を持つことがない(ユニーク)
# • 順序が保持されていない(挿入された順番通りに取り出すことができない) • ユニオンやインターセクションなどの集合処理を高速で行うことができる

set_a = {'a', 'b', 'c', 'd', 'a', 12}

print(set_a)
print('e' not in set_a)

print(12 in set_a)
print(len(set_a))

#- ★★★new 20220628
# # add, remove, discard, pop, clear
# set_a.add('e')
# print(set_a)

# set_a.remove('e')
# print(set_a)
# # set_a.remove('E')
# set_a.discard(12)
# print(set_a)
# set_a.discard(12)

# print(set_a)
# val = set_a.pop()
# print(val)
# print(set_a)
# set_a.clear()
# print(set_a)

set_a.add('A')
print(set_a)

set_a.remove('a')
print(set_a)
