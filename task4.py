employees = [
    {"name": "Олена", "department": "Marketing", "salary": 25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary": 28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]


def get_department_stats(employee_list, target_dept):
    dept = []
    for emp in employee_list:
        if emp["department"] == target_dept:
            dept.append(emp)

    if len(dept) == 0:
        return f"Відділ '{target_dept}' не знайдено"

    total = 0
    for emp in dept:
        total += emp["salary"]
    avg = round(total / len(dept), 2)

    top = dept[0]
    for emp in dept:
        if emp["salary"] > top["salary"]:
            top = emp

    return {"department": target_dept, "average_salary": avg, "top_earner": top["name"], "count": len(dept)}


it_result = get_department_stats(employees, "IT")
mark_result = get_department_stats(employees, "Marketing")

print("IT:", it_result)
print("Marketing:", mark_result)
print("HR:", get_department_stats(employees, "HR"))