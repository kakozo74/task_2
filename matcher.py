import re

brackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def check_brackets(input_str: str, brackets_types: list):

    inner_brackets = {}
    for bracket in brackets_types:
        inner_brackets[brackets[bracket]] = bracket
    not_closed_brakets = []
    not_closed_brakets_str_index = []
    result = [True, None, None]
    for i, symbol in enumerate(input_str):
        if symbol in inner_brackets.keys():
            if inner_brackets[symbol] not in not_closed_brakets:  # скобка без открывающей
                result[0] = False
                result[1] = (symbol, i)
                result[2] = (symbol, i)
                return result
            else:
                if inner_brackets[symbol] != not_closed_brakets[-1]:
                    result[0] = False
                    result[1] = (symbol, i)
                    result[2] = (not_closed_brakets[-1], not_closed_brakets_str_index[-1])
                    return result
                else:
                    not_closed_brakets = not_closed_brakets[::-1]
                    not_closed_brakets.remove(inner_brackets[symbol])
                    not_closed_brakets = not_closed_brakets[::-1]
        if symbol in brackets_types:
            not_closed_brakets.append(symbol)
            not_closed_brakets_str_index.append(i)
    if not_closed_brakets:
        result[0] = False
        for i in range(len(input_str) - 1, 0, -1):
            print(i)
            if input_str[i] in ('(', ')', '{', '}', '[', ']', '<', '>'):
                result[1] = (input_str[i], i)
                break
        result[2] = (not_closed_brakets[0], not_closed_brakets_str_index[0])
    return result


input_str = input('Введите строку: ')
while True:
    input_brackets = input('Введите скобки ')
    brackets_list = re.findall(r'[\(\[\{\<]', input_brackets)
    if not brackets_list:
        print('Не введено скобок')
        continue
    break
res = check_brackets(input_str, brackets_list)
print(str(res)[1:-1])