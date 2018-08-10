"""#Exercise: Assignment-4
#We are now ready to begin writing the code
that interacts with the player. We'll be implementing
the playHand function. This function allows the user
to play out a single hand. First, though, you'll need
to implement the helper calculate_handlen function, which
can be done in under five lines of code."""


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    sum_o = 0
    for letters in hand:
        sum_o = sum_o + hand[letters]
    return sum_o

def main():
    """main function"""
    n_num = input()
    a_dict = {}
    for _ in range(int(n_num)):
        data = input()
        l_ist = data.split()
        a_dict[l_ist[0]] = int(l_ist[1])
    print(calculate_handlen(a_dict))
if __name__ == "__main__":
    main()
