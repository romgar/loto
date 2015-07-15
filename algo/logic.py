from copy import copy
import random


def generate_number(already_used_numbers, min_range=0, max_range=1):
    number = None

    if len(already_used_numbers) == (len(range(min_range, max_range)) + 1):
        raise Exception('Not possible !')
    not_found = True
    while not_found:
        random_number = random.randrange(min_range, max_range)
        if random_number not in already_used_numbers:
            number = random_number
            not_found = False

    return number


class LotoGrid(object):

    def __init__(self, max_number=90):
        self.lists = []
        self.max_number = max_number
        for i in range(max_number/10):
            self.lists.append(list3(unit=i))

    def get_list_for_unit(self, unit_number):
        return self.lists[unit_number]

    def generate_numbers(self, number_of_numbers=15):
        already_used_numbers = []

        for i in range(9):
            print 'Generation between', i*10, 'and', (i+1)*10 - 1
            self.find_free_number(already_used_numbers, min_range=i*10, max_range=(i+1)*10 - 1)

        for i in range(number_of_numbers-9):
            print 'Generation between', 1, 'and', 90
            self.find_free_number(already_used_numbers, min_range=1, max_range=90)

    def find_free_number(self, already_used_numbers, min_range=None, max_range=None):
        if not min_range:
            min_range = 1
        if not max_range:
            max_range = self.max_number - 1
        import pdb; pdb.set_trace()
        random_number = random.randrange(min_range, max_range)
        for ind, lst in enumerate(self.lists):
            print 'List ', str(ind), ' - ', lst

        print 'Round number:', random_number
        print 'Already used:', already_used_numbers

        if random_number in already_used_numbers:
            self.find_free_number(already_used_numbers)
        else:
            try:
                unit = random_number / 10
                unit_list = self.get_list_for_unit(unit)
                unit_list.append(random_number)
            except ValueError:
                print 'ValueError'
                self.find_free_number(already_used_numbers)
            else:
                already_used_numbers.append(random_number)

    def get_grid(self):
        grid = []
        for list in self.lists:
            grid += list.elements
        return grid


class list3(object):

    def __init__(self, unit=0):
        self.elements = []
        self.unit = unit

    def append(self, element):
        if len(self.elements) > 2:
            raise ValueError('Cannot have more than 3 values')
        else:
            self.elements.append(element)

    def __str__(self):
        return str(self.elements)

if __name__ == '__main__':

    grid = LotoGrid()
    grid.generate_numbers()
    print grid.get_grid()
