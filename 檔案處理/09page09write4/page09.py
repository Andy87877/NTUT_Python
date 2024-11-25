# page 09

text = ["this is ", "a book"]

with open("out.txt", "a") as out_file:
    for line in text:
        out_file.write(line)
