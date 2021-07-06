### 7. CHALLENGE
given = input("when were you born (mmddyyyy)? For example, 06011990: ")
today = input("what day is it today (mmddyyyy)? For example, 06172021: ")
assert len(given) == 8
assert len(today) == 8
# function to convert input to day month year integers
def converter(input_string):
    day = input_string[2:4]
    month = input_string[0:3]
    year = input_string[4:8]
    return day, month, year
print(converter(given))


