"""Write a python program to find the square root of the given number
using approximation method

testcase 1
input: 25
output: 4.999999999999998
testcase 2
input: 49
output: 6.999999999999991"""

def main():
    """Defining main"""
    square_s = int(input())
    eps_ilon = 0.01
    low_i = 0
    high_i = square_s
    guess_es = (low_i+high_i)/2
    while abs(guess_es**2-square_s) >= eps_ilon:
        if guess_es**2 > square_s:
            high_i = guess_es
        else:
            low_i = guess_es
        guess_es = (low_i+high_i)/2
    if (guess_es**2-square_s) >= eps_ilon:
        print("Failed")
    else:
        print(guess_es)

if __name__== "__main__":
	 main()
