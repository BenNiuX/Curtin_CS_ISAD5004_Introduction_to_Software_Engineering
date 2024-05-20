"""
generation.py - a useful tool to calculate generation from a birthday

Written by : Ben Niu
Student ID : 21678145

Versions:
    - initial version by Ben Niu 20/05/24
"""


import sys
import common


def get_generation(year):
    generations_info = [
        (1901, 1945, "Silent Generation"),
        (1946, 1964, "Baby Boomers"),
        (1965, 1979, "Generation X"),
        (1980, 1994, "Millennials"),
        (1995, 2009, "Generation Z"),
        (2010, 2024, "Generation Alpha")
    ]
    for generation_info in generations_info:
        if year >= generation_info[0] and year <= generation_info[1]:
            return generation_info[2]
    return None


def main(input_file=None, output_file=None):
    birthday_str = None
    result = False
    if input_file is not None and output_file is not None:
        birthday_str = common.get_birthday_from_file(input_file)
    else:
        birthday_str = common.get_birthday_from_input()
    birthdays = common.convert_birthdays(birthday_str)
    if len(birthdays) >= 1:
        year = birthdays[0][2]
        generation = get_generation(year)
        if input_file is not None and output_file is not None:
            if common.write_output_to_file(
                    "Generation for %d: %s" % (year, generation), output_file):
                result = True
        else:
            common.write_output_to_console(
                "Generation for %d: %s" % (year, generation))
            result = True
    return result


if __name__ == '__main__':
    result = False
    if len(sys.argv) == 1:
        result = main()
    elif len(sys.argv) == 3:
        result = main(sys.argv[1], sys.argv[2])
    if not result:
        print("Usage: %s [INPUT_FILE OUTPUT_FILE]" % __file__)
