# page 11

with open("filename.txt", "r") as infile:
    line_num = 0
    for line in infile:
        line_num += 1
        if line_num % 2 == 0:
            print(line, end="")
