class Person:
    """人 クラス"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_introduce(self):
        print(f"私の名前は{self.name}、{self.age}才です。")


class SoccerPlayer(Person):
    """サッカー選手 クラス"""

    def self_introduce(self):
        # 親クラスのメソッドを呼び出す
        super().self_introduce()
        print(f"サッカー選手をやっています。")

    def kick(self):
        print("キック!")

s1 = SoccerPlayer("本田", 20)
s1.self_introduce()
