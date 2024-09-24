plan_money = [183, 383, 983, 1283]
list_sound_wifi_in = [0.08, 0.07, 0.06, 0.05]
list_sound_wifi_out = [0.139, 0.130, 0.108, 0.1]
list_sound_wifi_phone = [0.135, 0.121, 0.101, 0.09]

list_text_wifi_in = [1.128, 1.128, 1.128, 1.128]
list_text_wifi_out = [1.483, 1.483, 1.483, 1.483]

list_wifi_traffic = [1,3,5, 9999999999]
list_wifi_add_money = [250, 200, 150, 0]

money = [0,0,0,0]

sound_wifi_in = int(input())
sound_wifi_out = int(input())
sound_wifi_phone = int(input())

text_wifi_in = int(input())
text_wifi_out = int(input())
wifi_traffic = int(input())

min_money = 100000000000000

for i in range(4):
    now_money = 0
    now_money += sound_wifi_in*list_sound_wifi_in[i]
    now_money += sound_wifi_out*list_sound_wifi_out[i]
    now_money += sound_wifi_phone*list_sound_wifi_phone[i]

    now_money += text_wifi_in*list_text_wifi_in[i]
    now_money += text_wifi_out*list_text_wifi_out[i]

    if (wifi_traffic > list_wifi_traffic[i]):
        now_money += (wifi_traffic - list_wifi_traffic[i])*list_wifi_add_money[i]

    if (now_money < plan_money[i]):
        money[i] = plan_money[i]
    else:
        money[i] = now_money

    if (money[i] < min_money):
        min_money = money[i]

for i in range(4):
    if (money[i] == min_money):
        print("%d"%money[i])
        print(plan_money[i])
        break