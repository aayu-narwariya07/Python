# creating a dictionary
student_grade = {
    "Maria": 85,
    "soumya": 78,
    "ramar" : 62
}

print("student grade:", student_grade)

#  Accessing dictionary values
alice_grade = student_grade["Maria"]
print("Maria's Grade:", alice_grade)

# Adding a new key-value pair
student_grade["Aarti"] = 90
print("update student grade:", student_grade)

# Removing key-value pair
student_grade.pop("Maria")
print("removing student grade:", student_grade)

# checking key membership
is_charlie_in_dict = "Aarti" in student_grade
print("Is charlie in the dictionary?", is_charlie_in_dict )

# Iterating over a dictionary (key and values)
print("Iterating over student names and grades ")
for student, grade in student_grade.items():
    print(f"{student}: {grade}")

# using the get ()method
david_grade = student_grade.get("ramar", "this is student grade not found ")
print("ramar's grade:", david_grade)

# marging dictionaries
additional_grade = {"bhawani": 60, "usha": 75}
student_grade.update(additional_grade)
print("student grade after merging with additional data:", student_grade)

# handling nested dictionary
nested_dict = {
    "USA": {"new york": 8000000, "los angeles": 4000000},
"India": {"Mumbai": 20000000, "Delhi":15000000}
}  
print("Nested dictionery of countries and cities: ", nested_dict)

# Accessing nested values
ny_population = nested_dict["USA"]["new york"]
print("population of new york:", ny_population)
# clearing and copying dictionaries
student_grade_copy = student_grade.copy()
print("Copy of student grades:", student_grade_copy)
student_grade.clear()
print("Student grades after clearing:", student_grade)
