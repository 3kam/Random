import random
grid = [[" " for _ in range(5)]for _ in range(5)]
diamonds_placed = 0

while diamonds_placed < 15:
    row = random.randint(0, 4)
    col = random.randint(0 ,4)

    if grid[row][col] == " ":
        grid[row][col] = "X"
        diamonds_placed += 1

for row in grid:
    print("| " + " | ".join(row) + " |")