"""
life_path_number.py - a useful tool to calculate life path number and lucky
colour from a birthday

Written by : Ben Niu
Student ID : 21678145

Versions:
    - initial version by Ben Niu 20/05/24
"""


import sys
import common


def calc_life_path_number(day, month, year):
    '''
    Calculate life path number.
    '''
    num_d = add_digists(day)
    num_m = add_digists(month)
    num_y = add_digists(year)
    num_old = add_digists(num_d + num_m + num_y)
    lp_number = add_digists(num_old)
    while lp_number != num_old:
        num_old = lp_number
        lp_number = add_digists(lp_number)
    return lp_number


def add_digists(number):
    '''
    Calculate single digist from a number.
    '''
    if is_master_number(number):
        return number
    single_digist = 0
    while number > 0:
        digit = number % 10
        single_digist += digit
        number = number // 10
    if single_digist >= 10:
        return add_digists(single_digist)
    return single_digist


def is_master_number(number):
    '''
    Check the number is a master number or not.
    '''
    master_nums = [11, 22, 33]
    return number in master_nums


def get_lucky_colour(number):
    '''
    Get lucky colour from the life path number.
    '''
    master_lucky_colours = ["Silver", "White", "Crimson"]
    lucky_colours = ["Red", "Orange", "Yellow", "Green", "Sky Blue",
                     "Indigo", "Violet", "Magenta", "Gold"]
    lucky_colour = None
    if is_master_number(number):
        lucky_colour = master_lucky_colours[int(number / 11) - 1]
    else:
        if number >= 1 and number <= len(lucky_colours):
            lucky_colour = lucky_colours[number - 1]
    return lucky_colour


def main(input_file=None, output_file=None):
    '''
    Main function of life path number calculator.
    Specify input_file and output_file to read from/write to files.
    If want input through console, leave parameters as None.
    '''
    birthday_str = None
    result = False
    interact_file = input_file is not None and output_file is not None
    if interact_file:
        birthday_str = common.get_birthday_from_file(input_file)
    else:
        birthday_str = common.get_birthday_from_input()
    birthdays = common.convert_birthdays(birthday_str)
    lp_numbers = []
    for birthday in birthdays[:2]:
        lp_number = calc_life_path_number(birthday[0],
                                          birthday[1], birthday[2])
        lp_numbers.append(lp_number)
    for index, lp_number in enumerate(lp_numbers):
        if interact_file:
            if common.write_output_to_file(
                "%d/%d/%d: life path number=%d, lucky colour=%s, "
                "master number?=%s"
                % (
                    birthdays[index][0],
                    birthdays[index][1],
                    birthdays[index][2],
                    lp_number,
                    get_lucky_colour(lp_number),
                    is_master_number(lp_number),
                ), output_file
            ):
                result = True
        else:
            common.write_output_to_console(
                "%d/%d/%d: life path number=%d, lucky colour=%s, "
                "master number?=%s"
                % (
                    birthdays[index][0],
                    birthdays[index][1],
                    birthdays[index][2],
                    lp_number,
                    get_lucky_colour(lp_number),
                    is_master_number(lp_number),
                )
            )
            result = True
    if len(lp_numbers) >= 2:
        is_same_number = lp_numbers[0] == lp_numbers[1]
        if interact_file:
            common.write_output_to_file(
                "life path numbers are same?=%s" % is_same_number, output_file)
        else:
            common.write_output_to_console(
                "life path numbers are same?=%s" % is_same_number)
    return result


if __name__ == '__main__':
    result = False
    if len(sys.argv) == 1:
        result = main()
    elif len(sys.argv) == 3:
        result = main(sys.argv[1], sys.argv[2])
    if not result:
        print("Usage: %s [INPUT_FILE OUTPUT_FILE]" % __file__)
