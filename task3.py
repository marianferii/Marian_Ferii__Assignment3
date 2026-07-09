exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60

passed = 0
for student in exam_results:
    if student["score"] >= passing_score:
        student["passed"] = True
        passed += 1
    else:
        student["passed"] = False

print(exam_results)
print("-"*50)
print(f"Кількість студентів які здали: {passed}")

total_score = 0
for student in exam_results:
    total_score += student["score"]
average = total_score / len(exam_results)
print(f"Середній бал: {average}")