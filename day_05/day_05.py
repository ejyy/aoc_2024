with open("day_05_input.txt") as file:
    input = file.read().split("\n\n")

page_ordering = [page.split("|") for page in input[0].splitlines()]
page_numbers = [page.split(",") for page in input[1].splitlines()]

print(page_ordering)
print(page_numbers)
