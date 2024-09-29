Timetable = [] # 課程表
Timetable_name = [] # 課程表 第幾節
END = False

def init(): # 初始化
    for i in range(5):
        temp = []
        for j in range(12):
            temp.append([])
        Timetable.append(temp)

        temp = []
        for j in range(12):
            if (j >= 9):
                str_tmp = str(i+1)
                str_tmp += chr(j-9 + ord('a'))
            else:
                str_tmp = str(i+1)+str(j+1)
            temp.append(str_tmp)
        Timetable_name.append(temp)

    # print(Timetable)

    # for i in range(len(Timetable)):
    #     for j in range(len(Timetable[i])):
    #         print(Timetable[i][j], end = ",")
    #     print()

def input_data():
    Bug = False
    name = input()
    H = int(input())

    

    if (H > 3 or H < 1): 
        Bug = True
    for tttttttttttttttttttttttttttttttttttt in range(H):
        time_class = input()

        if (len(time_class) != 2):
            Bug = True
            continue

        Week = time_class[0]
        Section = time_class[1]
        Section_num = 0

        if (ord(Week) < ord('1') or ord(Week) > ord('5')):
            Bug = True
            continue

        if (ord('1') <= ord(Section) <= ord('9')):
            Section_num = int(Section)-1
        elif (Section == 'a' or Section == 'b' or Section == 'c'):
            Section_num = (ord(Section)-ord('a'))+9
        else:
            Bug = True
            continue

        Week = int(Week)

        Temp_List = list(Timetable[Week-1][Section_num])
        # print(Temp_List, name, end = "  wwwwww\n")
        Temp_List.append(name)
        Timetable[Week-1][Section_num] = Temp_List
        # print(Temp_List, name, end = "  .........\n")

        # Timetable_name[Week-1][Section_num] = time_class

        # print(Week-1, Section_num)
        # print_table()
    


    return Bug
    
def print_coiilade(List, name):
    n = len(List)

    for i in range(n):
        for j in range(i+1, n):
            print("%s,%s,%s" %(List[i], List[j], name))



def check():
    for i in range(5): # Week
        for j in range(12): # Section
            if (len(Timetable[i][j]) >= 2):
                print_coiilade(Timetable[i][j], Timetable_name[i][j])
                
def print_table():
    # print(Timetable)
    for i in range(len(Timetable)):
        for j in range(len(Timetable[i])):
            print(Timetable[i][j], end = " ")
        print(";")
    print("=======================")

def main():
    END = False
    init() # 初始化

    TIMESSSSSS = int(input())
    for tttttttttttttttttttt in range(TIMESSSSSS):
        Bug = input_data()
        END = (Bug or END)

    # print_table()

    if (END):
        print(-1)
    else:
        check()


main()