#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 9, 2025
# This code gets the user grade given user input


def grade_calculator(letter_grade):
    # Checks all possible grades you can get
    if letter_grade == "4+":
        grade_percent = 95
    elif letter_grade == "4":
        grade_percent = 90
    elif letter_grade == "4-":
        grade_percent = 85
    elif letter_grade == "3+":
        grade_percent = 79
    elif letter_grade == "3":
        grade_percent = 75
    elif letter_grade == "3-":
        grade_percent = 70
    elif letter_grade == "2+":
        grade_percent = 69
    elif letter_grade == "2":
        grade_percent = 65
    elif letter_grade == "2-":
        grade_percent = 60
    elif letter_grade == "1+":
        grade_percent = 59
    elif letter_grade == "1":
        grade_percent = 55
    elif letter_grade == "1-":
        grade_percent = 50

    # If is an invalid grade this happen
    else:
        grade_percent = -1
    return grade_percent


def main():
    # Get the user grade
    user_grade = input("What is your grade? ")

    # Get the percent by calling the function
    grade_percent = grade_calculator(user_grade)

    # If it is invalid this happens
    if grade_percent == -1:
        print("Please enter a valid grade (4+, 4, 3+, 3, etc.)")
    # If it is valid this happens
    else:
        print("Your grade is", grade_percent, "%")


if __name__ == "__main__":
    main()
