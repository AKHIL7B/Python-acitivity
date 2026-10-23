# This program is to print a hollow diamond pattern 
h  = (input("Enter the height of the of pattern(1-74) :"))
if h.startswith("-") and h[1:].isdigit():
    print("Negative number entered. Please enter a number between 1 and 74.")
elif not h.isdigit():
    print("Invalid input. Please enter a whole number between 1 and 74.")
else :
        h = int(h)
        if h >= 75:
            print("given number is greater the pattern will not be printed well give number less than 75.")
        elif h <= 0 :
            print("given number is less than 1 the pattern will not be printed well give number greater than 0.")
  
        else:
            
            for i in range(h):
                for j in range(h-i-1):
                    print(" ", end="")
                for j in range(2*i+1):
                    if j == 0 or j == 2*i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
            for i in range(h-2, -1, -1):
                for j in range(h-i-1):
                    print(" ", end="")
                for j in range(2*i+1):
                    if j == 0 or j == 2*i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()


         
    