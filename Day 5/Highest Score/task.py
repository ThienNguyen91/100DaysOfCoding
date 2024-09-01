student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
Min = student_scores[0]
Max = student_scores[0]
for score in student_scores:
    if score < Min:
        Min = score
    if score > Max:
        Max = score
print(Min, Max)
