exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45},
    {"student_name": "Дарина", "score": 60},
]

passing_score = 60

for student in exam_results:
    if student["score"] >= passing_score:
        student["passed"] = True
    else:
        student["passed"] = False

for s in exam_results:
    result = "склав" if s["passed"] else "не склав"
    print(f"{s['student_name']}: {s['score']} балів - {result}")

print()
print(exam_results)

total = 0
for s in exam_results:
    total += s["score"]

print(f"\nСередній бал: {round(total / len(exam_results), 1)}")