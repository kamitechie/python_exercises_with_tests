import sys
import datetime as dt
import math
import calendar
import datetime


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
    full_name = name + " " + last_name
    return full_name[::-1]


# 6

def exercise_num_to_tuple(numbers_list):
    return tuple(numbers_list)


# 7

def exercise_file_ext(file_name):
    file = file_name.split(".")
    return file[-1]


# 8

def exercise_colors(color_list):
    return print(f"First color: {color_list[0]}\nLast color: {color_list[-1]}")


# 9

def exercise_exam_date(exam_st_date):
    return print("The examination will start from : %i / %i / %i" % exam_st_date)


# 10

def exercise_triple_sum(num):
    double_num = num + num
    triple_num = num + num + num
    return num + double_num + triple_num


# 11

def exercise_abs_doc(func):
    return print(func.__doc__)


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
    diff = date_2 - date_1
    return print(diff.days)


# 15

def exercise_sphere_volume(r):
    volume = (4/3)*math.pi * r ** 3
    return print(f"Sphere volume: {volume}")


# 16

def number_diff(n):
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
