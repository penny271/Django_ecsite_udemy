class Person:
    """人 クラス"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_introduce(self):
        print(f"私の名前は{self.name}、{self.age}才です。")


class SoccerPlayer(Person):
    """サッカー選手 クラス"""

    # def __init__(self, name, age, is_daihyo):
    #     # 親クラスの__init__を呼び出す。
    #     super().__init__(name, age)
    #     # is_daihyo属性はSoccerPlayerクラス固有の属性なのでここで値設定する
    #     self.is_daihyo = is_daihyo
    def __init__(self, name, age, is_daihyo):


    self.is_daihyo = is_daihyo

    def self_introduce(self):
        super().self_introduce()
        print(f"サッカー選手をやっています。")
        # 追加
        if self.is_daihyo:
            print("日本代表選手です。")

    def kick(self):
        print("キック!")

s1 = SoccerPlayer("本田", 20, True)

s1.self_introduce()