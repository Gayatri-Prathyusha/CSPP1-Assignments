"""Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card bal_ance after one year
if a person only pays the minimum monthly payment required by the
# credit card company each month.

# The following variables contain values as described below:
# bal_ance - the outstanding bal_ance on the credit card
# annual_interestrate - annual interest rate as a decimal
# monthly_paymentrate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining
bal_ance. At the end of 12 months, print out the remaining
# bal_ance. Be sure to print out no more than two decimal digits of accuracy
 - so print

# Remaining bal_ance: 813.41
# instead of
# Remaining bal_ance: 813.4141998135

# So your program only prints out one thing: the remaining bal_ance
at the end of the year in the format:
# Remaining bal_ance: 4784.0

# A summary of the required math is found below:
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous bal_ance)
# Monthly unpaid bal_ance = (Previous bal_ance) - (Minimum monthly payment)
# Updated bal_ance each month = (Monthly unpaid bal_ance) +
 (Monthly interest rate x Monthly unpaid bal_ance)"""
def paying_debtoff_inayear(bal_ance, annual_interestrate, monthly_paymentrate):
    """Function definition to calculation of the data"""
    for i in range(12):
        bal_ance = bal_ance - (bal_ance * monthly_paymentrate) + (
            (bal_ance - (bal_ance * monthly_paymentrate)) * (annual_interestrate / 12))
       # print ( "Remaining bal_ance monthly ",round(bal_ance, 2))
    return round(bal_ance, 2)
def main():
    """ main function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: "+str(paying_debtoff_inayear(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()
