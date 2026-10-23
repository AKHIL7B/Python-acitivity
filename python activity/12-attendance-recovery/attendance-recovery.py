#This program is to find the attendance recovery percentage of a student based on the number of classes attended and total classes held.
h = (input("Enter the total number of classes held: "))
a = (input("Enter the number of classes attended: "))
if not str(h).isdigit() or not str(a).isdigit():
    print("Invalid input. Please enter whole numbers only.")
else:
    total = int(h)
    attended = int(a)
    if total == 0:
        print("Total classes must be greater than 0.")
    elif attended > total:
        print("Attended classes cannot be more than total classes.")
    else:
        p = (int(a) / int(h)) * 100
        print(f"The present attendance percentage is: {p:.2f}%")
        for i in range(1, 10000):
            new_percentage = ((int(a) + i) / (int(h) + i)) * 100
    
            if p >= 75:
                print("The attendance percentage is already above 75%. No recovery needed.")
                break
            elif new_percentage >= 75:
                break
        if p < 75:          
            print(f"After attending {i} more classes, the attendance percentage will be: {new_percentage:.2f}%")        