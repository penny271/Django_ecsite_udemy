# Dictionary(辞書型)

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

#- ★★★new
# print(car.get(‘brand’)) #取り出せなかったNone
# # 変数[‘キー’]または、変数.get(‘キー’)とすることで値を取り出すことができます。上の例では、Toyota
# print(car.get(‘Model’, ‘Does not exist’))
# # carにModelというキーが存在しない場合、Does not existを返します
print(car['brand'])
print(car.get('bran', 12))

print(car.get(1))

print(car.keys()) # キー一覧
print(car.values()) # 値一覧
print(car.items()) # キー + 値

for k, v in car.items():
    print('key = {}, value = {}'.format(k, v))

if 'bran' in car:
    print('carのブランドは{}'.format(car['brand']))
