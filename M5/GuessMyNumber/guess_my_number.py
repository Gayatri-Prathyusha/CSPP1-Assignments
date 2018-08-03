"""Guess My Number Exercise
"""
def main():
    """
    Main function"""
    least = 0
    low = 50
    high = 100
    guess = "Is your secret number: "
    print("Please think of a number between 0 and 100!")
    print(guess + str(least) + "?")
    s_request = input("$$$Enter 'h' to indicate the guess is too high. $$$$Enter 'l'\
     to indicate the guess is too low.$$$$$ Enter 'c' to indicate I guessed correctly. ")
    # In this problem, you'll create a program that guesses a secret number!
    while s_request != 'c':
        if  s_request == 'h':
            high = low
            low = int((low + least)/2)
        elif s_request == 'l':
            least = low
            low = int((low + high)/2)
        else:
            print("******Sorry, I did not understand your input.*********")
        print(guess + str(low) + "?")
        s_request = input("##Enter 'h' to indicate the guess is too high.## \
         Enter 'l' to indicate the guess is too low.#### \
         ###Enter 'c' to indicate I guessed correctly.### ")
    if s_request == 'c':
        print("Game over. Your secret number was:" + str(low))

main()
