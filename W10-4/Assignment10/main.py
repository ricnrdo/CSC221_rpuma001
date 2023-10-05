import functions

def infinite_sum():
    while True:
        num1 = input("Give me your first number? ('quit' to end program): ")
        if num1 == "quit":
            break

        num2 = input("Give me your second number? ('quit' to end program): ")
        if num2 == "quit":
            break
        
        num1 = int(num1)
        num2 = int(num2)
        functions.sum_and_sorted(num1, num2)
    
    return

def makeShirt():
    text = input("What text would you like to print in the shirt?: ")
    size = input("What shirt size do you want to order? (For default size L, hit Enter)\n")

    if size:
        functions.make_shirt(text, size)
    else:
        functions.make_shirt(text)

infinite_sum()
print("\n")
makeShirt()