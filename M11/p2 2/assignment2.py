""" #Exercise: Assignment-2
#Implement the update_hand function. Make sure
this function has no side effects: i.e., it must not
mutate the hand passed in. Before pasting your function
definition here, be sure you've passed the appropriate tests in test_ps4a.py."""

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    a_list = hand
    for j in word:
        if j in a_list:
            a_list[j] = a_list[j] - 1
    return a_list

def main():
    """function main"""
    n_num = input()
    ad_ict = {}
    for _ in range(int(n_num)):
        data = input()
        l_ist = data.split()
        ad_ict[l_ist[0]] = int(l_ist[1])
    data_1 = input()
    print(update_hand(ad_ict, data_1))

if __name__ == "__main__":
    main()
