# セットの関数
#- ★★★new 20220628
# union(|)・・・ユニオン、和集合を返します。 intersection(&)・・・集合の共通する要素、積集合を返します。 difference(-)・・・片方の集合にあり、片方の集合にない要素、差集合を返します symmetric_difference(^)・・・どちらか一方にだけある要素の集合を返します
#!
# s = {'a', 'b', 'c', 'd'}
# t = {'c', 'd', 'e', 'f'}

# u = s | t # 和集合
# u = s.union(t) # 和集合

# print(u)

# u = s & t # 積集合
# u = s.intersection(t)

# print(u)

# u = s - t # 差集合
# u = s.difference(t)
# print(u)

# u = s ^ t
# u = s.symmetric_difference(t)
# print(u)

# s |= t # => s = s | t => sがsとtの和集合=>sにtの要素が入る
# print(s)

# # issubset, issuperset, isdisjoint
# s = {'apple', 'banana'}
# t = {'apple', 'banana', 'lemon'}
# u = {'cherry'}

# print(s.issubset(t))
# print(s.issuperset(t))
# print(t.isdisjoint(s))
# print(t.isdisjoint(u))

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

u = s | t # 和集合
print(u)

u = s & t 

