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

        if self.is_roman(rom_value):
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
        for sym in value:
            if sym not in valid_symbols:
                return False

        return True


if __name__ == '__main__':
    num = RomanNumber('MMXXIV')
    print(num.is_roman(num.rom_value))
    res = num.decimal_number()
    print(res)

