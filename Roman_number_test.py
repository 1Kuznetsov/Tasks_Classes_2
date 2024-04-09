from Task_6 import RomanNumber

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
