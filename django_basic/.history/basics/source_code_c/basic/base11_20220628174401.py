# 辞書の関数

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_dict = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}
#- ★★★new 20220628 .update({'country': 'Japan', 'prefecture': 'Aichi'})
car.update(tmp_dict) #値の追加、更新
print(car)
car['city'] = 'Toyota-shi' #値の直接更新
car['year'] = 2017
print(car)

value = car.popitem()
print(car)
print('car.popitem():', value)

value = car.pop('model')
print(car)
print(value)

car.clear()
print(car)
del car
print(car)
