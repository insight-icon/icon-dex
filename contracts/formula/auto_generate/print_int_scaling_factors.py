from contracts.formula.auto_generate.common.constants import MAX_PRECISION


FIXED_1 = 1 << MAX_PRECISION
FIXED_2 = 2 << MAX_PRECISION
MAX_NUM = 1 << (256-MAX_PRECISION)


maxLen = len(hex(max([FIXED_1, FIXED_2, MAX_NUM])))


print('    _FIXED_1 = {0:#0{1}x}'.format(FIXED_1, maxLen))
print('    _FIXED_2 = {0:#0{1}x}'.format(FIXED_2, maxLen))
print('    _MAX_NUM = {0:#0{1}x}'.format(MAX_NUM, maxLen))