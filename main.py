
#Ilia (Part 3)

def main():
    while True:
        print("What task would you like to use:")
        print("1: Finding the factorial")
        print("2: Finding the fibonacci value")
        user_selection = int(input("Enter the number to be performed: "))

        if user_selection == 1:
            num = int(input("Enter the integer you'd like to find its factorial: "))
            print(f"The factorial of {num} is: {factorial(num)}")
        elif user_selection == 2:
            position_sequ = int(input("Enter the sequence position of the fibonacci value: "))
            print(f"The {position_sequ}th fibonacci is {fibonacci(position_sequ)}")
        else:
            print("Pleaser select 1 or 2.")


if __name__ == "__main__":
    main()
