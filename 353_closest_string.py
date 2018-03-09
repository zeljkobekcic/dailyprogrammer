
def hamming_distance(first_string, second_string):
    paired_list = zip(first_string, second_string)
    return len(list(filter(lambda x: x[0] != x[1], paired_list)))


def apply_string_metric(metric, string, list_of_strings):
    return list(map(lambda x: metric(string, x), list_of_strings))

def map_string_metric(metric, list_of_strings):

    accumulator = []
    for element in list_of_strings:
        tmp = list_of_strings[:]
        tmp.remove(element)
        accumulator.append(min(apply_string_metric(metric, element, tmp)))

    return accumulator

def read_file(file_name):
    file_content = open(file_name).read()
    lines = file_content.splitlines()
    return int(lines[0]), lines[1:]

if __name__ == "__main__":
    value, content = read_file('353_closest_string.input')
    values = map_string_metric(hamming_distance, content)
    position = values.index(min(values))
    print(min(values))
    print(content[position])
