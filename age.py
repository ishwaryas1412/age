def ages(age):
    newage=int(age)+18
    return newage

age=input("enter ur age :")
if int(age)<100:
    print(ages(age))
else:
    print("no way")
