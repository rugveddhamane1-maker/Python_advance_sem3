input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

first_two_lines = lines[:2]

with open(output_file, "w") as file:
    file.writelines(first_two_lines)

print("First two lines written successfully.")