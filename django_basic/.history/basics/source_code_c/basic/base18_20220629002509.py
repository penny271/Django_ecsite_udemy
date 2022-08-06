# for

for i in range(10):
    print(i)

#- ★new 変数に値を格納するのではなく、ただループしたいことを強調したい場合に利用する -20220628
for _ in range(100):
    # print('A')
    pass

for i in range(2,20,3):
    print(i)

# sample = ['John', 'Paul', 'George', 'Ringo']
sample = ('John', 'Paul', 'George', 'Ringo')

for member in sample:
    print(member)

human = {
    'Name': 'Taro',
    'Age': 20,
    'gender': 'Man'
}

#- ★★★new human.get()を使うことで値を取り出せる -20220628
for h in human:
    print(h, ':', human.get(h))
    print(h, 'test: ', human[])