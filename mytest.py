x = input("Enter Score between 0.0 and 1.0: ")
number = float(x)
if number >= 0.9 :
    print('A')
elif number >= 0.8 :
    print ('B')
elif number >= 0.7 :
    print ('C')
elif number >= 0.6 :
    print ('D')
elif number < 0.6 :
    print ('F')
else :
    print('Error, incorrect grade has been put in')
    #Second Program Ever Done