"""" Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube"""
def main():
    """code is here"""
    guess = 0
    x_val = int(input())
    while guess**3 < x_val:
        guess = guess + 1
    if guess**3 == x_val:
        print(x_val , "is a perfect cube")
    else:
        print(x_val , "is not a perfect cube")
if __name__ == "__main__":
    main()
