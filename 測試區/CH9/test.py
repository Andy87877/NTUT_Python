try:
    fp = open("hello.txt", "r")
    print(fp.read())
    fp.write("test")
except FileNotFoundError:
    print("file not found")
except:
    print("Something wrong")
finally:
    print("OK")
