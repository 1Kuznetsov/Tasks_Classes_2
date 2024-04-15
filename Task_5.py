import re


def to_dec(val):
    """
    Method converting the roman number to decimal
    :return: decimal number
    """

    if val is None:
        return None

    dec = 0
    rom_num = val
    for dc, rm in RomanNumber.roman_digits:
        while rom_num.startswith(rm):
            dec += dc
            rom_num = rom_num[len(rm):]
    return dec


def to_rom(val):
    """
    Method converting the decimal number to roman
    :return: roman number
    """

    if val is None:
        return None

    rom = ''
    try:
        int_num = int(val)

    except ValueError:
        return None

    while int_num > 0:
        for dc, rm in RomanNumber.roman_digits:
            while int_num >= dc:
                int_num -= dc
                rom += rm
    return rom


class RomanNumber:
    """
    Class representing the roman number system
    """

    roman_digits = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                    (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'),
                    (5, 'V'), (4, 'IV'), (1, 'I')]

    def __init__(self, number):
        """
        Sets all the necessary attributes for the class User
        :param number: number written in string or int format
        """

        if self.is_int(number):
            self.int_value = number

            if to_rom(number) is not None:
                self.rom_value = to_rom(number)
            else:
                self.rom_value = None
                print('ERROR')

        elif self.is_roman(number):
            self.rom_value = number

            if to_dec(number) is not None:
                self.int_value = to_dec(number)

            else:
                self.int_value = None
                print('ERROR')

        else:
            self.rom_value = None
            self.int_value = None

    def decimal_number(self):
        """
        Method converting the roman number to decimal
        :return: decimal number
        """

        if self.rom_value is None:
            return None

        dec = 0
        rom_num = self.rom_value
        for dc, rm in RomanNumber.roman_digits:
            while rom_num.startswith(rm):
                dec += dc
                rom_num = rom_num[len(rm):]
        self.int_value = dec
        return dec

    def roman_number(self):
        """
        Method converting the decimal number to roman
        :return: roman number
        """

        if self.int_value is None:
            return None

        rom = ''
        int_num = self.int_value

        while int_num > 0:
            for dc, rm in RomanNumber.roman_digits:
                while int_num >= dc:
                    int_num -= dc
                    rom += rm

        self.rom_value = rom
        return rom

    @staticmethod
    def is_roman(value):
        """
        Method of checking if the value is roman number
        :param value: num
        :return: True if value is roman and False otherwise
        """

        pattern = re.compile('''^(M{0,3})(D?C{0,3}|C[DM])(L?X{0,3}|X[LC])(V?I{0,3}|I[VX])$''''')
        if re.match(pattern, value):
            return True
        return False

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

    def __repr__(self):
        """
        represents data
        :return:
        """

        if self.rom_value is None and self.int_value is None:
            return 'ERROR'

        if self.rom_value is not None:
            return str(self.rom_value)

        if self.int_value is not None:
            return str(self.int_value)
