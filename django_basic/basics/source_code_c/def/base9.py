# if 1行 lambda
#- pythonで1行で終わるような関数を用いる場合には、lambda式という無名関数を用いることがよくあります。lambda式は以 下のように書きます。
#- lambda 引数: 返り値

y = 10
x = 0 if (y-20) > 0 else 1 # y>0 => 0 else 1
# print(x)

lambda_a = lambda x: x * x # 引数x 返り値x*x

print(lambda_a(10))
lambda_b = lambda x, y, z=5: x * y * z
print(lambda_b(2,3)) # x=2, y=3, z=5 => 30
print(lambda_b(2,3,4)) # x=2, y=3, z=4 => 24

# 条件式付きlambda
lambda_c = lambda x, y: y if x < y else x # if(x<y) => y, else x
print(lambda_c(2, 4))



lambda_x = lambda x,y,z=5: x*y*z if x > 5 else x+y
print('res:',lambda_x(5,20))