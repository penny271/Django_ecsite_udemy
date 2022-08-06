# Map関数

# list_a = [1,2,3,4,5]

# map_a = map(lambda x: x * 2, list_a)

# for x in map_a:
#     print(x)

# man = {
#     'name': 'Ichiro',
#     'age': '18',
#     'country': 'Japan'
# }
# map_man = map(lambda x: x + ',' + man.get(x), man)
# for x in map_man:
#     print(x)

# def calcurate(x, y, z):
#     if z == 'plus':
#         return x + y
#     elif z == 'minus':
#         return x - y

# map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus'])
# for x in map_sample:
#     print(x)


list_a = [1,2,3,4,5]

man = {
    'name': 'Ichiro',
    'age': '18',
    'country': 'Japan'
}

map_a = map(lambda x: x*2, list_a)

map_man = map(lambda x: f'{x}: {man.get(x)}',man)

# print([a for a in map_a])
# print([b for b in map_man])

print('[x for x in map_man]: ',[x for x in map_man])

for x in map_man:
    print(x)

# print(range(5))
# print(type(range(5)))


def calculate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y

map_sample = map(calculate,range(5), [3,3,3,3,3], ['plus','plus','minus','plus','minus','plus'])

for x in map_sample:
    print(x)


#- オリジナル - 20220721

def calc(*args):
    print(args)
    if args[0] == 1:
        return 'ok'
    elif args[1] == 2:
        return 'so so'
    else:
        return (f'{args[0]},{args[1]},{args[2]}')

yyy = map(calc,[1,9,18],['a',2,'c'],[4,5,6] )

zzz = [y for y in yyy]
print('yyy: ',zzz) # yyy:  ['ok', '2,b,5', '3,c,6']