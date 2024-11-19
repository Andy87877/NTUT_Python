# page 13

with open("hello.txt") as f:
    for line in f:
        if line.strip()[0] != "#":
            print(line)
