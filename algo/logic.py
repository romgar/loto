
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

    def get_grid_with_display(self):
        grid = []
        for list in self.lists:
            grid.append(list.get_display_order())
        return grid

    def get_number_row_column(self, grid, row, column):
        number = None
        try:
            number = grid[column][row]
        except KeyError:
            number = None
        return number

    def export_for_display(self):
        grid = self.get_grid_with_display()

        matrix = []
        for row in range(0, 3):
            row_data = []
            for col in range(0, 9):
                row_data.append(self.get_number_row_column(grid, row, col))
            matrix.append(row_data)
        return matrix


class list3(object):

    def __init__(self, unit=0):
        self.elements = []
        self.unit = unit

    def append(self, element):
        if len(self.elements) > 2:
            raise ValueError('Cannot have more than 3 values')
        else:
            self.elements.append(element)

    def get_display_order(self):
        elements_and_display = {}
        display_used = []
        for element in self.elements:
            display = generate_number(display_used, 0, 3)
            display_used.append(display)
            elements_and_display[display] = element
        return elements_and_display


    def __str__(self):
        return str(self.elements)


if __name__ == '__main__':

    grid = LotoGrid()
    grid.generate_numbers()
    disp_grid = grid.get_grid_with_display()

    for row in range(0, 3):
        row_str = ''
        for col in range(0, 9):
            row_str += str(grid.get_number_row_column(disp_grid, row, col)).ljust(2) + ' '
        print row_str
        print '\n'
