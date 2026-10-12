employees = {
    101: "Alica",
    102: "Bob",
    103: "Charlie"
}
print(employees)

# Accessing a value
print(employees[101])

# Adding a new employee
employees[104] ="David"
print(employees)

# Updating an employe Name
employees[102] = "Robert"
print(employees)

# Removing an empployee

del employees[103]
print(employees)

#Loop through the dictionary
for emp_id,name,in employees.items():
    print(emp_id,":",name)