marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}
name = input("Enter the student's name: ")

if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print(f"Student '{name}' not found in the records.")
