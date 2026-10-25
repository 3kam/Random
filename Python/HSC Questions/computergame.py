scores = [3, 5, 5, 2, 1 ,4, 0, 1, 4, 5]

points = []
for i in range(len(scores)):
    if scores[i] == 5:
        if i == len(scores) - 1:
            points.append(10)
        else:
            points.append(5 + scores[i + 1])
    else:
        points.append(scores[i])
print(f"{'Round':<8}{'Score':<8}{'Points'}")

total_points = 0
for i in range(len(scores)):
    round_num = i + 1
    print(f"{round_num:<8}{scores[i]:<8}{points[i]}")
    total_points += points[i]
print(f"Total Points: {total_points}")