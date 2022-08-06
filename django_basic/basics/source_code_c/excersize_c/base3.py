# じゃんけん 勝った場合はループの外、負けた場合3回でループの外、あいこはあいこと表示

from logging.handlers import MemoryHandler


def generator():
    while True:
        yield '1'
        yield '2'
        yield '3'

hands = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー',
}

gen = generator()

lose_count = 0

def is_win(your_hand, enemy_hand):
    if your_hand == '1' and enemy_hand == '2':
        return True
    elif your_hand == '2' and enemy_hand == '3':
        return True
    elif your_hand == '3' and enemy_hand == '1':
        return True
    else:
        return False



while True:
    your_hand = input('1: グー,2: チョキ,3: パー')
    print(your_hand)
    # if (your_hand != '1') and (your_hand != '2') and (your_hand != '3'):
    if your_hand not in ('1' , '2' , '3'): #- この書き方が一番ラク!!
        print('再入力してください')
        continue
    enemy_hand = next(gen)
    if your_hand == '1' and enemy_hand == '2' or your_hand == '2' and enemy_hand == '3' or your_hand == '3' and enemy_hand == '1':
        print(f'your_hand:{hands[your_hand]}, enemy_hand:{hands[enemy_hand]}')
        print('あなたは勝ちました')
        break
    elif your_hand == '2' and enemy_hand == '1' or your_hand == '3' and enemy_hand == '2' or your_hand == '1' and enemy_hand == '3':
        lose_count += 1
        print(f'your_hand:{hands[your_hand]}, enemy_hand:{hands[enemy_hand]}')
        if lose_count == 3:
            print('あなたは負けました')
            break
        else:
            print('あなたの負け、再チャレンジ')
    # elif your_hand ==  enemy_hand:
    #     print('あいこ')
    else:
        print('あいこ')

