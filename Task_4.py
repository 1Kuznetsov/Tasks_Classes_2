import re


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

        if RomanNumber.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ERROR')

    def decimal_number(self):
        """
        Method converting the roman number to decimal
        :return: decimal number
        """

        if self.rom_value is not None:
            dec = 0
            rom_num = self.rom_value
            for dc, rm in RomanNumber.roman_digits:
                while rom_num.startswith(rm):
                    dec += dc
                    rom_num = rom_num[len(rm):]

            return dec


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

    def __repr__(self):
        """
        represents data
        :return:
        """

        return str(self.rom_value)
