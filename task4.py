employees = [
    {"name": "Олена", "department": "Marketing", "salary":
    25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary":
    28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]

def get_department_stats(employee_list, target_dept):
    dept_employees = []
    for employee in employee_list:
        if employee["department"] == target_dept:
            dept_employees.append(employee)

    number_of_employees = len(dept_employees)

    total_salary = 0
    for employee in dept_employees:
        total_salary += employee["salary"]

    average_salary = round(total_salary / number_of_employees, 2)

    top = dept_employees[0]
    for employee in dept_employees:
        if employee["salary"] > top["salary"]:
            top = employee

IT = (get_department_stats(employees,"IT"))
Marketing = (get_department_stats(employees,"Marketing"))

print("-"*50)
print(f"У відділі {IT["department"]} середня зарплата склала {IT["average_salary"]}.\nЗ {IT["count"]} співробітників найкращим став/ла {IT['top_earner']}.")
print("-"*50)
print(f"У відділі {Marketing["department"]} середня зарплата склала {Marketing["average_salary"]}.\nЗ {Marketing["count"]} співробітників найкращим став/ла {Marketing['top_earner']}.")
print("-"*50)