import re

plain_mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
#do_dont_pattern = r'do\(\)|don\'t\(\)'

with open('day_03_input.txt', 'r') as file:
    data = file.read().rstrip()
    plain_mul_matches = re.findall(plain_mul_pattern, data)
    #do_dont_matches = re.findall(do_dont_pattern, data)

part_1_sum = 0

for match in plain_mul_matches:
    part_1_sum += int(match[0]) * int(match[1])

print("Part 1:", part_1_sum)

#print(do_dont_matches)
