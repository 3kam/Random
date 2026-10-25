print("Temperature Table:")
temperatures = [
    [18, 24, 20],
    [17, 22, 19],
    [19, 25, 21],
    [16, 23, 18],
    [20, 27, 22],
]

highest = temperatures[0][0]
lowest = temperatures[0][0]
total = 0
count = 0

for row in temperatures:
    print(row)

for row in temperatures:
    for value in row:
        if value > highest:
            highest = value
        if value < lowest:
            lowest = value

        total += value
        count += 1
average = total / count
print("\nHighest temperature: ", highest)
print("\nLowest temperature: ", lowest)
print("\nAverage temperature: ", round(average, 2))
