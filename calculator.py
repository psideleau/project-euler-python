import functools
class Calculator:
    def __init__(self, name):
        self.name = name

    def add(self, x, y):
        return x + y

    def multiples(self, upto):
        find_multiple = lambda x: (x % 3 == 0) or (x % 5 == 0)
        natural_numbers = (range(1, upto))
        return list(filter(find_multiple, natural_numbers))

    def sum(self, multiples):
        return functools.reduce(lambda x, y: x + y, multiples)

    def fibonnaci(self, amount):
        return self.f(amount)

    def fib_seq(self, amount):
        return list(map(self.fibonnaci, range(0, amount + 1)))



    def f(self, amount):
        if amount == 1:
            return 1
        elif amount == 0:
            return 0

        n = self.f(amount - 1) + self.f(amount - 2)
        return n