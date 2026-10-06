subjects = ["maths","science","history","english","geography"]


def check_result():
    total_marks=0
    for i in subjects:
        marks = int(input("Enter marks for "+i+": "))
        total_marks = total_marks+marks
    print("Total marks scored : ", total_marks)
    if total_marks > 250:
        print("You Passed!")
    else:
        print("You Failed :(")

check_result()

