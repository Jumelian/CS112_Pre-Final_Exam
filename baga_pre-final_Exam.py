print (" ")
print (" ")
print (" ")
print ("problem: Create a python program that display all prime numbers within a range")
print (" ")
print (" ")
print ("RULES TO CONSIDER:")
print ("[1] If number (start) is a negative number. The program will prompt a message [Enter a non-negative number].")
print ("[2] If number (end) is less than number (start). The program will prompt a message [Enter a number greater than number (start)]")
print ("[3] Lastly, if the user enter the number [0], the program will terminate.")
print (" ")
print (" ")
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
while True:
    start = int(input("enter a number [Start]: "))
    if start == 0:
        print("program terminated.")
        break
    if start < 0:
        print("enter a non-negative number.")
        continue
    end = int(input("Enter a number [end]: "))
    if end < start:
        print(f"enter a number greater than {start}.")
        continue
    if end == 0:
        print("program terminated.")
        break
    print(f"prime numbers between {start} and {end} are: {', '.join(str(number) for number in range(start, end + 1) if is_prime(number))}")