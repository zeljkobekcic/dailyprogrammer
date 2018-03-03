def parse_cards_from_string(string):
    between_delimiters = retrieve_between_squared_brackets(string)
    elements_between_delimiters = between_delimiters.split(',')
    trimmed_elements = [element.strip() for element in elements_between_delimiters]
    parsed = split_groups(trimmed_elements)
    return parsed

def retrieve_between_squared_brackets(string):
    return string.split('[')[1].split(']')[0]

def split_groups(list_of_groups):
    split = lambda x: x.split('/')
    return list(map(split, list_of_groups))

def parse_wanted_object_from_string(string):
    last_whitespace = string.rfind(' ')
    last_questionmark = string.rfind('?')
    return string[last_whitespace : last_questionmark].strip()

input = open('352_seven_wonders.input', 'r').read()



def cards_which_can_make(cards, resource):
    filtered_cards = []
    contains = lambda x: resource in x
    filterd = list(filter(contains, cards))
    return filterd


def bruteforce_seven_wonders(cards, output, accumulator):

    if output == "":
        return accumulator

    current_resource = output[0]
    remaining_resources = output[1:]

    useable_cards = cards_which_can_make(cards, current_resource)

    for card in useable_cards:
        tmp = cards[:]
        tmp.remove(card)
        cur_accumulator = accumulator[:]
        cur_accumulator.append((card, current_resource))
        output = bruteforce_seven_wonders(tmp, remaining_resources, cur_accumulator)

        if output != None:
            return output

    return None
