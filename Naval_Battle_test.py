from Task_3 import NavalBattle
from Task_3 import is_valid

player1 = NavalBattle('x')
player2 = NavalBattle('$')

player1.playing_field[0][0] = '0'
player1.playing_field[0][1] = '1'
player2.playing_field[1][0] = '1'
player2.playing_field[1][1] = '1'

player1.shot(1, 1)
NavalBattle.show()
player2.shot(2, 2)
NavalBattle.show()
player1.new_game()
count = 0
NavalBattle.show()

while count < 20:
    player_num = int(input())
    x, y = map(int, input().split())

    if is_valid(x, y):
        if player_num == 1:
            if player1.shot(x, y):
                count += 1
        if player_num == 2:
            if player2.shot(x, y):
                count += 1

    NavalBattle.show()
    print(count)

else:
    print('WIN')
