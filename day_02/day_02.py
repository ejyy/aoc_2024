number_safe_reports = 0

with open("day_02_input.txt") as file:
    for line in file:
        report = [int(x) for x in line.strip().split()]
        report_safe = True

        increasing = all(report[i+1] - report[i] > 0 for i in range(len(report)-1))
        decreasing = all(report[i+1] - report[i] < 0 for i in range(len(report)-1))

        if not (increasing or decreasing):
            report_safe = False

        for i in range(len(report)-1):
            diff = abs(report[i+1] - report[i])
            if diff < 1 or diff > 3:
                report_safe = False

        if report_safe:
            number_safe_reports += 1

print("Part 1:", number_safe_reports)
