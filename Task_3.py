import random


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

        if not NavalBattle.playing_field:
            print('Battlefield is not filled')

        elif NavalBattle.playing_field[x-1][y-1] != 1 and NavalBattle.playing_field[x-1][y-1] != 0:
            print('ERROR')

        elif NavalBattle.playing_field[x-1][y-1] == 1:
            NavalBattle.playing_field[x-1][y-1] = self.player_sym
            print('Got')

        else:
            NavalBattle.playing_field[x-1][y-1] = 'o'
            print('Away')

    @staticmethod
    def is_valid(i, j):
        """
        Function of checking if the coordinate is appropriate
        :param i: first coordinate
        :param j: second coordinate
        :return: True if appropriate and False otherwise
        """

        return 0 <= i < 10 and 0 <= j < 10

    @staticmethod
    def availability(field, x, y, size, is_horizontal):
        """
        Function of checking available places for placing ship
        :param field:
        :param x: x-axis coordinate
        :param y: y-axis coordinate
        :param size: size of ship
        :param is_horizontal: position in space
        :return: True if place is available and False otherwise
        """

        offsets = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for i in range(size):
            if not NavalBattle.is_valid(x, y) or field[x][y] != 0:
                return False

            for dx, dy in offsets:
                if NavalBattle.is_valid(x + dx, y + dy) and field[x + dx][y + dy] != 0:
                    return False

            if is_horizontal:
                y += 1

            else:
                x += 1
        return True

    @staticmethod
    def place_ship(field, x, y, size, is_horizont):
        """
        Function of placing the ship on the battlefield
        :param field: field with positions of ships
        :param x: x-axis coordinate
        :param y: y-axis coordinate
        :param size: size of ship
        :param is_horizont: position in space
        :return: None
        """

        if is_horizont:
            for i in range(size):
                field[x][y + i] = 1

        else:
            for i in range(size):
                field[x + i][y] = 1

    @staticmethod
    def new_game():
        """
        Method creating the initial ships arrangement
        :return: Generated battlefield
        """

        NavalBattle.playing_field = [[0 for _ in range(10)] for _ in range(10)]

        ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        for size in ship_sizes:
            while True:
                x = random.randint(0, 10 - size)
                y = random.randint(0, 10 - size)
                is_horizont = random.randint(0, 1)

                if NavalBattle.availability(NavalBattle.playing_field, x, y, size, is_horizont):
                    NavalBattle.place_ship(NavalBattle.playing_field, x, y, size, is_horizont)
                    break
