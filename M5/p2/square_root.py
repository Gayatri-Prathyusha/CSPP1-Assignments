"""Write a python program to find the square root of the given number
using approximation method
testcase 1
input: 25
output: 4.999999999999998

testcase 2
input: 49
output: 6.999999999999991"""
def main():
    """your code here"""
    square = int(input())
    epsilon = 0.01
    guess = 0.0
    i = 0.0001
    num_of_guess = 0
    while abs(guess**2 - square) >= epsilon:
        guess += i
        num_of_guess += 1
    if abs(guess**2 - square) > epsilon:
        print('Failed')
    else:
        print(guess)

if __name__ == "__main__":
   main()
