# デコレータ関数

def my_decorator(func):
    def wrapper(*args, **kwargs):
        # if args[0] == 1:
        #     return 1
        func(*args, **kwargs) #-func_a(1,2,apple='りんご')  や  func_b(2,2,3) が入る
        func(*args, **kwargs) #-func_a(1,2,apple='りんご')  や  func_b(2,2,3) が入る
        print('*' *100)
        func(*args, **kwargs) #-func_a(1,2,apple='りんご')  や  func_b(2,2,3) が入る
        print('*' *100)
    return wrapper

@my_decorator
def func_a(*args, **kwargs):
    print('func_aを実行')
    print('args: ',args,type(args))
    print('kwargs: ',kwargs.get('apple'))
    print('kwargs: ',kwargs.get('grape')) #! 存在しない場合、Noneを返す
    print('kwargs: ',kwargs['apple'])
    # print('kwargs: ',kwargs['grape']) #! エラーが出る 存在しないため

@my_decorator
def func_b(*args, **kwargs):
    print('func_bを実行')
    print('args: ',args,type(args))

func_a(1,2,apple='りんご')
func_b(2,2,3)

