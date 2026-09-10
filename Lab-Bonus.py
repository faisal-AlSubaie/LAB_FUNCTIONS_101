def pattern(number1):
    word = "" 
    
    for i in range(number1, 0, -1):
        for j in range(i, 0, -1):
            word = word + str(j) + " " 
            
        word = word + "\n" 
        
    return word 

User_Number = int(input("Enter Number : "))
printPattern = pattern(User_Number) 
print(printPattern)