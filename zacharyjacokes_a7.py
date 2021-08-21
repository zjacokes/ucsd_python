num_lines = 0
num_charc = 0
num_space = 0
num_break = 0

f = open('lesson7_file.txt', 'r')
lines = f.readlines()

for line in lines:
    num_lines = num_lines + 1
    print(str(num_lines) + '. ' + line)
    for char in line:
        if " " in char:
            num_space = num_space + 1
        elif "\n" in char:
            num_break = num_break + 1
        else:
            num_charc = num_charc + 1

print('\n \nFile statistics: \n')
print("Line count: " + str(num_lines))
print("Word count: " + str(num_space + num_break))
print("Character count: " + str(num_charc))
print("Space count: " + str(num_space))
print("Break count: " + str(num_break))
