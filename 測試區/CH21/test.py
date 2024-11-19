s = "\u4eba\u751f\u82e6\u77ed\uff0cpy\u662f\u5cb8"
print(type(s))  # <class 'str'>
print(s)  # 人生苦短，py是岸
s_utf8 = s.encode(encoding="utf-8")
print(s_utf8)
# b'\xe4\xba\xba\xe7\x94\x9f\xe8\x8b\xa6\xe7\x9f\xad\xef\xbc\x8cpy\xe6\x98\xaf\xe5\xb2\xb8’print(type(s_utf8)) #<class 'bytes'>

print()
string = "大家好，我是呵呵呵呵"
print(string)

encode_utf8 = string.encode("utf-8")
encode_gbk = string.encode("gbk")

print(encode_utf8)
print(encode_gbk)

print(encode_utf8.decode("utf-8"))
print(encode_gbk.decode("gbk"))


