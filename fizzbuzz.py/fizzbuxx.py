


print("Welcome to FizzBuzz!")

max_number = int(input("Enter a maximum number: "))
for i in range(1, max_number + 1):
    
   if i % 3 == 0 and i % 5 == 0:
        print(f"{i} - FizzBuzz")
    

    elif i % 3 == 0:
        print(f"{i} - Fizz")
    
    
    elif i % 5 == 0:
        print(f"{i} - Buzz")
      
    else:
        print(i)
print(f"Done! Checked {max_number} numbers.")

