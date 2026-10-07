INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

math_sum = 0
python_sum = 0
english_sum = 0
count = 0

best_name = ""
best_avg = 0

with open(INPUT_FILE, encoding="utf-8") as f:
    next(f)
    for line in f:
        parts = line.strip().split(",")
        name = parts[0]
        math = int(parts[1])
        python = int(parts[2])
        english = int(parts[3])

        math_sum += math
        python_sum += python
        english_sum += english
        count += 1

        student_avg = (math + python + english) / 3
        if student_avg > best_avg:
            best_avg = student_avg
            best_name = name

math_avg = math_sum / count
python_avg = python_sum / count
english_avg = english_sum / count

result = (
    "Середній бал по класу:\n"
    f"math: {math_avg:.1f}\n"
    f"python: {python_avg:.1f}\n"
    f"english: {english_avg:.1f}\n"
    "\n"
    f"Найкращий студент: {best_name} ({best_avg:.1f})\n"
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(result)

print(result)
