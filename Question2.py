string = input("Please Enter your Own String : ")
alphabets = digits = special = UppercaseAlphabets = LowercaseAplhabets = 0

for i in range(len(string)):
    if(string[i].isalpha()):
      if(string[i].isupper()):
        UppercaseAlphabets = UppercaseAlphabets + 1
      elif(string[i].islower()):
        LowercaseAplhabets = LowercaseAplhabets + 1


        alphabets = alphabets + 1
    elif(string[i].isdigit()):
        digits = digits + 1

    else:
        special = special + 1

print("\nTotal Number of Alphabets in this String :  ", alphabets)
print("\nTotal Number of Lowercase Alphabets in this String :  ", LowercaseAplhabets)
print("\nTotal Number of Uppercase Alphabets Alphabets in this String :  ", UppercaseAlphabets)

print("Total Number of Digits in this String :  ", digits)
print("Total Number of Special Characters in this String :  ", special)
