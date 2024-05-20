"""
common.py - provide common functions handling input/output and date

Written by : Ben Niu
Student ID : 21678145

Versions:
    - initial version by Ben Niu 20/05/24
"""


def get_birthday_from_input():
    birthday_str = input("Enter birthday (DD MM YYYY): ")
    return birthday_str


def get_birthday_from_file(file_name):
    try:
        with open(file_name) as in_file:
            birthday_str = in_file.readline().strip()
    except OSError:
        birthday_str = ""
    return birthday_str


def write_output_to_console(output):
    print(output)


def write_output_to_file(output, file_name):
    result = True
    try:
        with open(file_name, "w") as out_file:
            out_file.write(output)
    except OSError:
        result = False
    return result


def convert_birthdays(birthdays_str):
    result = []
    if birthdays_str:
        sub_strs = birthdays_str.split()
        if len(sub_strs) == 6 or len(sub_strs) == 3:
            for i in range(int(len(sub_strs)/3)):
                try:
                    result.append(
                        convert_birthday(
                            f"{sub_strs[i * 3]} {sub_strs[1 + i * 3]} "
                            f"{sub_strs[2 + i * 3]}"
                        )
                    )
                except ValueError:
                    pass
    return result


def convert_birthday(birthday_str):
    if birthday_str:
        sub_strs = birthday_str.split()
        if len(sub_strs) == 3:
            year = verify_year(int(sub_strs[2]))
            month = verify_month(convert_month_str(sub_strs[1]))
            day = verify_day(int(sub_strs[0]))
            if year != -1 and month != -1 and day != -1:
                return (day, month, year)
    raise ValueError("Birthday input error: %s" % birthday_str)


def verify_year(year):
    if year >= 1901 and year <= 2024:
        return year
    return -1


def verify_month(month):
    if month >= 1 and month <= 12:
        return month
    return -1


def verify_day(day):
    if day >= 1 and day <= 31:
        return day
    return -1


def convert_month_str(month_str):
    month_mmm = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                 "Aug", "Sept", "Oct", "Nov", "Dec"]
    month_mmmm = ["January", "February", "March", "April", "May",
                  "June", "July", "August", "September", "October",
                  "November", "December"]
    month = -1
    try:
        month = month_mmm.index(month_str) + 1
    except ValueError:
        try:
            month = month_mmmm.index(month_str) + 1
        except ValueError:
            try:
                month = int(month_str)
            except (TypeError, ValueError):
                pass
    return month
