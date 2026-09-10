def pattern(number1):
    
    for i in range(number1  , 0 , -1):

        for j in range (i , 0 , -1):
            print(j , end=" ")

        print("")

User_Number = int(input("Enter Number : "))
pattern(User_Number)