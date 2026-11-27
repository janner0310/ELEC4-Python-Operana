# Name: JOFIL OPERANA
# Section: IV-BSIT-B
# Activity: P2 - Custom Module
# Date: November 27, 2026

def calculate_average(grades):
    return sum(grades) / len(grades)


def check_pass_fail(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "Passed"
    else:
        return "Failed"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)
