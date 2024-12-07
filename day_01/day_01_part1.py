list1 = []
list2 = []
list3 = []

with open("day_01_input.txt") as file:
    for line in file:
        split_line = line.split("   ")
        list1.append(int(split_line[0]))
        list2.append(int(split_line[1]))

list1.sort()
list2.sort()

for idx, x in enumerate(list1):
    list3.append(abs(x - list2[idx]))

print(sum(list3))
