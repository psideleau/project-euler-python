import unittest
from calculator import Calculator

class TestMultiples(unittest.TestCase):

    def test_multiples_of_3_and_5_up_to_10(self):
        c = Calculator(name='paul')
        multiples = c.multiples(upto=10)
        self.assertEqual([3, 5, 6, 9], multiples)

    def test_fibonannci10(self):
        c = Calculator(name='paul')
        self.assertEqual(0, c.fibonnaci(0))
        self.assertEqual(1, c.fibonnaci(1))
        self.assertEqual(1, c.fibonnaci(2))
        self.assertEqual(2, c.fibonnaci(3))
        self.assertEqual(3, c.fibonnaci(4))
        self.assertEqual(5, c.fibonnaci(5))
        self.assertEqual(55, c.fibonnaci(10))

        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], c.fib_seq(10))


    def test_sum_of_multiples(self):
        c = Calculator(name='paul')
        multiples = c.multiples(upto=10)
        self.assertEqual(23, c.sum(multiples))
        print(c.sum(c.multiples(1000)))


# download python, pycharm, pip3 install Django
#Collecting Django
#django-admin startproject finance
#python manage.py startapp polls

if __name__ == '__main__':
    unittest.main()
