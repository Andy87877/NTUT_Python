def myPrint(n, mark):
    for i in range(n):
        print(mark, end = "")

def main():
    n = int(input())
    for i in range(n):
        # myPrint(n-i-1,".")
        # myPrint(i+1,"*")
        
        myPrint(i, ".")
        myPrint(n-i, "*")
        
        print()

main()