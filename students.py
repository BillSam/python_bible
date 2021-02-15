students = {
    "Alice": ["ID001", 26, "A"],
    "Bob": ["ID002", 26, "A"],
    "Sam": ["ID003", 26, "A"],
    "Pen": ["ID004", 26, "A"],
    "Nice": ["ID005", 26, "A"],
}

student = {
    "Alice": {"id": "ID001", "age": 26, "grade": "A"},
    "Bob": {"id": "ID001", "age": 26, "grade": "A"},
    "Sam": {"id": "ID001", "age": 26, "grade": "A"},
    "Pen": {"id": "ID001", "age": 26, "grade": "A"},
    "Nice": {"id": "ID001", "age": 26, "grade": "A"},
}

print(students["Alice"][1])

print(student["Pen"]["id"], student["Pen"]["grade"])

