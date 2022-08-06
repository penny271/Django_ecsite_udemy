# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val' # クラス変数

    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数

    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA() # インスタンス化
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()
#* <クラス変数>
#* • オブジェクト同士で共有することができる変数 • メソッドの内部でなく、クラスの直下に記載
#! クラス変数はオブジェクト同士で共有しているので、一つのオブジェクトがクラス変数を変更すると、すべてのオブジェクトに適用されるため、基本、書き換えてはいけない
#- クラス変数にアクセスするには クラス名.クラス変数名
#- インスタンス名.__class__.クラス変数名
print(SampleA.class_val)
print(instance_a.__class__.class_val) # クラス変数
instance_b = SampleA() #インスタンス化
instance_b.set_val()
instance_b.print_val()
instance_a.__class__.class_val = 'class val 2' #! 値の書き換え
instance_b.print_val()

print('*'*100)
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))
print(id(instance_a))
print(id(instance_b))
