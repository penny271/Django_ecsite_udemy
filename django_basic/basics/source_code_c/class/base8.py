# メタクラス

class MetaException(Exception):
    pass

class Meta1(type): # type(デフォルトのメタクラス)

    #- 特殊メソッド __new__()はインスタンスを生成する
    def __new__(metacls, name, bases, class_dict):
        print('metacls = {}'.format(metacls))
        print('name = {}'.format(name))
        print('bases = {}'.format(bases)) # 継承しているクラスが入っている
        print('class_dict = {}'.format(class_dict))
        print('*'*100)
        # if 'my_var' not in class_dict.keys():
        #     raise MetaException('my_varを定義してください。')

        for base in bases: # 継承しているクラス
            #^ class SubClassA(ClassA): ClassAは Meta1 のインスタンス
            if isinstance(base, Meta1):
                raise MetaException('継承できません') # finalクラス

        #- 元のMetaクラスをsuper()で呼び出して、その処理をすることができる
        #- # typeクラスでクラスを生成する
        return super().__new__(metacls, name, bases, class_dict)

#- ClassAを作成した際に、(metaclass=Meta1)とmetaclassを指定しているので、
#- def __new__()が呼ばれ 内部のprint()が実行されている
# class ClassA(): #! 何も起きない
# class ClassA(Meta1): #! 何も起きない
#- class定義時に、継承と同じ形でmetaclass=メタクラス名とすると自身のメタクラスを指定できます
class ClassA(metaclass=Meta1): #^ ClassAは Meta1 のインスタンス
    a = '123'
    my_var = 'AAA'
    pass

class SubClassA(ClassA):
    pass
