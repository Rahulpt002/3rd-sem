x=input("enter the word: ")
r=reversed(x)
if list(x)==list(r):
    print("palindrom")
else:
    print("not palindrom")
