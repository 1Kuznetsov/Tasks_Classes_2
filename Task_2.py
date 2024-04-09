class NavalBattle:
    """
    Class representing the naval battle game
    """

    playing_field = [[0]*10 for _ in range(10)]

    def __init__(self, player_sym):
        """
        Sets all the necessary attributes for the class User
        :param player_sym: symbol of player turn
        """

        self.player_sym = player_sym

    @staticmethod
    def show():
        """
        Method of showing the current battlefield
        :return: current state of battle
        """

        for row in NavalBattle.playing_field:
            print(' '.join([cell if cell != 1 and cell != 0 else '~' for cell in row]))

    def shot(self, x, y):
        """
        Method of making a turn
        :param x: coordinate of x-axis
        :param y: coordinate of y-axis
        :return: result of making a turn
        """

        if NavalBattle.playing_field[x-1][y-1] == 1:
            NavalBattle.playing_field[x-1][y-1] = self.player_sym
            print('Got')

        else:
            NavalBattle.playing_field[x-1][y-1] = 'o'
            print('Away')


if __name__ == '__main__':
    player1 = NavalBattle('x')
    player2 = NavalBattle('$')

    player1.playing_field[0][0] = 0
    player1.playing_field[0][1] = 1
    player2.playing_field[1][0] = 1
    player2.playing_field[1][1] = 1

    player1.shot(1, 1)
    NavalBattle.show()
    player2.shot(2, 2)
