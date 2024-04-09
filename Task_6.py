class RomanNumber:
    """
    Class representing the roman number system
    """

    roman_digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                    (5, 'V'), (4, 'IV'), (1, 'I')]

    def __init__(self, rom_value):
        """
        Sets all the necessary attributes for the class User
        :param rom_value: number written in string or int format
        """

        if self.is_int(rom_value):
            self.int_value = rom_value
        elif not self.is_roman(rom_value):
            self.int_value = None
            print('ERROR')

        elif self.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ERROR')

    def decimal_number(self):
        """
        Method converting the roman number to decimal
        :return: decimal number
        """

        if self.rom_value is None:
            return None

        dec = 0
        for dc, rm in RomanNumber.roman_digits:
            while self.rom_value.startswith(rm):
                dec += dc
                self.rom_value = self.rom_value[len(rm):]

        return dec

    def roman_number(self):
        """
        Method converting the decimal number to roman
        :return: roman number
        """

        if self.int_value is None:
            return None

        rom = ''
        while self.int_value > 0:
            for dc, rm in RomanNumber.roman_digits:
                while self.int_value >= dc:
                    self.int_value -= dc
                    rom += rm

        return rom

    @staticmethod
    def is_roman(value):
        """
        Method of checking if the value is roman number
        :param value: num
        :return: True if value is roman and False otherwise
        """

        if value is None:
            return False

        valid_symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        for sym in str(value):
            if sym not in valid_symbols:
                return False

        return True

    @staticmethod
    def is_int(value):
        """
        Method of checking if the value is decimal number
        :param value: num
        :return: True if value is decimal and False otherwise
        """

        if value is None:
            return False

        valid_symbols = [str(x) for x in range(0, 10)]

        for sym in str(value):
            if sym not in valid_symbols:
                return False

        return True

    @staticmethod
    def make_nums(x, y):
        """
        Method checking that numbers can be converted into int type
        :param x: first num
        :param y: second num
        :return: integer x and y
        """

        if not RomanNumber.is_int(x):
            if not RomanNumber.is_roman(x):
                print('ERROR')
                x, y = None, None
                return x, y
            x = x.decimal_number()

        if not RomanNumber.is_int(y):
            if not RomanNumber.is_roman(y):
                print('ERROR')
                x, y = None, None
                return x, y
            y = y.decimal_number()

        return x, y

    @staticmethod
    def addition(x, y):
        """
        Method of addition two numbers
        :param x: first number
        :param y: second number
        :return: result in roman number system
        """
        x, y = RomanNumber.make_nums(x, y)
        if x is None or y is None:
            print('ERROR')
        else:
            result = RomanNumber(x + y)
            return RomanNumber.roman_number(result)

    @staticmethod
    def subtraction(x, y):
        """
        Method of subtraction two numbers
        :param x: first number
        :param y: second number
        :return: result in roman number system
        """

        x, y = RomanNumber.make_nums(x, y)
        if x is None or y is None:
            print('ERROR')
        else:
            if x > y:
                result = RomanNumber(x - y)
                return RomanNumber.roman_number(result)
            else:
                result = RomanNumber(y - x)
                return '-' + RomanNumber.roman_number(result)

    @staticmethod
    def multiplication(x, y):
        """
        Method of multiplication two numbers
        :param x: first number
        :param y: second number
        :return: result in roman number system
        """

        x, y = RomanNumber.make_nums(x, y)
        if x is None or y is None:
            print('ERROR')
        else:
            result = RomanNumber(x * y)
            return RomanNumber.roman_number(result)

    @staticmethod
    def division(x, y):
        """
        Method of division two numbers
        :param x: first number
        :param y: second number
        :return: result in roman number system
        """

        x, y = RomanNumber.make_nums(x, y)
        if x is None or y is None:
            print('ERROR')
        else:
            if y != 0 and x % y == 0:
                result = RomanNumber(int(x / y))
                return RomanNumber.roman_number(result)
            return 'ERROR'


if __name__ == '__main__':
    num = RomanNumber('MMXXIV')
    print(num.is_roman(num.rom_value))
    res = num.decimal_number()
    print(res)
    num_2 = RomanNumber(2024)
    print(num_2.roman_number())
    r = RomanNumber.addition(10, 5)
    q = RomanNumber.subtraction(29, 32)
    p = RomanNumber.multiplication(5, 30)
    t = RomanNumber.division(10, 2)
    print(r, q, p, t)
