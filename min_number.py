def min_number(num, k):
    '''
    Возвращает строкой минимальное число после удаления k цифр из строки num.
    '''
    if k >= len(num):
        return '0'
    lst = []

    for digit in num:
        while k > 0 and lst and lst[-1] > digit:
            lst.pop()
            k -= 1
        lst.append(digit)

    while k > 0:
        lst.pop()
        k -= 1

    return ''.join(lst).lstrip('0')


if __name__ == '__main__':
    import unittest

    class TestBetweenDays(unittest.TestCase):
        def test_digits_01(self):
            num = '1432219'
            k = 3
            call = min_number(num, k)
            result = '1219'
            self.assertEqual(call, result, 'Неправильный результат')

        def test_digits_02(self):
            num = '10200'
            k = 1
            call = min_number(num, k)
            result = '200'
            self.assertEqual(call, result, 'Неправильный результат')

    unittest.main()
