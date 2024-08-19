while True:
    print("1.add")
    print("2.sub")
    print("3.mult")
    print("4.div")
    print("5.exit")
    c=int(input("enter choice: "))
    if c == 5:
        print("exit")
        break
    if c in [1,2,3,4]:
        n1=int(input("enter the number: "))
        n2=int(input("enter the number: "))
        if c == 1:
            result=n1+n2
            print(result)
            
        elif c == 2:
            result=n1-n2
            print(result)
        elif c == 3:
            result=n1*n2
            print(result)
        elif c == 4:
            result=n1/n2
            print(result)
    else:
        print("invalid choice")
    
