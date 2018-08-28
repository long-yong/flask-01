#!/usr/bin/python3
# coding=utf-8

# source codes or import from package
def reverseList(list):
    L = len(list)
    for i in range(int(L/2)):
        list[i], list[L-1-i] = list[L-1-i], list[i]
    return list

def isPalindrome(str):
    L = len(str)
    for i in range(int(L / 2)):
        if str[i] != str[L - 1 - i]:
            return False
    return True

def coins(num):
    quart = int(num/25)
    num -= quart*25
    dime = int(num/10)
    num -= dime*10
    nickel =int(num/5)
    num -= nickel*5
    penny = num
    return [quart, dime, nickel, penny]

def Factorial(num):
    if num == 0:
        return 0
    product = 1
    for i in range(1, num+1):
        product *= i
    return product

def Fib(N):
    if N == 1 or N == 2: return 1
    else: return Fib(N-1) + Fib(N-2)



import unittest

class reverseListTest(unittest.TestCase):
    def test01(self): return self.assertEqual    (reverseList([]), [])
    def test02(self): return self.assertEqual    (reverseList([1]), [1])
    def test03(self): return self.assertNotEqual (reverseList([1, 2]), [1, 2])
    def test04(self): return self.assertEqual    (reverseList([-1, -2]), [-2, -1])
    def test05(self): return self.assertNotEqual (reverseList([1, 2, 3]), [1, 2, 3])
    def test06(self): return self.assertEqual    (reverseList([1, 2, 3]), [3, 2, 1])
    def test07(self): return self.assertNotEqual (reverseList([1, 2, 3, 4]), [1, 2, 3, 4])
    def test08(self): return self.assertEqual    (reverseList([1, 2, 3, 4]), [4, 3, 2, 1])
    def test09(self): return self.assertEqual    (reverseList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    def test10(self): return self.assertEqual    (reverseList(['a', 'b', 'c']), ['c', 'b', 'a'])
    def setUp(self): print("reverseList-setup")
    def tearDown(self): print("reverseList-teardown")

class isPalindromeTest(unittest.TestCase):
    def test01(self): return self.assertEqual(isPalindrome('racecar'), True)
    def test02(self): return self.assertEqual(isPalindrome('rabbit'),  False)
    def test03(self): return self.assertEqual(isPalindrome('abcde'),   False)
    def test04(self): return self.assertEqual(isPalindrome('abcba'),   True)
    def test05(self): return self.assertEqual(isPalindrome('abcd'),    False)
    def test06(self): return self.assertEqual(isPalindrome('abba'),    True)
    def test07(self): return self.assertEqual(isPalindrome('123'),     False)
    def test08(self): return self.assertEqual(isPalindrome('121'),     True)
    def test09(self): return self.assertEqual(isPalindrome('12'),       False)
    def test10(self): return self.assertEqual(isPalindrome('11'),       True)
    def test11(self): return self.assertEqual(isPalindrome('a'),        True)
    def test12(self): return self.assertEqual(isPalindrome(''),         True)
    def setUp(self): print("isPalindrome-setup")
    def tearDown(self): print("isPalindrome-teardown")

class coinsTest(unittest.TestCase):
    def test01(self): return self.assertEqual   (coins(0),  [0, 0, 0, 0])
    def test02(self): return self.assertNotEqual(coins(1),  [0, 0, 0, 0])
    def test03(self): return self.assertEqual   (coins(41), [1, 1, 1, 1])
    def test04(self): return self.assertEqual   (coins(92), [3, 1, 1, 2])
    def test05(self): return self.assertEqual   (coins(87), [3, 1, 0, 2])
    def test06(self): return self.assertEqual   (coins(101),[4, 0, 0, 1])

class FactorialTest(unittest.TestCase):
    def test01(self): return self.assertEqual(Factorial(0), 0)
    def test02(self): return self.assertEqual(Factorial(1), 1)
    def test03(self): return self.assertEqual(Factorial(2), 2)
    def test04(self): return self.assertEqual(Factorial(3), 6)
    def test05(self): return self.assertEqual(Factorial(5), 120)
    def setUp(self): print("Factorial-setup")
    def tearDown(self): print("Factorial-teardown")

class FibTest(unittest.TestCase):
    def test01(self): return self.assertEqual(Fib(1), 1)
    def test02(self): return self.assertEqual(Fib(2), 1)
    def test03(self): return self.assertEqual(Fib(3), 2)
    def test04(self): return self.assertEqual(Fib(4), 3)
    def test05(self): return self.assertEqual(Fib(5), 5)
    def test06(self): return self.assertEqual(Fib(6), 8)
    def setUp(self): print("Fib-setup")
    def tearDown(self): print("Fib-teardown")

if __name__ == '__main__':
    unittest.main()
