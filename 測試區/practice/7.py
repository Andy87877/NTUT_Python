# 輸入每月網內、網外、市話、通話時間(秒)及網內、網外簡訊則數、網路流量，求最佳資費。

List_money = [183, 383, 983, 1283]

List_in_wifi_voice = [0.08, 0.07, 0.06, 0.05]
List_out_wifi_voice = [0.139, 0.130, 0.108, 0.100]
List_phone_voice = [0.135, 0.121, 0.101, 0.090]

List_in_wifi_txt = [1.128, 1.128, 1.128, 1.128]
List_out_wifi_txt = [1.483, 1.483, 1.483, 1.483]

List_wifi_flow = [1, 3, 5, 999999999999999999999]
List_wifi_flow_add = [250, 200, 150, 0]


def judge(
    index,
    in_wifi_voice,
    out_wifi_voice,
    phone_voice,
    in_wifi_txt,
    out_wifi_txt,
    wifi_flow,
):
    money = 0

    money += List_in_wifi_voice[index] * in_wifi_voice
    money += List_out_wifi_voice[index] * out_wifi_voice
    money += List_phone_voice[index] * phone_voice

    money += List_in_wifi_txt[index] * in_wifi_txt
    money += List_out_wifi_txt[index] * out_wifi_txt

    now_flow = wifi_flow
    now_flow -= List_wifi_flow[index]

    if now_flow > 0:
        money += List_wifi_flow_add[index] * now_flow

    if money < List_money[index]:
        money = List_money[index]

    return money


in_wifi_voice = int(input())
out_wifi_voice = int(input())
phone_voice = int(input())
in_wifi_txt = int(input())
out_wifi_txt = int(input())
wifi_flow = int(input())

min_money = 999999999999999999999
ans_choose = 0

for i in range(4):
    money = judge(
        i,
        in_wifi_voice,
        out_wifi_voice,
        phone_voice,
        in_wifi_txt,
        out_wifi_txt,
        wifi_flow,
    )

    if money < min_money:
        min_money = money
        ans_choose = List_money[i]

print("%d" % (min_money))
print("%d" % (ans_choose))
