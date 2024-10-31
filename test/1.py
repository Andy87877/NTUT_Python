name = input()
number = int(input())

chinese = int(input())
pc = int(input())
program = int(input())

score = chinese+pc+program
avg = int(score/3)

print("Name:%s" %(name))
print("ID:%d" %(number))
print("Average:%d" %(avg))
print("Total:%d" %(score))