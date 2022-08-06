# 文字列型

# fruit = 'apple' # ""
# print(fruit)
# print(type(fruit))

#- new 文字列をかけることができる -20220628
# print(fruit * 10)

# new_fruit = fruit + ' banana'
# print(new_fruit)

# """
# fruits = """apple
# banana
# grape
# """
# print(fruits)

# fruit = 'banana'
# print(fruit[2])

#- new -20220628
# # encode, decode(bytes[]型の関数) => bytes[]
# byte_fruit = fruit.encode('utf-8')

# print(byte_fruit)
# print(type(byte_fruit))
# str_fruit = byte_fruit.decode('shift-jis')
# print(str_fruit)
# print(type(str_fruit))

#- new 20220628
# count関数

msg = 'ABCDEABC'

print(msg.count('ABCDEF'))

#- new 20220628
# # startswith endswith

# print(msg.startswith('ABCD'))
# print(msg.endswith('FABC'))
# print(msg.endswith('ABC'))

# #　strip, rstrip, lstrip

#- new 20220628 順不同で存在した場合に削除していく
# print(msg.strip('ACB')) #DE
# print(msg.rstrip('ACB')) #ABCDE #右端
# print(msg.lstrip('ACB')) #DEABC #左端

#- new 20220628
# # upper, lower, swapcase, replace, capitalize

# msg = 'abcABC'
# msg_u = msg.upper()
# msg_l = msg.lower()
# msg_s = msg.swapcase() # 大文字小文字入れ替え

# print(msg_u)
# print(msg_l)
# print(msg_s)

#- new 20220628 第3引数最初のものだけ変換される
# msg = 'ABCDEABC'
# msg_r = msg.replace('ABC', 'FFF', 1)
# print(msg_r)

# msg = 'hELLO world'
# print(msg.capitalize())

#- new 20220628
# 文字列の一部取り出し、format関数、文字列から数値への変換、islower, isupper
msg = 'h '
print(msg.isupper())
print(msg.islower())

msg = 'hello, my name is taro'

print(msg[0:10:2])
name = 'Hanako'
msg = f'my name is {name}' # 3.6
msg = f'my name is {name=}' # 3.8

print(msg)

msg = '12.21'
int_msg = float(msg)
print(int_msg)
print(type(int_msg))

#- new 20220628
# find, index, rfind, rindex
print(msg.find('ABC'))
print(msg.rfind('ABC'))
print(msg.index('ABC'))
print(msg.rindex('ABC'))

print(msg.find('ABCE')) #-1
print(msg.index('ABCE')) #- error発生

msg = 'ABCDEABC'
print(msg.rfind('ABDC'))
