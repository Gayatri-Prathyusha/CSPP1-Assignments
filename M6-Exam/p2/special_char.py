'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    s_st = input()
    i = 0
    for char in s_st:
        if char in "!@#$%^&*":
            s_st[i] = " b"      

        print(s_st[::])

if __name__ == "__main__":
    main()
