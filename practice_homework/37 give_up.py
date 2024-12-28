import math

# course_ 這四個字典有相關
course_amount = {}  # 課程標號+時間 學生的數量
course_student = {}  # 課程標號+時間 學生ID
course_time_dict = {}  # 課程標號+時間 學年時間
course_withdraw = {}  # 課程標號+時間 撤選率

times_course = {}  # 學年時間 課程標號

# student_ 這三個字典有相關
student_course = {}  # 學生ID 課程標號
student_score = {}  # 學生ID 分數
student_ranking_course = {}  # 學生ID 排名(該課程的排名)

# 學生ID 學年時間相關
student_time = {}  # 學生ID 學年時間
student_time_course = {}  # 學生ID 學年時間
student_time_withdraw = {}  # 學生ID 撤選率
student_time_score = {}  # 學生ID 學年成績

department_student = {}  # 入學年+科系(111530) 學生ID

All_department_list = []  # 入學年+科系
All_course_list = []  # 課程標號
All_student_list = []  # 學生ID


# 顯示字典
def show_dic():
    print("course_amount", course_amount)  # 課程標號+時間 學生的數量
    print("course_student", course_student)  # 課程標號+時間 學生ID
    print("course_time_dict", course_time_dict)  # 課程標號+時間 學年時間
    print("course_withdraw", course_withdraw)  # 課程標號+時間 撤選率

    print()
    print("times_course", times_course)  # 學年時間 課程標號

    # student_ 這三個字典有相關
    print()
    print("student_course", student_course)  # 學生ID 課程標號
    print("student_score", student_score)  # 學生ID 分數
    print("student_ranking_course", student_ranking_course)  # 學生ID 排名

    print("student_time_withdraw", student_time_withdraw)  # 學生ID 撤選率

    print("department_student", department_student)  # 入學年+科系(111530) 學生ID

    print()
    print("All_department_list", All_department_list)  # 入學年+科系
    print("All_course_list", All_course_list)  # 課程標號
    print("All_student_list", All_student_list)  # 學生ID


# 得到課程資訊
def get_course_data():
    # 課程標號, 開課時間, 學生人數
    course_ID, course_time, student_amount = input().split()

    # 檢查是不是國文或英文課
    Chinese_English = False
    if (course_ID[0:3]) == "101" or (course_ID[0:3]) == "201":
        Chinese_English = True

    # 開課時間 - 學年 (不用看學期)
    course_time = course_time[0:3]

    # 課程標號, 開課時間
    course_ID_and_time = course_ID + course_time

    # 學生人數
    student_amount = int(student_amount)

    # ID, score -> 算排名
    list_ID = []
    list_score = []

    Withdraw_amount = 0  # 退選人數

    for tmp_student in range(student_amount):
        student_data_list = list(input().split())

        student_ID = student_data_list[0]
        list_ID.append(student_ID)

        # 撤選
        if student_data_list[-1] == "w":
            score = -1
            Withdraw_amount += 1
        else:
            score = int(student_data_list[1])
            if Chinese_English:
                exam_score = int(student_data_list[2])
                score = score * 0.7 + exam_score * 0.3
            score = math.ceil(score)

        list_score.append(score)

        # dict 處理

        # 課程標號+時間 學號
        if course_ID_and_time in course_student:
            course_student[course_ID_and_time].append(student_ID)
        else:
            course_student[course_ID_and_time] = [student_ID]

        # 學生ID 該課程的關係
        if student_ID in student_course:
            student_course[student_ID].append(course_ID)  # 學生ID 課程編號
            student_score[student_ID].append(score)  # 學生ID 分數
        else:
            student_course[student_ID] = [course_ID]
            student_score[student_ID] = [score]

        department_ID = student_ID[0:6]

        if department_ID in department_student:
            department_student[department_ID].append(
                student_ID
            )  # 入學年+科系(111530) 學生ID
        else:
            department_student[department_ID] = [student_ID]

        if department_ID not in All_department_list:
            All_department_list.append(department_ID)  # 入學年+科系

        if student_ID not in All_student_list:
            All_student_list.append(student_ID)  # 入學年+科系

    # 排名次
    for i in range(student_amount):
        for j in range(student_amount):
            if list_score[i] > list_score[j]:
                list_ID[i], list_ID[j] = list_ID[j], list_ID[i]
                list_score[i], list_score[j] = list_score[j], list_score[i]

            if list_score[i] == list_score[j] and list_ID[i] > list_ID[j]:
                list_ID[i], list_ID[j] = list_ID[j], list_ID[i]
                list_score[i], list_score[j] = list_score[j], list_score[i]
    print(list_score)
    # 學生ID 與排名
    for rank in range(student_amount):
        student_ID = list_ID[rank]
        if list_score[rank] == -1:  # 退選
            student_ranking_course[student_ID].append(0)  # 沒有第0名
            break

        if student_ID in student_ranking_course:
            student_ranking_course[student_ID].append(rank + 1)  # 學生ID
        else:
            student_ranking_course[student_ID] = [rank + 1]  # 學生ID 排名

    # 結束迴圈(紀錄數據)
    Withdraw_rate = math.floor(100 * (Withdraw_amount / student_amount))  # 課程的撤選率

    # 處理 課程標號 dict
    if course_ID not in All_course_list:
        All_course_list.append(course_ID)  # 課程標號
        course_amount[course_ID_and_time] = [student_amount]
        course_time_dict[course_ID_and_time] = [course_time]
        course_withdraw[course_ID_and_time] = [Withdraw_rate]
    else:
        course_amount[course_ID_and_time].append(student_amount)  # 課程標號 學生的數量
        course_time_dict[course_ID_and_time].append(course_time)  # 課程標號 學年時間
        course_withdraw[course_ID_and_time].append(Withdraw_rate)  # 課程標號 撤選率

    if course_time not in times_course:
        times_course[course_time] = [course_ID]
    else:
        times_course[course_time].append(course_ID)  # 學年時間 課程標號


# 得到學生的撤選率
def mange_student_withdraw():
    All_student_amount = len(All_student_list)

    # student_time_withdraw = {}  # 學生ID 撤選率

    for student_ID in All_student_list:
        score_list = student_score[student_ID]  # 分數的list
        Withdraw_amount = score_list.count(-1)  # 徹選的數量

        Withdraw_rate = math.floor(
            100 * (Withdraw_amount / len(score_list))
        )  # 學生的撤選率

        student_time_withdraw[student_ID] = Withdraw_rate


def sort_all_list():
    All_department_list.sort()
    All_course_list.sort()
    All_student_list.sort()


def main():
    input_amount = int(input())
    for tmp_amount in range(input_amount):
        get_course_data()

    mange_student_withdraw()  # 處理學生撤選率

    sort_all_list()  # 排序list

    show_dic()  # 顯示字典

    # 輸出各科系、各年級、每年的平均成績前三名的名次百分比與撤選百分比


main()

"""
【【輸出說明】
輸出分為以下三部分，每一部分中間無間隔
1.  輸出各科系、各年級、每年的平均成績前三名的名次百分比與撤選百分比
2.  輸出每個課程、每年所有非撤選學生的最高學期成績、平均學期成績、最低學期成績和課程的撤選百分比（無條件捨去至整數），前三名的成績和名次百分比。
3.  輸出在搜尋的學科編碼，歷年學期分數最高的前兩名學號和最多人數的科系


每個學科一學年僅開一次，且每位學生一年至少上完一堂課，各項數值計算如下：
1.  排名：成績較高排名較前，若成績相同則學號編碼較小排名較前
2.  課程撤選百分比： 課程撤選人數/課程總人數
3.  學生撤選百分比:    學生撤選的課程數/學生選修的課程數
4.  學年平均成績： 該學年所有非撤選課程成績*該課程學分數加總/該學年所有非撤選學分數且無條件捨去至整數
5.  名次百分比：
"""
