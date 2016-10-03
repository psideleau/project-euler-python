import unittest
from calculator import Calculator

class TestExample(unittest.TestCase):

    def test_add(self):
        c = Calculator(name='paul')
        print(c.name)
        self.assertEqual(4, c.add(2,2))

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FA'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# download python, pycharm, pip3 install Django
#Collecting Django
#django-admin startproject finance
#python manage.py startapp polls

if __name__ == '__main__':
    unittest.main()