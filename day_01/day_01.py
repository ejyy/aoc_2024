left_list, right_list = [], []

total_list = []
similarity_index = 0

with open("day_01_input.txt") as file:
    for line in file:
        split_line = line.split("   ")
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1]))

left_list.sort()
right_list.sort()

for idx, x in enumerate(left_list):
    total_list.append(abs(x - right_list[idx]))

print("Part 1:", sum(total_list))

left_dict = {x:left_list.count(x) for x in left_list}
right_dict = {x:right_list.count(x) for x in right_list}

for left_key, left_value in left_dict.items():
    if left_key in right_dict:
        similarity_index += left_value * (left_key * right_dict[left_key])

print("Part 2:", similarity_index)
