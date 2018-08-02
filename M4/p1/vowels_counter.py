#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	 """ definingvowels """
    var_s = "azcbobobegghakl"
    count = 0
    for char in var_s:
        if char in 'AEIOUaeiou':
            count = count+1
    print(count)

if __name__== "__main__":
	main()
