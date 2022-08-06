# __name__ の主な使い方は __main__ と組み合わせて、コマンドラインから直接呼ばれたかを判定することです。Python のプログラムがコマンドラインから直接呼ばれた場合、 __name__ には __main__ という文字列が格納されます。なお、importで他のプログラムから呼ばれた場合、ファイル名が格納されます。 https://tinyurl.com/2alampw6

def print_name():
    print(__name__)

if __name__ == '__main__':
    print_name()