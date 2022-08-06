# Dictionary(辞書型)

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015, 1: 100}

#- ★★★new - 20220628 car.get(‘brand’)
# print(car.get(‘brand’)) #取り出せなかったNone
# # 変数[‘キー’]または、変数.get(‘キー’)とすることで値を取り出すことができます。上の例では、Toyota
# print(car.get(‘Model’, ‘Does not exist’))
# # carにModelというキーが存在しない場合、Does not existを返します
print(car['brand'])
print(car.get('bran', 'car.get("bran"): Does not exist'))

print(car.get(1))

#- new 20220628
print(car.keys()) # キー一覧
print(car.values()) # 値一覧
print(car.items()) # キー + 値

# for k, v in car.items():
#     print('key = {}, value = {}'.format(k, v))

#- brandというキーが存在する場合だけ実行する
if 'bran' in car:
    print('carのブランドは{}'.format(car['brand']))

# for k,v in car.items():
#     print(f'key: {k}, value: {v}')