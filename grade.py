#Umair Sayeed
#Gets number grade from user as input and outputs corresponding letter grade.

numGrade = eval(input("Enter your grade: "))

if numGrade > 89:
    print("A")
elif numGrade > 79:
    print("B")
elif numGrade > 69:
    print("C")
elif numGrade > 59:
    print("D")
else:
    print("F")