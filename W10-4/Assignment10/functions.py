'''
functions module
We have two functions: sum_and_sorted() and cars()
Author: Ricardo Puma
'''
def sum_and_sorted(num1, num2=3.141592653589793, verbose=False):
    '''
    sum_and_sorted() which calculates the sum of two numbers and sorts them.
    '''

    total = num1 + num2
    sort_num = sorted([num1, num2])

    print(f"The sum of {num1} and {num2} is: {total}")

    if verbose:
        print(f"\nVerbose=True\n{num1=}\n{num2=}\nSum: {total}\nSorted: {sort_num}")

def make_shirt(text, size="L"):
  print(f"The shirt is a size {size}")
  print(f"We will print this text on the shirt: {text}")

if __name__ == '__main__':
    make_shirt("Live, Laugh, Love", "L")
    make_shirt(size="L", text="No Snacks? IM OUT")
    make_shirt("I love Python")
    make_shirt("I love Python", "M")
    make_shirt("In my defense I was left unsupervised", "XL")

    sum_and_sorted(15)
    sum_and_sorted(23, 2)
    sum_and_sorted(4, 3, True)