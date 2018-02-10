#!/usr/bin/python3

########################################################
# Weighted GPA Calculator for Canadian Medical Schools #
# v0.1                                                 #
#                                                      #
# By: Matthew Nguyen                                   #
#                                                      #
# GNU GENERAL PUBLIC LICENSE                           #
# Version 3, 29 June 2007                              #
########################################################

### Weighted GPA Calculators
def UBC(transcript):
    global credits
    global A_flag
    A_plus = {"A+": 95, "A": 87, "A-": 82, "B+": 78, "B": 74, "B-": 70, "C+": 66, "C": 62, "C-": 58,
              "D+": 54, "D": 50, "D-": 46, "F": 25}
    A = {"A": 92, "A-": 84, "B+": 78, "B": 74, "B-": 70, "C+": 66, "C": 62, "C-": 58, "D+": 54,
         "D": 50, "D-": 46, "F": 25}
    year_gpa = []
    print("University of British Columbia")

    for year in range(len(transcript)):
        for semester in range(len(transcript[year])):
            if A_flag == True: # Your school offers A+


    if credits < 90:
        print("YOU ARE NOT ELIGIBLE FOR THE WEIGHTED GPA")

### Helper functions
# Requests the number of years completed by the user
def years_input():
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8}
    years = input("How many years have you completed? ")
    if years.isdigit():
        years = int(years)
    else:
        years = words[years]
    return years

def transcript_input(years):
    global credits
    transcript = [[[] for i in range(3)] for j in range(years)] # Empty transcript
    semester_dict = {"0": "Fall", "1": "Winter/spring", "2": "Summer"}
    year_dict = {"0": "first", "1": "second", "2": "third", "3": "fourth", "4": "fifth", "5": "sixth",
                 "6": "seventh", "7": "eighth"}
    grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    user_input = ""
    for year in range(years): # Starts at first year
        for semester in range(3): # Semester starts at fall
            print("\n", semester_dict[str(semester)], "of", year_dict[str(year)], "year")
            print("\nEnter grades and course credits in this format")
            print("FORMAT: grade,credit (ex. A+,3)")
            print("Press N to go to the next semester, X to stop inputting courses")
            while True:
                user_input = input("Please enter your grade and credits for a course in this semester: ")
                if user_input == "N" or user_input == "X":
                    break
                input_list = [x.strip() for x in user_input.split(',')]
                if input_list[0] not in grades and (user_input != "N" and user_input != "X"):
                    print("That is not a valid input.")
                transcript[year][semester].append((input_list[0],input_list[1]))
                credits += int(input_list[1])
            if user_input == "X":
                return transcript
            print(transcript)

### Main Interface
credits = 0 # Number of credits completed
A_flag = False # Keeps track if the school uses A+
years = years_input()
transcript = transcript_input(years)

while True:
    user_input = input("\nDoes your school offer A+? (Y/N): ")
    if user_input == "Y":
        A_flag = True
        break
    elif user_input != "N":
        print("That is not a valid input")


