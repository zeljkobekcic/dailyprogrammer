from functools import reduce
from sys import argv


class permutation_madness:

    def __init__(self, original_list, current_list):
        self.original_list = original_list 
        self.current_list = current_list

    def spin(self, position):
        spinner_index = len(self.current_list) - position
        result_list = self.current_list[spinner_index : ] + self.current_list[0 : spinner_index]
        return permutation_madness(self.original_list, result_list)
    
    def exchange(self, position1, position2):
        result_list = self.current_list[:]
        result_list[position1] = self.current_list[position2]
        result_list[position2] = self.current_list[position1]
        return permutation_madness(self.original_list, result_list)
    
    def partner(self, position1, position2):

        element_at_position1 = self.original_list[position1]
        element_at_position2 = self.original_list[position2]

        current_position1 = self.current_list.index(element_at_position1)
        current_position2 = self.current_list.index(element_at_position2)

        return self.exchange(current_position1, current_position2)


def parse_elements(task):
    task_name = task[0]
    task_elements = task[1:].split('/')
    task_elements = list(map(int, task_elements))
    return task_name, task_elements

def parse_to_list(string):
    elements = string.split(',')
    return list(map(parse_elements, elements))

def apply_argument(perm, task):
    if task[0] == 's':
        return perm.spin(task[1][0])
    elif task[0] == 'x':
        return perm.exchange(task[1][0], task[1][1])
    elif task[0] == 'p':
        return perm.partner(task[1][0], task[1][1])


if __name__ == "__main__":
    input_file = open('input.txt', 'r')
    
    start = list(input_file.readline())[:-1]
    program = parse_to_list(input_file.readline())

    start_permutation = permutation_madness(start, start)
    result_permutation = reduce(apply_argument, program, start_permutation)

    print(''.join(result_permutation.current_list))
    
