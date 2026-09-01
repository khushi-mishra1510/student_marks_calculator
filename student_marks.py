name=input("enter your name:")
maths=float(input("enter maths marks: "))
python=float(input("enter python marks: "))
english=float(input("enter english marks: "))

total= maths + python + english
percentage = round(total/3,2) 

print("\n--- Student Result ---")
print("Name:",name)
print("Total Marks:", total)
print("Percentage:" , percentage)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
     grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print(" Grade",grade)   

if percentage >= 40:
    print("Result : Pass")
else:
    print("Result: Fail")
