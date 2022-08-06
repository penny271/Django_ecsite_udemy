# 1~100 3:Fizz,5:Buzz,15:FizzBuzz

for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print('{}: Fizz Buzz'.format(i))
    elif i % 3 == 0:
        print('{} :Fizz'.format(i))
    elif i % 5 == 0:
        print('{}: Buzz')
    else:
        print(i)
