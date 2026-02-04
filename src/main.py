count=0
for i in range(1, 10):
    name = input("Enter student name: ")
    present = input("Is " +name+ " present? (yes/no): ")

    if present == "yes":
        count += 1
    elif present == "no":
        count=count
    else:
        print("Invalid input")

print("Number of present students:", count)
