# inner関数　ノンローカル変数
#- inner関数　ノンローカル変数

def outer():
    outer_value = '外側の変数'
    def inner():
        #- nonlocalouter_value #nonlocalと宣言することで、外側の関数の変数であるouter_valueを変更できるようになります。
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()

print('\n', '',  ,'\n')

#- nonlocalなし
def outer():
    outer_value = '外側の変数'
    def inner():
        # nonlocal outer_value
        outer_value = '内側の変数'
        print(f'inner: {outer_value=}','id={}'.format(id(outer_value)))
        print('aaa')
    inner()
    print('outer: outer_value = {}, id ={}'.format(outer_value, id(outer_value)))

outer()
