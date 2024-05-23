"""
common.py - provide common functions handling input/output and date

Written by : Ben Niu
Student ID : 21678145

Versions:
    - initial version by Ben Niu 20/05/24
"""


def get_birthday_from_input():
    '''
    Read 1 birthday string or 2 birthday strings (string)
    from keyboard as user input. Then it returns the string directly.
    '''
    birthday_str = input("Enter birthday (DD MM YYYY): ")
    return birthday_str


def get_birthday_from_file(file_name):
    '''
    Read a line which contains 1 birthday string or 2 birthday strings
    (string) from a text file. Then it returns the string directly.
    '''
    try:
        with open(file_name) as in_file:
            birthday_str = in_file.readline().strip()
    except OSError:
        birthday_str = ""
    return birthday_str


def write_output_to_console(output):
    '''
    Print the output string on the screen.
    '''
    print(output)


def write_output_to_file(output, file_name):
    '''
    Write the output string to a file with the name of file name.
    '''
    result = True
    try:
        with open(file_name, "w") as out_file:
            out_file.write(output)
    except OSError:
        result = False
    return result


def convert_birthdays(birthdays_str):
    '''
    Convert the input birthday strings to an array of (date, month, year).
    The max input available birthday is 2.
    '''
    result = []
    if birthdays_str:
        sub_strs = birthdays_str.split()
        if len(sub_strs) == 6 or len(sub_strs) == 3:
            for i in range(int(len(sub_strs) / 3)):
                try:
                    result.append(
                        convert_birthday(
                            f"{sub_strs[i * 3]} {sub_strs[1 + i * 3]} "
                            f"{sub_strs[2 + i * 3]}"
                        )
                    )
                except ValueError:
                    pass
    if len(result) == 0:
        print("Input error: %s" % birthdays_str)
    return result


def convert_birthday(birthday_str):
    '''
    Convert the input string to a integer tuple of (date, month, year).
    '''
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
    '''
    Verify the year and return a valid year integer value.
    The year must between 1901 and 2024, others return -1.
    '''
    if year >= 1901 and year <= 2024:
        return year
    return -1


def verify_month(month):
    '''
    Verify the month and return a valid month integer value.
    The month should between 1 and 12, others return -1.
    '''
    if month >= 1 and month <= 12:
        return month
    return -1


def verify_day(day):
    '''
    Verify the day and return a valid day integer value.
    The day should between 1 and 31, others return -1.
    Assumption: we assume every month has 31 days, do not consider
    30 days for April or 28/29 days for February.
    '''
    if day >= 1 and day <= 31:
        return day
    return -1


def convert_month_str(month_str):
    '''
    Convert the different type of month string to month (integer).
    Like convert "Jan" or "January" to 1.
    '''
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
