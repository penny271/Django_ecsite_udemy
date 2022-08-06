# 再帰

# def sample(a):
#     if a < 0:
#         return
#     else:
#         print(a)
#         sample(a-1)

# sample(10)

# 1,1,2,3,5,8,13,21,34

#- 添付ファイル参照: フィボナッチ関数_20220720.jpg

# フィボナッチ
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2) #6の場合  結果8

    #fib(5) + fib(4)  1  => 0
    #fib(4) + fib(3)  1  => 0
    #fib(3) + fib(2)  2  => 1
    #fib(2) + fib(1)  3  => 1, 1
    #fib(1) + fib(0)  4  => 1, 1

for x in range(1, 10):
    print('結果:',fib(x))


# #- test
# def fib(n):
#     return 1 if n < 3 else fib(n-1) + fib(n-2) #5の場合

#     #fib(4) + fib(3)  1
#     #fib(3) + fib(2)  2  => 1
#     #fib(2) + fib(1)  3  => 1, 1
#     #fib(3) + fib(2)  4

# for x in range(1, 10):
#     print('x:',fib(x))
