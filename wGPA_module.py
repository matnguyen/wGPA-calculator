### Weighted GPA Calculators
def UBC(transcript):
    global credits
    global A_flag
    global courses
    cGPA = 0
    year_GPA = 0
    year_courses = 0
    year_credits = 0
    A_plus = {"A+": 95, "A": 87, "A-": 82, "B+": 78, "B": 74, "B-": 70, "C+": 66, "C": 62, "C-": 58,
              "D+": 54, "D": 50, "D-": 46, "F": 25}
    A = {"A": 92, "A-": 84, "B+": 78, "B": 74, "B-": 70, "C+": 66, "C": 62, "C-": 58, "D+": 54,
         "D": 50, "D-": 46, "F": 25}
    GPAs = []
    total_credits = []
    print("University of British Columbia")

    for year in range(len(transcript)):
        for semester in range(len(transcript[year])):
            if A_flag: # Your school offers A+
                cGPA += A_plus[transcript[year][semester]]
                year_courses += 1
                year_GPA += A_plus[transcript[year][semester]]
                year_credits += 1
            else:
                cGPA += A[transcript[year][semester]]
                year_courses += 1
                year_GPA += A[transcript[year][semester]]
                year_credits += 1
        GPAs.append(year_GPA/year_credits)
        total_credits.append(year_credits)
        year_GPA = 0
        year_courses = 0
        year_credits = 0
    print("Your cumulative GPA for UBC is:", cGPA/courses)
    if credits < 90:
        print("\nYOU ARE NOT ELIGIBLE FOR THE WEIGHTED GPA")
        return
    else:
        index_lowest = GPAs.index(min(GPAs))
        if total_credits[index_lowest] <= 30:
            GPAs.pop(index_lowest)
        else:
            lowest_year_GPA = []
            lowest_year_credits = []
            credits_removed = 0
            for course in range(len(transcript[index_lowest])):
                if A_flag:
                    lowest_year_GPA = A_plus[transcript[index_lowest][course][0]]
                else:
                    lowest_year_GPA = A[transcript[index_lowest][course][0]]
                lowest_year_credits = transcript[index_lowest][course][1]
            while credits_removed <= 30:
                index_to_remove = lowest_year_GPA.index(min(lowest_year_GPA))
                lowest_year_GPA.pop(index_to_remove)
                credits_removed += lowest_year_credits[index_to_remove]
                lowest_year_credits.pop(index_to_remove)
            GPAs[index_lowest] = lowest_year_GPA
        wGPA = sum(GPAs)/len(GPAs)
        print("Your weighted GPA for UBC is:", wGPA)
