import sys
import math
import calendar
import datetime as dt


# 1

def exercise_twinkle():
    twinkle_string = "Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high," \
                     "\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
    return print(twinkle_string)


# 2

def exercise_python_version():
    print("Python version")
    return print(sys.version)


# 3

def exercise_date_time(date):
    date_formatted = date.strftime("%Y-%m-%d %H:%M:%S")
    return print(date_formatted)


# 4


def exercise_circle_area(r):
    if type(r) != int:
        raise TypeError('Please enter a number')

    if r <= 0:
        raise ValueError('The number should be positive')
    return math.pi * r ** 2


# 5

def exercise_reverse_name(name, last_name):
    if type(name) != str:
        raise TypeError('Name and Last name should be letters')
    if type(last_name) != str:
        raise TypeError('Name and Last name should be letters')

    full_name = name + " " + last_name
    return full_name[::-1]


# 6

def exercise_list_to_tuple(numbers_list):
    if type(numbers_list) != list:
        raise TypeError('Please enter a list')
    return tuple(numbers_list)


# 7

def exercise_file_ext(file_name):
    if type(file_name) != str:
        raise TypeError('Please enter valid file name')
    if '.' not in file_name:
        return 'Incorrect file name'

    file = file_name.split(".")
    return file[-1]


# 8

def exercise_colors(color_list):
    if type(color_list) != list:
        raise TypeError('Please enter a list of colors')
    elif not color_list:
        return 'There are no colors in a list'
    elif type(color_list[0]) != str or type(color_list[-1]) != str:
        return 'The list is not valid'
    else:
        return f"First color: {color_list[0]}\nLast color: {color_list[-1]}"


# 9

def exercise_exam_date(exam_st_date):
    if type(exam_st_date) != tuple:
        raise TypeError('Date format should be: (YYYY, MM, DD)')
    elif len(exam_st_date) > 3 or exam_st_date[1] > 12 or exam_st_date[2] > 31:
        return 'This date does not exist'
    else:
        return 'The examination will start from : %i / %i / %i' % exam_st_date


# 10

def exercise_triple_sum(num):
    if type(num) != int:
        raise TypeError('Please enter a number')
    double_num = num + num
    triple_num = num + num + num
    return num + double_num + triple_num


# 11

def exercise_abs_doc():
    return print(abs.__doc__)


# 12

def exercise_calendar(year, month):
    cal = calendar.month(year, month)
    return print(cal)


# 13

def exercise_multiline_string():
    return print("""
    a string that you "don't" have to escape
    This
    is a ....... multi-line
    heredoc string --------> example
    """)


# 14

def exercise_diff_days(date_1, date_2):
    if type(date_1) != dt.date or type(date_2) != dt.date:
        raise TypeError('Incorrect date, date format: (YYYY, MM, DD)')
    diff = date_2 - date_1
    return diff.days


# 15

def exercise_sphere_volume(r):
    if type(r) != int:
        raise TypeError('Please enter a number')
    elif r <= 0:
        raise ValueError('Input should be positive number')
    else:
        volume = (4/3)*math.pi * r ** 3
    return f"Sphere volume: {volume}"


# 16

def exercise_number_diff(n):
    if type(n) != int:
        raise TypeError('Please enter a number')
    number = abs(n - 17)
    if n > 17:
        return number * 2
    else:
        return number


# Is number a Narcissist

def number_narcissist(value):
    separate_list = [int(n) for n in value]
    base = len(value)
    sum_of_number = sum(num ** base for num in separate_list)

    if sum_of_number == int(value):
        return True
    else:
        return False


# Capitalize string

def to_cap_case(string):
    list_string = string.split()
    cap_list = [word.capitalize() for word in list_string]
    cap_string = " ".join(cap_list)
    return cap_string

# print(to_cap_case("How can mirrors be real if our eyes aren't real"))


# Counting vowels in string

vowels = ["a", "e", "i", "o", "u"]


def get_count(sentence):
    vowel_count = 0
    for letter in sentence:
        if letter in vowels:
            vowel_count += 1
    return vowel_count

# Moving zeros


def move_zeros(lst):
    for num in lst:
        if num == 0:
            lst.remove(num)
            lst.append(0)
    return lst
