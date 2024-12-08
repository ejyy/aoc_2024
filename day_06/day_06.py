import numpy as np

with open("day_06_input.txt") as file:
    read_file = file.readlines()

# Create a 2D numpy array representing the puzzle grid
puzzle_grid = np.array([list(line.strip('\n')) for line in read_file])

# Find the starting position of "^"
starting_position = np.where(np.char.find(puzzle_grid, "^") == 0)
starting_x = starting_position[0].tolist()[0]
starting_y = starting_position[1].tolist()[0]

def move_position(current_x, current_y, x_offset, y_offset):
    # Calculate new grid reference
    new_x = current_x + x_offset
    new_y = current_y + y_offset

    # Bounds checking: if ^ would move out of bounds, return a signal to stop
    if new_x < 0 or new_x >= puzzle_grid.shape[0] or new_y < 0 or new_y >= puzzle_grid.shape[1]:
        return "OOB"

    # Check if the next position is blocked by '#'
    if puzzle_grid[new_x, new_y] == "#":
        return False

    # Replace current position with 'X'
    puzzle_grid[current_x][current_y] = "X"

    # Move '^' to new position
    puzzle_grid[new_x][new_y] = "^"

    return new_x, new_y

# Define directions: (x_offset, y_offset) for up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_index = 0  # Start by moving upwards (index 0)

while True:
    x_offset, y_offset = directions[direction_index]

    # Try to move in the current direction
    result = move_position(starting_x, starting_y, x_offset, y_offset)

    if result == "OOB":
        # ^ Moving out-of-bounds so puzzle complete
        break
    elif result:
        # Update current coordinates to new location of ^
        starting_x, starting_y = result
    else:
        # Turn 90 degrees (next direction)
        direction_index = (direction_index + 1) % 4

# Flatten the grid and count occurences of 'X' (+1 for final ^ position)
output_list = puzzle_grid.flatten().tolist()
d = {x:output_list.count(x) for x in output_list}

print("Part 1:", d['X'] + 1)
