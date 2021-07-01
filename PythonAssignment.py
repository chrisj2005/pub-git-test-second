largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try :
        numb = float(num)
    except :
        print('Invalid input')
        largest = -1
    for value in [7, 2, 10, 4] :
    	if value > largest_so_far :
            largest = value
    for value in [7, 2, 10, 4] :
    	if smallest is none :
            smallest = value
        elif value < smallest :
            smallest = value


    if num == "done" : break
    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)