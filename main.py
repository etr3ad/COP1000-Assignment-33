# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

# Input: Get the year, month, and day from the user
year = input("Enter the year: ")
month = input("Enter the month (1-12): ")
day = input("Enter the day (1-31): ")

# Check to be sure date is valid
if int(year) <= MIN_YEAR:  # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH:  # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY:  # invalid day
    validDate = False

# Test to see if date is valid and output result
if validDate == True:
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")
