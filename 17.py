N = 0
Name_list = []
Class_list = []

def check_ERROR(class_time):
    if (len(class_time) != 2):
        return True

    Weekday, Curriculum = class_time[0], class_time[1]

    if (not(ord('1') <= ord(Weekday) <= ord('5'))):
        return True

    if (not(ord('1') <= ord(Curriculum) <= ord('9'))):
        if (not(Curriculum == 'a' or Curriculum == 'b' or Curriculum == 'c')):
            return True
        
    return False

def get_Class():
    ERROR = False
    name = input()
    Name_list.append(name)

    H = int(input())
    tmp_list = ["a"]*H
    for i in range(H):
        class_time = input()
        ERROR = (check_ERROR(class_time)) or (ERROR)
        tmp_list[i] = class_time
    Class_list.append(tmp_list)

    return ERROR

def judge_hit(N):    
    CORRECT = True
    for i in range(N):
        for j in range(len(Class_list[i])):
            for i_2 in range(i+1, N):
                for j_2 in range(len(Class_list[i_2])):
                    # print("%s: %s      %s: %s"%(Name_list[i], Class_list[i][j], Name_list[i_2], Class_list[i_2][j_2]))
                    if (Class_list[i][j] == Class_list[i_2][j_2]):
                        print("%s,%s,%s"%(Name_list[i], Name_list[i_2], Class_list[i][j]))
                        CORRECT = False
    return CORRECT

def main():
    N = int(input())
    ERROR = False
    for ttttttttt in range(N):
        ERROR = get_Class() or ERROR

    # print(Name_list)
    # print(Class_list)

    if (ERROR):
        print(-1)
    else:
        CORRECT = judge_hit(N)
        if (CORRECT):
            print("correct")
            
    

main()