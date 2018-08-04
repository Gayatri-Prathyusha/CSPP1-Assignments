"""
Given a number int_input, find the product of all the digits
example:
    input: 123
    output: 6
"""
def main():
    """
    Read any number from the input, store it in variable int_input.
    """
    g_num = int(input())
    rem_num = 0
    pro_num = 1
    if g_num == 0:
        print(0)
    elif g_num<0:
        g_num= abs(g_num)
        while g_num != 0:
            rem_num = g_num % 10
            pro_num = pro_num * rem_num
            g_num = g_num // 10

        print('-',pro_num)
    else:
        while g_num != 0:
            rem_num = g_num % 10
            pro_num = pro_num * rem_num
            g_num = g_num // 10
        print(pro_num)

if __name__ == "__main__":
    main()
