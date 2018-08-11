'''
    This is a continuation of the social net_work problem
    There are 3 functions below that have to be completed
    Note: PyLint score need not be 10/10 for this assignment. We expect 9.5/10
'''

def f_ollow(net_work, arg1, arg2):
    '''
        3 arguments are passed to this function
        net_work is a dictionary representing the social net_work
        arg1 and arg2 are two people in the net_work
        follow function is called when arg1 wants to follows arg2
        so, this should result in adding arg2 to the followers list of arg1
        update the net_work dictionary and return it
    '''
    # remove the pass below and start writing your code
    return arg1

def un_follow(net_work, arg1, arg2):
    '''
        3 arguments are passed to this function
        net_work is a dictionary representing the social net_work
        arg1 and arg2 are two people in the net_work
        un_follow function is called when arg1 wants to stop following arg2
        so, this should result in removing arg2 from the followers list of arg1
        update the net_work dictionary and return it
    '''
    # remove the pass below and start writing your code
    return arg2

def delete_person(net_work, arg1):
    '''
        2 arguments are passed to this function
        net_work is a dictionary representing the social net_work
        arg1 is a person in the net_work
        delete_person function is called when arg1 wants to exit from the net_work
        so, this should result in deleting arg1 from net_work
        also, before deleting arg1, remove arg1 from the everyone's followers list
        update the net_work dictionary and return it
    '''
    # remove the pass below and start writing your code
    return arg1

def main():
    '''
        handling testcase input and printing output
    '''
    net_work = eval(input())
    lines = int(input())
    for i in enumerate(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            net_work = f_ollow(net_work, output[1], output[2])
        elif output[0] == "un_follow":
            net_work = un_follow(net_work, output[1], output[2])
        elif output[0] == "delete":
            net_work = delete_person(net_work, output[1])

    print(net_work)

if __name__ == "__main__":
    main()
