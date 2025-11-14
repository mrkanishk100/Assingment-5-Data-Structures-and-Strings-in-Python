students = {                                             # Creating the dictionary
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}

a = input("Enter the student's name: ")                  # Ask the user for a student's name

if a in students:                                        # Retrieve and display marks or show 'not found'
    print(f"{a}'s marks: {students[a]}")
else:
    print("Student not found.")
