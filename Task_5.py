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


if __name__ == '__main__':
    num = RomanNumber('MMXXIV')
    print(num.is_roman(num.rom_value))
    res = num.decimal_number()
    print(res)
    num_2 = RomanNumber(2024)
    print(num_2.roman_number())
