class NavalBattle:
    """
    Class representing the naval battle game
    """

    playing_field = []

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
            ptr = ''
            for cell in row:
                if cell != 1 and cell != 0:
                    ptr += cell
                else:
                    ptr += '~'
            print(ptr)

    def shot(self, y, x):
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
