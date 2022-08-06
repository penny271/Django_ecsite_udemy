# try except

try:
    b = [10,20,30]
    a = b[4]
    c = b.method_a()
    a = 10 / 0
except ZeroDivisionError as e:
    #- ★★new エラーの詳細、発生行数なども表示させられる - 20220628
    import traceback
    traceback.print_exc()
    # print(e, type(e))
    pass
# except IndexError as e:
    # print('indexerror発生')
except Exception as e:
    print('Exception: ', e, type(e))
# else:
#     print('Else処理')
# finally:
#     print('Finally処理')

# print('処理が完了しました。')