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
    z_st = ""
    for char in s_st:
        if char in "!@#$%^&*":
            z_st += " "
        else:
            z_st += char              
    print(z_st)
if __name__ == "__main__":
    main()
